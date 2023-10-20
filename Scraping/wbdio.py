import requests


login_url = 'https://auth.dio.me/'


login_payload = {
    'email': 'reginaldosantanati@gmail.com',
    'password': ''
}

response = requests.get(login_url)
print(response.content)
print(response.status_code)
print(response.headers)
