# append (valor)
# insert (posicao, valor)

lista = ["Banana", "Maçã", "Laranja"]
print(f"Tipo da lista: {type(lista)}")

print("Lista antes do append")
print(lista)

lista.append("Abacaxi") # Adicionando um elemento ao final da lista.

print("Lista depois do append")
print(lista)

lista.insert(1, "Melancia") # Adicionando um elemento na posição 1 da lista.
print("Lista depois do insert")
print(lista)    