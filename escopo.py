
"""
nome = "Jose"
print(nome) # Variável global


for x in range(3): # Range tem a função de alcance, isso siginifica que o for vai funcionar 3 vezes
    nome = "Ana" # Quando dentro do for uma variável receber um novo valor, esse valor será utilizado fora do escopo também
    print(nome) 

print(nome) # Variável alterada pelo for
"""

nome = "Jose"
print(nome)

def mostrarNome(): # Def é uma função e "mostrarNome" é seu nome
    nome = "Maria" # Quando o valor de uma variável é alterado no escopo de uma função ele apenas funciona dentro dessa função
    print(nome)

mostrarNome()
print(nome) # Aqui vemos que o valor da variável global ainda é o mesmo


