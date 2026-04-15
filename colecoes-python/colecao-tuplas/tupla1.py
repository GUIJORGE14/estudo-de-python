# As tuplas são semelhantes às listas, mas são imutáveis, ou seja, não podem ser alteradas depois de criadas. 
# Elas são definidas usando parênteses () em vez de colchetes [].
# Posições:
#        0  1  2  3  4  
tupla = (1, 2, 3, 4, 5)
print(f"Tipo da tupla: {type(tupla)}")

print("Tupla toda")
print(tupla)

print("Primeiro elemento")
print(tupla[0])

print("Terceiro elemento")
print(tupla[2])

tupla[2] = 10 # Isso vai gerar um erro, pois as tuplas são imutáveis. Você não pode alterar os elementos de uma tupla depois de criada.


