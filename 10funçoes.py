# Funções 

# Funções são blocos de códsigos reutilizáveis que realizam
# uma tarefa específica. Em vez de escrever o mesmo código 
# várias vezes, criamos uma função e apenas a chamamos quando precisamos dela.

# Exemplo real
# imagine que você tem que caucular o imposto de vários produtos em uma loja
# Em vez de repitir a mesma conta várias vezes, você pode criar uma função
# chamada calcular_imposto() e usá-la sempre que precisar calcular o imposto de um produto. 


# def saudacao(nome):
#     print(f"Olá, {nome}! Bem-vindo ao curso de Python!")

# saudacao("Guilherme")   


#  # Retorno de valores 

# def somar(a, b, c):
#      return a + b - c 

# # Chamado a função e armazenamento o resultado

# resultado = somar(5, 3, 2)
# print(f"O resultado da soma é {resultado}")



# Funções com vários parâmetros     

def calcular_media(n1, n2, n3):
    media = (n1 + n2 + n3)/3    
    return media

# Chamando a função 

resultado = calcular_media(7, 8, 5)
print(f"A média é {resultado:.2f}")





