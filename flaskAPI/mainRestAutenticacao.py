# pip install flask-httpauth
from flask import Flask, jsonify
from flask_httpauth import HTTPBasicAuth
from flask_restful import Resource, Api

auth = HTTPBasicAuth()
app = Flask(__name__)
api = Api(app)

USUARIOS = {
    'reginaldo' : '123',
    'eliza' : '123'
}

@auth.verify_password
def verificacao(login, senha):
    if not (login, senha):
        return False
    return USUARIOS.get(login) == senha

class Desenvolvedor(Resource):
    @auth.login_required()
    def get(self):
        return "Passou do login"

api.add_resource(Desenvolvedor, '/testelogin')

app.run()