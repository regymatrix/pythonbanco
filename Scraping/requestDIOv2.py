import requests

url ="https://www.dio.me/sign-in"

with requests.session() as session:
    response = session.post(url, auth=("regymatrix@gmail.com","acesso1"))
    print(response.text)

    