# Exercício 1 

# Peça para o usuário digitar seu nome e exiba
# uma saudação personalizada. 
# Ex: "Olá Fulano! Seja bem-vindo!"

# Resposta:

nome = input("Digite seu nome para prosseguir: ")
print(f"Olá, seja bem-vindo, {nome}!")


# Exercício 2

# Peça dois números inteiros ao usuário, some-os e
# apresente o resultado em uma frase no formato 
# abaixo.
# Ex: O resultado é 20

numero = int(input("Digite um número inteiro: "))
numero2 = int(input("Digite outro número inteiro: "))
soma = numero + numero2
print(f"O resultado é {soma}")


# Exercício 3   

# Peça dois nduas notas ao usuário, (podem ter
# casas decimais) e mostre a média delas. 

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: ")) 

media = (nota1 + nota2) / 2
media_round = round(media, 1)

print(f"A média das notas é {media_round}")

# Exercício 4

# Peça ao usuário o nome, idade e estado dele,
# e exiba uma frase completa no formato abaixo:
# Ex: Fulano tem 21 anos e mora no estado da Bahia.

nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade:"))
estado = input("Digite o estado onde mora: ")

print(f"{nome} tem {idade} anos e mora no estado de {estado}.")
