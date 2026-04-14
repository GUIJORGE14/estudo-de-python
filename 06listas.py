#Listas e Tuplas
# Tipos de dados que armazenam múltiplos valores, mas têm diferenças importantes.

# Listas
#   - Modicável (pode adicionar, remover e alterar valores)
#   - Mais lenta
#   - Quando precimsamos modificar dados

# Tuplas:
#   - Não é modificável (uma vez criado, não pode ser alterado)
#   - Mais rápida
#   - Quando os dados não devem ser alterados

#Lista
# Definida entre colchetes [] e pode armazenar diferenc


# frutas = ["maçã", "banana", "laranja", "uva"]
# numeros = [1, 2, 3, 4, 5]
# misturada = ["Python", 3.14, True]


# Acessando elementos da lista

# print(frutas[0])  # "maçã"
# print(frutas[1])  # "banana"
# print(frutas[2])  # "laranja" (índice negativo conta de trás para frente)
# print(frutas[-1]) # "uva" 

# Alterando um valor da lista 

# print(frutas) 

# frutas[1] = "abacaxi"
# frutas[2] = "melancia"
# print(frutas)  # ["maçã", "abacaxi", "laranja", "uva"]

# Adicionasndo elementos na lista

# append() adiciona um elemento no final da lista
# insert() adiciona um elemento em uma posição especifíca 

# numeros = [1, 2, 3]
# print(numeros) # [1, 2, 3]

# # numeros.append(4)
# # print(numeros) # [1, 2, 3, 4]

# numeros.insert (1, 10) # (posição, valor)
# print(numeros) # [1, 10, 2, 3, 4] ( inseriu o 10 na posição 1 )

# remove(): removee um item pelo valor 
# pop(): remove um item pelo índice (ou o último item sem nenhum índice for passado)

# frutas = ["maçã", "banana", "laranja", "uva"]
# frutas.remove("banana")
# print(frutas) # ["maçã", "laranja", "uva"]

# frutas.pop(1) # remove o item na posição 1 ( "laranja" )    
# print(frutas) # ["maçã", "uva"]  

# as posições dos índices começam em 0, ou seja, 
# o primeiro item tem índice 0, o segundo tem índice 1, 
# e assim por diante.


# Tuplas
# Tuplas são como listas, definidas entre parênteses () e são imutáveis, 
# # ou seja, não podem ser alteradas após a criação.

# cores = ("vermelho", "verde", "azul")
# numeros = (1, 2, 3, 4, 5)

# # Acessando elementos da tupla
# print(cores[0])  # "vermelho"
# print(cores[-1])  # "azul"

# # Tentando modificar uma tupla (Erro!)
# # cores[1] = "amarelo"  # Isso causará um erro, pois tuplas são imutávei

# Convertendo entre listas e tuplas
# Podemos converter uma lista em tupla usando a função tuple() 
# e vice-versa usando a função list().

tupla = (1, 2, 3)   
lista = list(tupla) # Converte a tupla em lista
lista.append(4) # Agora podemos modificar a lista
tupla = tuple(lista) # Convertendo de volta para tupla
print(tupla) # (1, 2, 3, 4)


# Quando usar tuplas?
# - Quando os dados não devem ser alterados, como coordenadas geográficas,
#  dias da semana, meses do ano, etc.

# meses = ("Janeiro", "Fevereiro", "Março", "Abril")
# print(meses[3]) # "Abril"   
