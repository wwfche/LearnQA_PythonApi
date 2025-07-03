import allure
import pytest
import requests
import string
import random
from lib.base_case import BaseCase
from lib.assertions import Assertions


class TestUserRegister(BaseCase):
# Этот тег объединяет все тесты по глобальной теме, например: работа с пользователями
    @allure.epic('User Registration')
# Здесь указывается конкретная часть функционала, например: регистрация или авторизация
    @allure.feature('API Testing')
    base_url = "https://playground.learnqa.ru/api/user/"

    def get_random_email(self):
        base_part = "testuser"
        domain = "example.com"
        return f"{base_part}{str(random.randint(10000, 99999))}@{domain}"

    def get_default_user_data(self):
        return {
            "password": "123",
            "username": "testuser",
            "firstName": "Test",
            "lastName": "User",
            "email": self.get_random_email()
        }

    def test_create_user_with_invalid_email(self):
        data = self.get_default_user_data()
        data["email"] = "invalidemail.com"

        response = requests.post(self.base_url, data=data)

        assert response.status_code == 400
        assert response.text == "Invalid email format"

    @pytest.mark.parametrize("missing_field", ["password", "username", "firstName", "lastName", "email"])
    def test_create_user_with_missing_field(self, missing_field):
        data = self.get_default_user_data()
        data.pop(missing_field)

        response = requests.post(self.base_url, data=data)

        assert response.status_code == 400
        assert f"The following required params are missed: {missing_field}" in response.text

    def test_create_user_with_short_name(self):
        data = self.get_default_user_data()
        data["firstName"] = "A"

        response = requests.post(self.base_url, data=data)

        assert response.status_code == 400
        assert "The value of 'firstName' field is too short" in response.text

    def test_create_user_with_long_name(self):
        data = self.get_default_user_data()
        data["firstName"] = "A" * 251

        response = requests.post(self.base_url, data=data)

        assert response.status_code == 400
        assert "The value of 'firstName' field is too long" in response.text
