import requests

class TestAPIHeader:
    def test_check_header(self):
        url = 'https://playground.learnqa.ru/api/homework_header'
        response = requests.get(url)

        headers = response.headers
        print(f"Полученные заголовки: {headers}")

        header_name = 'x-secret-homework-header'
        assert header_name in headers, f"Заголовок '{header_name}' не найден в ответе"

        header_value = headers[header_name]
        print(f"Значение заголовка '{header_name}': {header_value}")

        expected_value = 'Some secret value'
        assert header_value == expected_value, f"Ожидалось значение '{expected_value}', но получено '{header_value}'"
