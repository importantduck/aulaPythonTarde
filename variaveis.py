""" 
nome = "Jose" # Variável tipo String
numero = 6 # Variável tipo Int
troco = 4.65 # Variável tipo Float
is_login = True # Variavéis tipo Bool são True ou False e devem ser escritos com a primeira letra maiúscula

print (type(nome)) # Type mostra na tela o tipo de variavél que está sendo usado
print (type(numero))
print (type(troco))
print (type(is_login))
"""

nomes = ["Maria", "João", "Fábio", "Ana", "Zé"]
print (type(nomes)) # Mostra o tipo List
print (nomes) # Mostra a lista
print (nomes[1]) # Mostra a posição 2
print (nomes.pop()) # Exclui a última posição e mostra o nome excluído
print (nomes) # Mostra a lista novamente
nomes.pop() # Exclui a última posição
print (nomes)
nomes.append("Ana") # Adiciona um nome no final da lista
nomes.append("Lorenzo") # A função append adiciona somente um nome por vez
print (nomes)

for x in nomes: # A ideia desse For é mostrar todas as posições x na lista nomes
    print(x) # Tudo que estiver indentado (tab) está dentro do for, o que não estiver está fora
