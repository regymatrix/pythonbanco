from flask import Flask, jsonify, request
import json

app = Flask(__name__)

desenvolvedores = [{'nome' : 'Reginaldo',
                    'habilidades': ['Python','Flask']
                    },
                    {'nome': 'Eliza',
                    'habilidades': ['C#', 'Swegger']
                    }]
@app.route("/devall")
def desenvolvedorall():
    return jsonify(desenvolvedores)

@app.route('/dev/<int:id>', methods=['GET','PUT','DELETE'])
def desenvolvedor(id):
    if request.method=='GET':
        try:
            response =desenvolvedores[id]
        except IndexError:
            mensagem ='Dev não existe com esse ID'.format(id)
            response = {'status': 'erro', 'mensagem': mensagem}
        except Exception:
            mensagem = 'Erro desconhecido'
            response = {'status': 'erro', 'mensagem': mensagem}
        return jsonify(response)

    elif request.method=='PUT':
        dados = json.loads(request.data)
        desenvolvedores.append(dados)
        return jsonify(dados)
    elif request.method=='DELETE':
        desenvolvedores.pop(id)
        return jsonify({'status': 'Sucesso','mensagem': 'Registro excluído'})


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