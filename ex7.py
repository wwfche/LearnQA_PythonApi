import requests

url = 'https://playground.learnqa.ru/ajax/api/compare_query_type'

response = requests.get(url)
print(response.text)

response = requests.head(url)
print(response.status_code)
print(response.text)

response = requests.get(url, params={'method': 'GET'})
print(response.text)

methods = ['GET', 'POST', 'PUT', 'DELETE']
for actual_method in methods:
    for sent_method in methods:
        if actual_method == 'GET':
            resp = requests.get(url, params={'method': sent_method})
        else:
            resp = requests.request(method=actual_method, url=url, data={'method': sent_method})

        if sent_method != actual_method and "success" in resp.text.lower():
            print(f"Отправляем {actual_method} с method={sent_method}, сервер ответил ОК: {resp.text}")

        if sent_method == actual_method and "success" not in resp.text.lower():
            print(f"Отправляем {actual_method} с method={sent_method}, но сервер НЕ принял: {resp.text}")
