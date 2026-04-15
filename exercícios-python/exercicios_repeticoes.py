# Exercício 1 
# Monte um programa que peça, um de cada vez, vários números  para
# o usuário até que elel digite 0. Ao fim, mostre a soma dde todos 
# esse número que ele digitou.

numero_lido = int(input("Informe um número: "))
somatorio = 0;

while numero_lido != 0:
    somatorio = somatorio + numero_lido 
    numero_lido = int(input("Informe mais um número: "))

print(f"O somatório dos números digitados é: {somatorio}    ")

# Exercício 2
# Monte um programa que, para um determinado número
# informado pelo usuário (limite), exiba o produtório dos números
# de 1 até esse limite.

limite = int(input("Informe o limite:  "))
produtorio = 1 


for i in range(1, limite + 1):
    produtorio = produtorio * i

print(f"Resultado do produtório: {produtorio}")

# Exercício 3
# Monte um programa que, parau um determinado número informado
# pelo usuário (limite), exiba o dobro da cada número de 1 até esse limiet.

limite = int(input("Informe o limite:  "))  

for i in range(1, limite + 1):
    print(f"Dobro de {i} é {2 * i}")


    