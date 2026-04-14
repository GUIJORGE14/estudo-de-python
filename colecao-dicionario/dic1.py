dicionario = {
    "nome": "Guilherme",
    "idade": 19,
    "altura": 1.78,
}

print(f"Tipo do dicionário: {type(dicionario)}") # O tipo do dicionário é exibido como <class 'dict'>, indicando que a variável 'dicionario' é do tipo dict,
print(dicionario) # O dicionário é exibido como {'nome': 'Guilherme', 'idade': 19, 'altura': 1.78}, mostrando as chaves e valores do dicionário.

dicionario["nome"] = "Brenon"
dicionario["estado"] = "São Paulo" # A chave "estado" não existia anteriormente no dicionário, mas ao atribuir um valor a essa chave, ela é adicionada ao dicionário com o valor "São Paulo".


print("Após a modificação do dicionário:")
print(dicionario)

print(dicionario["nome"]) 
print(dicionario["estado"])