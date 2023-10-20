import requests
import secrets

# URL da página de login
login_url = 'https://www.dio.me/sign-in'

# Gerar um valor state aleatório
state = secrets.token_urlsafe(16)

# Dados de login (payload)
login_payload = {
    'client_id': 'spa-core-client',
    'redirect_uri': 'https://web.dio.me/',
    'state': state,
    'response_mode': 'fragment',
    'response_type': 'code',
    'scope': 'openid',
    'nonce': '7159e95c-bccc-4893-b086-95a136a0fddb'
}

# Enviar a solicitação POST para fazer login
login_response = requests.post(login_url, data=login_payload)

# Verificar se o login foi bem-sucedido
if 'Bem-vindo' in login_response.text:
    print("Login bem-sucedido!")
else:
    print("Falha no login.")
