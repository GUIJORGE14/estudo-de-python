# CONDICIONAIS

# São estruturas que permitem ao nosso programa tomar decisões com base em  determinadas condições.
# Em outras palavras, o programa pode executar ações diferentes dependendo de uma situação específica.

# Exemplo:

# Você está em uma cafeteria e está com pouca grana. 
# O capuccino custa 10 reais, café de leite 7 e o café simples 4. 

# Se você tiver 10 reais ou mais na carteira, pode pedir o cappuccino.
# Se você tiver 7 reais ou mais, pode pedir o café com leite. 
# Se não, pede o café simples. 

# Sintaxe básica no Python! 

# if = "se"
# else = "se não"
# elif = "se não + se"


# if condição: 
    # Código a ser executado se a condição for verdadeira. 
# elif outra_condição: 
    # Código executado se a primeira condição for falsa, mas essa for verdadeira.
# else:
    # Código executado se nenhuma das condições anteriores for verdadeira. 

    
# EXEMPLO 


# Verificando a idade para entrada em um evento (18 ANOS+)

idade = int(input("Digite sua idade: ")) # Usuário digita sua idade. 

if idade >= 18:
   print("Você pode entrar no evento.")
else: 
   print("Idade insuficiente para a entrada do evento.")



# VERIFICANDO A NOTA DE UM ALUNO

nota = float(input("Digite a nota do aluno: ")) # Usuário insere a nota

if nota >= 7:
    print("Parabéns, você foi aprovado!")
elif nota >= 5:
    print("Você esta de recuperação, estude para passar de ano!")
else: 
    print("Não foi desta vez, você foi reprovado.")




    
        
