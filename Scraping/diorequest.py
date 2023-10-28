import requests
import secrets

# URL da página de login
login_url = 'https://auth.dio.me/realms/master/protocol/openid-connect/auth?client_id=spa-core-client&redirect_uri=https%3A%2F%2Fweb.dio.me%2F&state=85e38e48-43c5-4ec1-80a0-f68fe3eea620&response_mode=fragment&response_type=code&scope=openid&nonce=941235b2-a84c-4e89-8db8-8d2e7fdbaf2a'


# Dados de login (payload)
login_payload = {
    'session_code': '2CCd7VjgjAAfWodfu_UQyHl3jDobj8j4NmphrclDj80',
    'execution': '1ecc3b57-7fd0-47a5-921c-ba3f9c445fc5',
    'client_id': 'spa-core-client',
    'tab_id': '-r08IpHWKZw',
    'username': 'regymatrix@gmail.com',
    'password': 'acesso1',
    'credentialId': '',
    # Outros parâmetros (se necessário)
    'state': '85e38e48-43c5-4ec1-80a0-f68fe3eea620',
    'response_mode': 'fragment',
    'response_type': 'code',
    'scope': 'openid',
    'nonce': '941235b2-a84c-4e89-8db8-8d2e7fdbaf2a'
}


# Enviar a solicitação POST para fazer login
login_response = requests.post(login_url, data=login_payload)

print(login_response)
# Verificar se o login foi bem-sucedido
if 'Bem-vindo' in login_response.text:
    print("Login bem-sucedido!")
else:
    print("Falha no login.")
