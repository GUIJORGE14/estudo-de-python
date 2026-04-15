# Posições:
#        0  1  2  3  4  
tupla = (1, 2, 3, 4, 5)

print(f"Tipo da tupla: {type(tupla)}")

lista_convertida = list(tupla) # A função list() é usada para converter a tupla em uma lista. 



print(f"Tipo da lista convertida: {type(lista_convertida)}")
print(lista_convertida) # No terminal a lista convertida é exibida como [1, 2, 3, 4, 5] com colchetes, indicando que a tupla foi convertida com sucesso em uma lista.

lista_convertida[2] = 14 # Agora que a tupla foi convertida em uma lista, podemos alterar seus elementos. Neste caso, o elemento na posição 2 (que originalmente era 3) 
                         # é alterado para 14.

tupla_convertida = tuple(lista_convertida)
print(tupla_convertida) # A função tuple() é usada para converter a lista de volta para uma tupla. No terminal, a tupla convertida é exibida como (1, 2, 14, 4, 5), 
                        # mostrando que o elemento na posição 2 foi alterado para 14.
tupla = tuple(lista_convertida) 
print(f"tupla original: {tupla}") # A tupla original é atualizada com os valores da lista convertida, resultando em (1, 2, 14, 4, 5).




