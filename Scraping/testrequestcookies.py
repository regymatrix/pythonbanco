import requests

url = 'https://auth.dio.me/realms/master/protocol/openid-connect/auth?client_id=spa-core-client&redirect_uri=https%3A%2F%2Fweb.dio.me%2F&state=85e38e48-43c5-4ec1-80a0-f68fe3eea620&response_mode=fragment&response_type=code&scope=openid&nonce=941235b2-a84c-4e89-8db8-8d2e7fdbaf2a'

response = requests.get(url)

#print(response.cookies)
for cookie in response.cookies:
    print('Cookie domian: '+ cookie.domain)
    print('Cookie name: ' + cookie.name)
    print('Cookie value: ' + cookie.value)
    print('**************************************')

cookiesmy = dict(username='regymatrix@gmail.com',password='')

response2 = requests.get(url,cookies=cookiesmy)



#print(response2.text)

# Dados de login (payload)
login_payload = {
    'username': 'regymatrix@gmail.com',
    'password': '',
}


# Enviar a solicitação POST para fazer login
login_response = requests.post(url, data=login_payload)

print(login_response.text)