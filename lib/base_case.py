import json.decoder
import requests


class BaseCase:
    def get_json_value(self, response: requests.Response, name: str):
        try:
            response_as_dict = response.json()
        except json.decoder.JSONDecodeError:
            assert False, f"Ответ не в формате JSON. Текст: '{response.text}'"
        assert name in response_as_dict, f"В ответе нет ключа '{name}'"
        return response_as_dict[name]
