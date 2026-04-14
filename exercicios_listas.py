# Exercício 1
# Crie uma lista chamada países com alguns 
# nomes de países dentro dela. Em seguida :
# - Adicione um novo país ao fim da lista.
# - Adicione um novo país logo antes da primeira posição da lista.
# - Remova um país pelo nome 
# - Remova um país pelo indice
# - Mostre o total de países na lista.
#                  0          1        2         3        4
lista_paises = ["Brasil", "França", "China", "Vietnã", "Cuba"]
print("Lista original")
print(lista_paises)

lista_paises.append("India") # O método append() sem o valor do índice, o novo país "India" é adicionado ao final da lista.
print("Lista após adicionar a Índia ao final da lista")
print(lista_paises)   

lista_paises.insert(0, "Somália") # O método insert() é usado para adicionar um novo país, o valor 0 indica a posição, ou seja, o início da lista.
print("Lista após adicionar a Somália no início da lista")
print(lista_paises)

lista_paises.remove("França") # O método remove() é usado para remover um país pelo nome.
print("Lista após remover a França")
print(lista_paises) 

lista_paises.pop(3) # O método pop() é usado para remover um país pelo índice, o valor 3 indica a posição do país a ser removido.
print("Lista após remover o país na posição 3")
print(lista_paises)


print(f"Total de países na lista: {len(lista_paises)}") # A função len() é usada para obter o total de países na lista.


# Exercício 2
# Crie um dicíonário que armazene as 
# informações de um carro, informações essas que serão a 
# marca, modelo e ano. Em seguida, exiba uma frase apresentando
# essas informações do carr, no seguinte formato: 
# O carro é um [marca] [modelo] do ano [ano].

carro = {
    "marca": "Volkswagen",
    "modelo": "Nivus",
    "ano": 2025
}

print(f"O carro é um {carro["marca"]} {carro["modelo"]} do ano {carro["ano"]}.") # A frase é exibida usando f-strings, onde as chaves {} são usadas para inserir os valores correspondentes do dicionário 'carro'. 

# Exercício 3
# Crie uma lista com números repetidos,
# e através de conversão desta para um conjunto,
# elemine os valores repetidos.

# Repetidos: 1, 14 e 7. 
        
lista = [1, 14, 23, 42, 14, 1, 7, 55, 90, 7, 12, 1, 33, 22]

print(f"Tipo da lista: {type(lista)}") 
print(lista) 

conjunto_convertido = set(lista) # A função set() é usada para converter a lista em um conjunto, o que automaticamente elimina os valores repetidos.

print(f"Tipo do conjunto convertido: {type(conjunto_convertido)}")
print(conjunto_convertido)

lista_convertida = list(conjunto_convertido) # A função list() é usada para converter o conjunto de volta para uma lista, agora sem os valores repetidos.
print(f"Tipo da lista convertida: {type(lista_convertida)}")
print(lista_convertida)
