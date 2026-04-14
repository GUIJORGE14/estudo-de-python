# pop (posição) remove pelo valor, se não for informado a posição, o pop remove o último elemento da lista.
#           0        1        2      3      4   
lista = ["Banana", 7.77 , "Laranja", 14 , True]
print(f"Tipo da lista: {type(lista)}")

print("Lista antes do pop")
print(lista)

tam = len(lista) # Obtendo o tamanho da lista utilizando a função len().
print(f"Tamanho da lista: {tam}")

lista.pop(2) # Removendo o elemento da posição 2 da lista, que é "Laranja".
print("Lista depois do pop")
print(lista)

tam = len(lista) 
print(f"Tamanho da lista: {tam}")



