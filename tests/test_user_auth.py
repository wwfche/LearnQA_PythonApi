import requests
from lib.base_case import BaseCase
from lib.assertions import Assertions


class TestUserAuth(BaseCase):
    def test_auth_user(self):
        data = {
            'email': 'vinkotov@example.com',
            'password': '1234'
        }

        response = requests.post("https://playground.learnqa.ru/api/user/login", data=data)

        Assertions.assert_code_status(response, 200)

        Assertions.assert_json_value_by_name(
            response,
            "user_id",
            5,
            "Неверный user_id при входе"
        )
