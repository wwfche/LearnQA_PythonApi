import allure
import pytest
import requests
from lib.base_case import BaseCase
from lib.assertions import Assertions


class TestUserEdit(BaseCase):
# Этот тег объединяет все тесты по глобальной теме, например: работа с пользователями
    @allure.epic('User Editing')
# Здесь указывается конкретная часть функционала, например: регистрация или авторизация
    @allure.feature('API Testing')

    def setup_method(self):
        # создаем нового пользователя для изоляции тестов
        self.register_data = self.prepare_registration_data()
        self.response = requests.post("https://playground.learnqa.ru/api/user/", data=self.register_data)

        Assertions.assert_code_status(self.response, 200)
        self.user_id = self.get_json_value(self.response, "id")

    def test_edit_without_auth(self):
        response = requests.put(f"https://playground.learnqa.ru/api/user/{self.user_id}", data={"firstName": "Hacker"})

        Assertions.assert_code_status(response, 400)
        assert response.text == "Auth token not supplied", "Ошибка: редактирование без авторизации не заблокировано"

    def test_edit_as_another_user(self):
        # Авторизация как другой пользователь
        other_login_data = {
            "email": "vinkotov@example.com",
            "password": "1234"
        }
        response_login = requests.post("https://playground.learnqa.ru/api/user/login", data=other_login_data)
        Assertions.assert_code_status(response_login, 200)

        auth_sid = response_login.cookies.get("auth_sid")
        token = response_login.headers.get("x-csrf-token")

        response_edit = requests.put(
            f"https://playground.learnqa.ru/api/user/{self.user_id}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid},
            data={"firstName": "HackedName"}
        )

        Assertions.assert_code_status(response_edit, 400)
        assert response_edit.text == "You can edit only your own data", "Ошибка: чужие данные можно редактировать"

    def test_edit_email_to_invalid(self):

        login_data = {
            "email": self.register_data["email"],
            "password": self.register_data["password"]
        }

        response_login = requests.post("https://playground.learnqa.ru/api/user/login", data=login_data)
        Assertions.assert_code_status(response_login, 200)

        auth_sid = response_login.cookies.get("auth_sid")
        token = response_login.headers.get("x-csrf-token")


        response_edit = requests.put(
            f"https://playground.learnqa.ru/api/user/{self.user_id}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid},
            data={"email": "invalidemail.com"}
        )

        Assertions.assert_code_status(response_edit, 400)
        assert response_edit.text == "Invalid email format", "Ошибка: некорректный email принят системой"

    def test_edit_first_name_to_one_char(self):
        login_data = {
            "email": self.register_data["email"],
            "password": self.register_data["password"]
        }

        response_login = requests.post("https://playground.learnqa.ru/api/user/login", data=login_data)
        Assertions.assert_code_status(response_login, 200)

        auth_sid = response_login.cookies.get("auth_sid")
        token = response_login.headers.get("x-csrf-token")

        response_edit = requests.put(
            f"https://playground.learnqa.ru/api/user/{self.user_id}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid},
            data={"firstName": "A"}
        )

        Assertions.assert_code_status(response_edit, 400)
        assert "too short" in response_edit.text, "Ошибка: короткое имя не было отклонено"
