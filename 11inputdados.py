# nome = input("Digite seu nome para prosseguir: ")
# print(f"Olá, seja bem-vindo, {nome}!")

# Exemplo de input para avaliar um produto ou serviço, por exemplo:

# numero = input("Olá informe um número de 1 a 5 para avaliar: ")
# print(f"Você avalio com {numero} estrelas!")

# print(type(numero)) O tipo do input é string, mesmo que seja um número, porque o input sempre retorna uma string. 

# print(numero - 1) # Isso vai gerar um erro, porque não é possível subtrair um número de uma string.

# para usar o número como um número, é necessário converter a string para um tipo numérico, como int ou float.


nome = input("Digite seu nome para avaliar: ")
print(f"Olá, seja bem-vindo, {nome}!")

numero = int(input("Olá, informe a quantidade de estrelas de 1 a 5 para avaliar: "))
print(f"O número que avaliou menos 1 são, {numero - 1} estrelas!")

numero_decimal = float(input("Agora, informe a quantidade de estrelas com casas decimais, para ser mais preciso: ")) #float para números decimais e int para números inteiros.
print(f"Você avaliou com {numero_decimal} estrelas!")

