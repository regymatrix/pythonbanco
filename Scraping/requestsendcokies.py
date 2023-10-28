import requests
from urllib.parse import urlparse, parse_qs

original_url= 'https://web.dio.me'

#response = requests.get(original_url)
#final_url = response.url
#print(final_url)

# Iniciar uma sessão
session = requests.Session()
# Configurar a sessão para seguir redirecionamentos
session.max_redirects = 60  # Defina um limite para evitar redirecionamentos infinitos
# Fazer uma solicitação GET para a URL original com a sessão
response = session.get(original_url)
# Obter a URL final após o redirecionamento
final_url = response.url
print("URL final após redirecionamento:", final_url)



parsed_url = urlparse(final_url)
query_parameters = parse_qs(parsed_url.query)
print("Parâmetros da URL redirecionada:", query_parameters)


# Iniciar uma sessão
session = requests.Session()

# Configurar a sessão para seguir redirecionamentos
session.max_redirects = 30  # Defina um limite para evitar redirecionamentos infinitos

# Fazer uma solicitação GET para a URL original com a sessão
response = session.get(original_url)

# Obter a URL final após o redirecionamento
final_url = response.url

print("URL final após redirecionamento:", final_url)