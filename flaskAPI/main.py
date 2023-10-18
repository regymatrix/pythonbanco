from flask import Flask, jsonify, request
import json

app = Flask(__name__)

@app.route("/")
def home():
    return 'Página inicial [Teste]'

@app.route("/parmteste/<numero>",methods=['GET','POST'])
def parmteste(numero):
    return 'Valor: {}'.format(numero)

@app.route("/pessoa")
def pessoa():
    return jsonify({'name':'Reginaldo',
                    'profissao':'Dev'
    })
@app.route('/soma/<int:valor1>/<int:valor2>')
def soma(valor1,valor2):
    return jsonify({'soma': valor1+valor2})

@app.route('/somav',methods=['POST','GET','PUT'])
def somav():
    if request.method=='POST':
        dados = json.loads(request.data)
        total =sum(dados['valores'])
    elif request.method=='GET':
        total = 0
    return jsonify({'soma':total})




app.run(debug=True)