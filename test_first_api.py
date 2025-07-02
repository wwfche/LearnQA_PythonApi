import requests
class TestFirstApi:
    def test_hello_call(self):
        url = 'https://playground.learnqa.ru/ajax/api/hello'

        name = 'Svetlana'
        data = {'name':name}

        response = requests.get(url, params=data)

        assert response.status_code == 200, 'worng status code'

        response_dict = response.json()
        assert 'answer' in response_dict, 'no answer in response'