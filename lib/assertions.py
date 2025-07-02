class Assertions:
    @staticmethod
    def assert_json_value_by_name(response, name, expected_value, error_message):
        try:
            response_as_dict = response.json()
        except Exception:
            assert False, f"Ответ не в JSON формате. Текст ответа: '{response.text}'"

        assert name in response_as_dict, f"Ответ JSON не содержит ключ '{name}'"
        actual_value = response_as_dict[name]
        assert actual_value == expected_value, error_message

    @staticmethod
    def assert_code_status(response, expected_status):
        assert response.status_code == expected_status, \
            f"Ожидался статус-код {expected_status}, но получен {response.status_code}"
