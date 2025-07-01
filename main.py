import requests
from json.decoder import JSONDecodeError
payload = {"name": "User"}
response = requests.get('https://playground.learnqa.ru/api/hello', params=payload)
print(response.text)


response = requests.get('https://playground.learnqa.ru/api/hello', params=payload)
parsed_response_text = response.json()
print(parsed_response_text['answer'])

response = requests.get('https://playground.learnqa.ru/api/get_text')
print(response.text)
try:

    parsed_response_text = response.json()
    print(parsed_response_text)
except JSONDecodeError:
    print('error json format')

response = requests.get('https://playground.learnqa.ru/api/check_type', params=payload)#в get параметры передаем через параметры
print(response.text)
response = requests.post('https://playground.learnqa.ru/api/check_type', data=payload) #в post передаем параметры в дате
print(response.text)

#статус коды
response = requests.post('https://playground.learnqa.ru/api/get_500')
print(response.status_code)
response = requests.post('https://playground.learnqa.ru/api/get_5000')
print(response.status_code)
print(response.text)

response = requests.post('https://playground.learnqa.ru/api/get_301', allow_redirects=True)#работа с редиректом, если поставить true то он перейдет по редиректу
# и если там будет ок то 200 код
print(response.status_code)
#print(response.text)

#работа с историей ридеректов
first_response = response.history[0]
second_response = response
print(first_response.url)
print(second_response.url)

#работа с заголовками
headers = {'some_headers': '123'}
response = requests.post('https://playground.learnqa.ru/api/show_all_headers', headers= headers)
print(response.text)
print(response.headers)

payload = {'login':'secret_login', 'password':'secret_pass'}
response1 = requests.post('https://playground.learnqa.ru/api/get_auth_cookie', data=payload)
cookie_value = response1.cookies.get('auth_cookie')

cookies = {}
if cookies is not None:
    cookies.update({'auth_cookie': cookie_value})

response2 = requests.post('https://playground.learnqa.ru/api/check_auth_cookie', cookies=cookies)

print(f'test cookies',response2.text)
print(cookie_value)
print(response1.status_code)
print(dict(response1.cookies))
print(response1.headers)


