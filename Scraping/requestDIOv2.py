import requests

url ="https://www.dio.me/sign-in"

r = requests.get(url)
cookies = r.cookies
st = r.status_code

for cok in cookies:
    print(f"Nome do cookie: {cok.name}")
    print(f"Valor do cookie: {cok.value}")



