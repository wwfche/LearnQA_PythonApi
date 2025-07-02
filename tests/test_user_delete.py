import requests
from lib.base_case import BaseCase
from lib.assertions import Assertions


class TestUserDelete(BaseCase):
    def test_delete_protected_user(self):
        credentials = {
            'email': 'vinkotov@example.com',
            'password': '1234'
        }

        login_response = requests.post("https://playground.learnqa.ru/api/user/login", data=credentials)
        token = login_response.headers.get("x-csrf-token")
        sid = login_response.cookies.get("auth_sid")

        delete_response = requests.delete(
            "https://playground.learnqa.ru/api/user/2",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": sid}
        )

        Assertions.assert_code_status(delete_response, 400)
        assert delete_response.text == "Please, do not delete test users with ID 1, 2, 3, 4 or 5."

    def test_delete_own_account(self):
        new_user = self.prepare_registration_data()
        create_response = requests.post("https://playground.learnqa.ru/api/user/", data=new_user)
        user_id = self.get_json_value(create_response, "id")

        login_response = requests.post("https://playground.learnqa.ru/api/user/login", data={
            "email": new_user["email"],
            "password": new_user["password"]
        })
        token = login_response.headers.get("x-csrf-token")
        sid = login_response.cookies.get("auth_sid")

        delete_response = requests.delete(
            f"https://playground.learnqa.ru/api/user/{user_id}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": sid}
        )
        Assertions.assert_code_status(delete_response, 200)

        check_response = requests.get(
            f"https://playground.learnqa.ru/api/user/{user_id}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": sid}
        )
        Assertions.assert_code_status(check_response, 404)
        assert check_response.text == "User not found"

    def test_delete_user_as_different_account(self):
        user_a = self.prepare_registration_data()
        res_a = requests.post("https://playground.learnqa.ru/api/user/", data=user_a)
        user_a_id = self.get_json_value(res_a, "id")

        user_b = self.prepare_registration_data()
        requests.post("https://playground.learnqa.ru/api/user/", data=user_b)

        login_b = requests.post("https://playground.learnqa.ru/api/user/login", data={
            "email": user_b["email"],
            "password": user_b["password"]
        })
        token = login_b.headers.get("x-csrf-token")
        sid = login_b.cookies.get("auth_sid")

        delete_attempt = requests.delete(
            f"https://playground.learnqa.ru/api/user/{user_a_id}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": sid}
        )

        check_response = requests.get(
            f"https://playground.learnqa.ru/api/user/{user_a_id}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": sid}
        )

        assert check_response.status_code == 200
        assert "username" in check_response.json()
