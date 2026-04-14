# Exercício 1

# Crie 4 variáveis com os seguintes nomes:
# - nome
# - idade
# - altura
# uma variável booleana para representar se a pessoa gosta de programação.

# Preencha essas variáveis com informações de alguém, em seguida exiba o tipo de cada variável.

nome = "Lucas" 
idade = 22
altura = 1.77
gosta_de_programação = True

print(type(nome))                  
print(type(idade))
print(type(altura))
print(type(gosta_de_programação))

# <class 'str'>
# <class 'int'>
# <class 'float'>
# <class 'bool'>


# Exercicio 2

# Usando as mesmas variáveis do exercício anterior, exiba uma frase com todas as informações usando f-strings. 

print(f"O nome dele é {nome}, ele tem {idade} anos, mede {altura} de altura e se ele gosta de programação: {gosta_de_programação}.")


# Exercicio 3

# Crie uma variável chamada 'estuda_python' atribua a ela um valor booleano.

# Depois, exiba uma frase dizendo se a pessoa estuda python ou não.

nome = "Felipe"
estuda_python = False

print(f"{nome}, etuda python: {estuda_python}.")



