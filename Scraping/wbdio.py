import requests


login_url = 'https://auth.dio.me/'


login_payload = {
    'email': 'reginaldosantanati@gmail.com',
    'password': 'Cabrunco@123'
}

response = requests.get(login_url)
print(response.content)
print(response.status_code)
print(response.headers)
