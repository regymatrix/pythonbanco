from flask import Flask, jsonify
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

desenvolvedores = [{'nome' : 'Reginaldo',
                    'habilidades': ['Python','Flask']
                    },
                    {'nome': 'Eliza',
                    'habilidades': ['C#', 'Swegger']
                    }]

class Desenvolvedor(Resource):
    def get(self, id):
        try:
            response = desenvolvedores[id]
        except IndexError:
            mensagem = 'Dev não existe com esse ID'.format(id)
            response = {'status': 'erro', 'mensagem': mensagem}
        except Exception:
            mensagem = 'Erro desconhecido'
            response = {'status': 'erro', 'mensagem': mensagem}
        return jsonify(response)
    def put(self):
        pass

    def delete(self):
        pass

class ListaDev(Resource):
    def get(self):
        return desenvolvedores

api.add_resource(Desenvolvedor, '/dev/<int:id>/')
api.add_resource(ListaDev,'/devall')

app.run()
