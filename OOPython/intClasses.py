class Bicicleta:
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
    
    def buzinar(self):
        print("Plim, plim...")
    
    def parar(self):
        print("Parando bicicleta...")

    def correr(self):
        print("Vrunmmmm...")

    def _str_(self):
        return f"{self.__class__.__name__}: {[f'{chave}={valor}' for chave, valor in self.__dict__]}"

b1 = Bicicleta("vermelha","caloi",2022,500)
b1.buzinar()
b1.correr()
b1.parar()
print(b1.modelo)




