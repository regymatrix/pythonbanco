lista = [4,2,3,4,5,2,1,4]
print( set(lista))

listaSet =([1,2,3,4,1])
listaSet = {1,2,1,3,4}

print(listaSet)

numeros = {1,2,3,4}
numLista = list(numeros)
print(numLista[2])

conjuntoA = {1,2}
conjuntoB = {2,3,4}


print(conjuntoA.union(conjuntoB))
print(conjuntoA.intersection(conjuntoB))
print(f"O que tem em A e não tem em B {conjuntoA.difference(conjuntoB)}")
print(f"O que tem em B e não tem em A {conjuntoB.difference(conjuntoA)}")
print(f"Todos os elementos que não são comuns {conjuntoA.symmetric_difference(conjuntoB)}")
print(f"Todos os elementos de A estão em B {conjuntoA.issubset(conjuntoB)}")
print(f"Todos os elementos de A não existe em B {conjuntoA.isdisjoint(conjuntoB)}")
print(f"3 está em B {3 in conjuntoB}")
