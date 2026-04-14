# Exercicio 1

# Crie duas variáveis, uma chamada nome e outra chamada idade.
# Atribua a elas o nome e idade de uma pessoa, e mostre essas
# informações na tela no seguinta formato: 
# "Meu nome é [nome] e eu tenho [idade] anos."

nome = "Guilherme"
idade = 19

print(f"Me nome é {nome} e eu tenho {idade} anos.")

# Exercicio 2

# Crie duas variáveis: nome e animal, contendo o nome e o animal
# de estimação de uma pessoa. Em seguida, mostre essas informações
# no seguinte formato, usando as três formas de exibir texto junto
# com variáveis:
# "O animal de estimação é um [animal] e ele pertence a [nome]."

nome = "Jorge"
animal = "Cachorro"

print(f"O animal de estimação é um {animal} e ele pertence a {nome}.") # ultilizadno o f antes da string, o python entende que as variáveis estão dentro das chaves e as substitui pelo valor delas.

print("O animal de estimação é um", animal, "e ele pertence a", nome, ".") # utilizando a vírgula, o python já coloca um espaço entre as variáveis. 

print("O animal de estimação é um " + animal + " e ele pertence a " + nome + ".") # é necessario colocar os espaços no final e no início das variáveis para que a frase fique correta.


# Exercicio 3

# Crie uma constante chamada PAIS com o valor "China", uma vairavel chamada 
# "nome" com o nome de alguém, e outra chamada "idade" com a idade desta pessoa.
# Exiba essas informações no seguinte formato:
# "[nome] mora no país [PAIS] e tem [idade] anos."


PAIS = "China"
nome = "Heloisa"
idade = 23 

print(f"{nome} mora no país {PAIS} e tem {idade} anos.")







