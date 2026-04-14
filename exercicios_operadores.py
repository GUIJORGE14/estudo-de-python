# Exercício 1 - Operadores Aritméticos

# Crie duas variáveis, com valores inteiros. 

# Faça com essas variáveis todas as operções aritméticas 
# monstrandas na aula. Armazene os resultados de cada 
# operação em variáveis separadas, e utilize fstrings
# para imprimir cada resultado no seguinte modelo:

# (exemplo para a soma)

# "Resultado no seguinte modelo:"

# Resposta:

x = 100
y = 4 

resultado_soma = x + y
resultado_sub = x - y 
resultado_mult = x * y 
resultado_div  = x / y
resultado_pot = x ** y
resultado_div_int = x // y
resultado_resto = x % y


print(f'Resultado da soma: {resultado_soma}')
print(f'Resultado da sub: {resultado_sub}')
print(f'Resultado da mult: {resultado_mult}')
print(f'Resultado da div: {resultado_div}')
print(f'Resultado da pot: {resultado_pot}')
print(f'Resultado da div int: {resultado_div_int}')
print(f'Resultado do resto da div: {resultado_resto}')


# Exercicio 2 

# Crie duas variáveis, uma contendo um valor com três casas
# decimais, e outra contendo um valor deciaml com duas casas decimais.

# Multiplique essas duas variaveis, e apresente o resultado 
# contendo duas casas decimais. 

# Resposta:

valor_1 = 34.253
valor_2 = 3.45

resultado = valor_1 * valor_2
resultado_formatado = round(resultado, 2)

print(f"resultado antes da formatação: {resultado}")
print(f"resultado formatado: {resultado_formatado}")


# Exercicio 3

# Crie duas variáveis inteiras. Faça todas as operações relacionais 
# apresentadas na aula, exibindo o resultado de cada comparação.

# Resposta:

a = 24 
b = 42 

print("a é igual a b:", a == b)
print("a é diferente de b", a != b)
print("a é maior do que b?", a > b)
print("a é menor do que b?", a < b)
print("a é maior ou igual a b?", a >= b)
print("a é menor ou igual a b?", a <= b)


# Exercício 4

# Pense na seguinte situação: ano que vem, eu vou viajar
# Mas, eu só consigo viajar se eu estiver de férias do 
# trabalho e tiver conseguido comprar as passagens. 
 
# Não consegui as férias no trabalho, mas consegui comprar as passagens.
 
# Se eu fosse utilizar variáveis booleanas do python, e um
# operador lógico para montar um código para exibir se
# desse jeito eu vou ou não conseguir viajar, como esse
# código ficaria?

# Resposta:

esta_de_ferias = False
comprou_passagens = True

vai_viajar = esta_de_ferias and comprou_passagens   

print(f"Vai conseguir viajar? {vai_viajar}")


# Exercício 5

# Eu só posso participar de um evento na minha cidade se
# eu tiver um convite, ou então, se meu nome estiver na 
# na lista da entrada.

# Meu nome não está na lista, mas eu tenho um convite.

# Seu eu fosse utilizar variáveis boolenanas do python, e 
# um operador lógico para montar um código para exibir se
# desse jeito eu vou ou não conseguir entrar, como esse
# código ficaria?

# Resposta:        

nome_da_lista = False
tem_convite = True

entra_no_evento = nome_da_lista or tem_convite
print(f"Vai conseguir entrar no evento? {entra_no_evento}")

