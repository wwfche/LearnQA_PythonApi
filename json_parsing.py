import json
import requests

string_as_json_format = '{"answer": "Hello, User"}'
ob = json.loads(string_as_json_format)
print(ob['answer'])

key = 'answer1'
if key in ob:
    print(ob[key])
else:
    print(f'Ключа {key} в JSON нет')