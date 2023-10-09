pessoa = {"nome":"Guilherme","idade":28}

cargos = dict(nome="Supervisor", salario=1000)

pessoa["cargo"] = cargos

print(pessoa["cargo"]["nome"])
print(pessoa["cargo"]["salario"])

cidade = dict.fromkeys(["estado","cidade"],"vazio")
print(pessoa.get("idade"))


print(pessoa.keys())
print("nome" in pessoa)
print("Supervisor" in cargos)