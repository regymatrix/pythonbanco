import urllib

from bs4 import BeautifulSoup
import requests


login_url = 'https://www.workana.com/pt/login'


# Crie uma sessão para manter a autenticação
session = requests.Session()


login_payload = {
    'csrf_name': 'csrf652dd49d8d39e',
    'csrf_value': '57d3c1fed85392604f174669f8e3019c',
    'dcst-input':'4bfc3c1c68bc170995298ba5a7eb897a0d7414664f45ff041889bcee1ae72d75',
    'r': '',
    'email': 'reginaldosantanati@gmail.com',
    'password': ''
}


login_response = session.post(login_url, data=login_payload)


if 'Bem-vindo' in login_response.text:
    print('Login bem-sucedido!')
else:
    print('Falha no login.')


