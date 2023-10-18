import requests


login_url = 'https://www.workana.com/pt/login'


login_payload = {
    'email': 'reginaldosantanati@gmail.com',
    'password': 'Cabrunco@123'
}

response = requests.get(login_url)
print(response.content)
print(response.status_code)
print(response.headers)

#r = requests.post(login_url, data=login_payload)
#print(r.text)
