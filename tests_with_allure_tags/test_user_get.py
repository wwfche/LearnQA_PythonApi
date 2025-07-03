import allure
import requests
from lib.base_case import BaseCase
from lib.assertions import Assertions


class TestUserGet(BaseCase):
# Этот тег объединяет все тесты по глобальной теме, например: работа с пользователями
    @allure.epic('User Info Retrieval')
# Здесь указывается конкретная часть функционала, например: регистрация или авторизация
    @allure.feature('API Testing')
    def test_get_user_data_as_another_user(self):
        # Авторизуемся как user_id=2
        login_data = {
            "email": "vinkotov@example.com",
            "password": "1234"
        }

        response_login = requests.post("https://playground.learnqa.ru/api/user/login", data=login_data)
        Assertions.assert_code_status(response_login, 200)

        auth_sid = response_login.cookies.get("auth_sid")
        token = response_login.headers.get("x-csrf-token")
        user_id_from_auth = self.get_json_value(response_login, "user_id")


        target_user_id = 1 if user_id_from_auth != 1 else 3

        response_user = requests.get(
            f"https://playground.learnqa.ru/api/user/{target_user_id}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid}
        )

        Assertions.assert_code_status(response_user, 200)
        response_dict = response_user.json()

        assert "username" in response_dict, "В ответе нет поля 'username'"
        assert "email" not in response_dict, "Должен быть скрыт email чужого пользователя"
        assert "firstName" not in response_dict, "Должен быть скрыт firstName чужого пользователя"
        assert "lastName" not in response_dict, "Должен быть скрыт lastName чужого пользователя"
