# Laços de Repetição ( for e while )

# Imagine que você precisa pedir para alguém contar de 0 a 100 
# e escrever cada número em um papel. Fazer isso manualmente 
# seria muito cansativo e demorado, né?  

# Agora, imagine um programa que pode fazer essa contagem automaticamente, 
# sem precisar repetir o mesmo comando 100 vezes. É exatamente isso que os
# laços de repetição fazem! 

# Os laços de repetição são usados para executar um bloco de código várias vezes,
# até que uma condição seja atingida. 

# Python tem dois tipos principais de laços: 

# for -> Quando sabemos quantas vezes queremos repetir algo. 
# while -> Quando queremos repetir algo até que uma condição se torne falsa. 



# FOR 

# O FOR  é utilizado quando sabemos quantas vezes queremos repetir um bloco de código. 
# Ele percorre uma sequência de valores, como uma lista, um intervalo de números
# ou até mesmo letras de uma palavra. 

# Estrura: 

# for variavel in sequencia:
#     # Código a ser repetido



# Contando de 1 a 5 com o FOR 

# {1, 2, 3, 4, 5}
 
# for numero in range (1, 11): 
#     print(numero) 

# O range (1, 6) gera números de 1 a 5 (o 6 não é incluído).

# Percorrendo uma lista de compras

# compras = ["Arroz", "Feijão", "Carne", "Alface", "Melancia", "Macarrão", "Coca-Cola"]

# for item in compras:
#     print(f"📌 Comprar: {item}")



# # Percorrendo as lestras de uma palavra

# palavra = "Guilherme Jorge"

# for letra in palavra:
#     print(letra)


# WHILE     

# O while é usado quando não sabemos quantas vezes a repetição vai acontecer,
# mas sabemos a condição que deve ser atendida para continuar.

# while condição: 
# Código a ser repetido enquanto a conidção for verdadeira


# obs: Cuidado com loops infinitos!
# Se a condição nunca mudar para False, o código nunca parte de rodar. 


# Contagem regressiva 

# contador = 5 

# while contador > 0:
#     print(contador)
#     contador -= 1 # Diminui o contador a cada repetição

# print("FOGOOOOO!!! Feliz ano novo!")


# Pedindo uma senha até acertar

senha_correta = "1234"
senha = ""

while senha != senha_correta:
    senha = input ("Digite a senha: ")

print("Senha correta! Acesso liberado.")




