def produto (x, y):
    resultado = x * y
    return resultado

def soma (a, b):        # Testando mais de uma função no mesmo arquivo. 
    resultado = a + b
    return resultado


multiplicacao = produto(14, 7)
adicao = soma(60, 7)

print(f"Resultado de 14 x 7 = {multiplicacao}") 
print(f"Resultado de 60 + 7 = {adicao}")

diferenca = adicao - multiplicacao
print(f"Resultado de {adicao} - {multiplicacao} = {diferenca}")
