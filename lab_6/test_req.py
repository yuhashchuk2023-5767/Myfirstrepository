import requests

response = requests.get('https://google.com')

print(f"Версія бібліотеки requests: {requests.__version__}")
print(f"Статус відповіді від Google: {response.status_code}")

if response.status_code == 200:
    print("Успіх! Бібліотека працює правильно.")