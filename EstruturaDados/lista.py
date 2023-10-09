
lista_simples =["Maria","joão"]
list_vazia =[]
letras = list("Reginaldo")

print(letras[4])
print(list(range(10)))
print(letras)
print(letras[0])
print(letras[-1])

print(letras[::])
print(f"reodernado: {letras[::-1]}")

for caracteres in letras:
    print(caracteres)

for indice, carac in enumerate(letras):
    print(f"{indice}: {carac}")

numeros = [1, 30, 21, 22, 9, 65]
pares=[]

for num in numeros:
    if num % 2==0:
        pares.append(num)

print(pares)
impar = [num for num in numeros if num % 2 ==1]
print(impar)
quadrado = [num **2 for num in numeros]
print(quadrado)

linguagens=["python","c","java"]
linguagens.sort(key=lambda x: len(x), reverse=True)

print(linguagens)