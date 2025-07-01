import requests
import time

url = 'https://playground.learnqa.ru/ajax/api/longtime_job'

# 1 Создаем задачу
response = requests.get(url)
data = response.json()

token = data.get("token")
wait_time = data.get("seconds")

print(f"Создана задача. Token: {token}, ждать: {wait_time} сек.")

# 2 Проверяем статус ДО готовности
response_before = requests.get(url, params={"token": token})
data_before = response_before.json()

print(f"Статус ДО ожидания: {data_before.get('status')}")

# Проверка: статус должен быть "Job is NOT ready"
if data_before.get("status") != "Job is NOT ready":
    print("статус 'Job is NOT ready'")
else:
    print("Статус OK")

# 3. Ждем указанное количество секунд
time.sleep(wait_time)

# 4. Проверяем статус ПОСЛЕ ожидания
response_after = requests.get(url, params={"token": token})
data_after = response_after.json()

print(f"Статус ПОСЛЕ ожидания: {data_after.get('status')}")
print(f"Результат: {data_after.get('result')}")

# Проверки
if data_after.get("status") != "Job is ready":
    print("статус должен быть 'Job is ready'")
elif "result" not in data_after:
    print("result отсутствует")
else:
    print("Статус и результат ОК")
