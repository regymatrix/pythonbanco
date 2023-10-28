import json

class Conta:
    def __init__(self, agencia,  numero_conta, dac):
        self.agencia = agencia
        self.numero= numero_conta
        self.dac= dac        

class Cliente:
    def __init__(self, cpf,  nome):
        self.cpf = cpf
        self.nome = nome
        self.contas =[]

cliente = Cliente('0980888','Reginaldo')
conta1 = Conta('0001','989898','8')
conta2 = Conta('0002','555555','4')

cliente.contas.append(conta1)
cliente.contas.append(conta2)
 
cliente_json = json.dumps(cliente, default=lambda o: o.__dict__)

cliente_json_string = str(cliente_json)

print(cliente_json_string)

#Codigo para JSON
# using Newtonsoft.Json;
# // Suponhamos que você tenha a string JSON no C# em algum ponto:
# string clienteJsonString = "seu_json_aqui";
# // Deserializar a string JSON em um objeto Cliente
# Cliente cliente = JsonConvert.DeserializeObject<Cliente>(clienteJsonString);

# // Agora, você tem o objeto Cliente com os mesmos atributos do JSON
