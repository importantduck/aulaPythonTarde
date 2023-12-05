for x in range(5):
    print(x)

    lista = ["Maria", "Joao", "Pedro"]
    for x in lista:
        print(x)

soma = 0
listaNumeros = [6, 4, 5, 7]
for x in listaNumeros:
    soma += x
print(soma)

numeros = [4, 9, 12, 15]
print(len(numeros)) # A função len me mostra quantos itens existem em um list

i = 0
while i < len(numeros):
    print (numeros[i])
    i += 1 # Isso é o mesmo que i = i + 1