import requests

# URL original
original_url = 'https://web.dio.me/'

# Fazer uma solicitação GET para a URL original
response = requests.post(original_url, allow_redirects=False)

# Verificar se houve redirecionamento
if response.status_code == 302:
    # Acessar a URL de redirecionamento
    new_url = response.headers['Location']
    print("URL final após redirecionamento:", new_url)
else:
    print("Não houve redirecionamento. A URL original é:", original_url)