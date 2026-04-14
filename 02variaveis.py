# Variáveis e tipos de dados "básicos"

# Uma variavel é um espaço na memória onde armazenamos um valor

# <nome da var> = <valor> 

nome = "Guilherme" # variável do tipo string (texto), sempre entre aspas (""OU""")
idade = 19         # var do tipo int (núm inteiros)
altura = 1.75      # var do tipo float (núm com casa decimal)
dev = True         # var do tipo booleana, valores lógicos (true/false)  

# print(f"Olá, {nome}! Você tem {idade} anos e mede {altura}m. É desenvolvedor? {dev}")

nome = input("Digite seu nome: ") # entrada de texto 
idade = int(input("Digite sua idade: ")) # entrada de texto convertida pra int 
altura = float(input("Digite sua altura em metros: ")) # entrada convertida pra float

print(f"Olá, {nome}! Você tem {idade} anos e mede {altura}m.")



