import requests

def test_homework_cookie():
    url = 'https://playground.learnqa.ru/api/homework_cookie'
    response = requests.get(url)

    cookies = response.cookies
    print(f"Полученные cookies: {cookies}")

    cookie_name = 'HomeWork'
    assert cookie_name in cookies, f"Ожидалась cookie с именем '{cookie_name}', но она не найдена"

    cookie_value = cookies.get(cookie_name)
    print(f"Значение cookie '{cookie_name}': {cookie_value}")

    expected_value = 'hw_value'
    assert cookie_value == expected_value, f"Ожидалось значение '{expected_value}', но получено '{cookie_value}'"
