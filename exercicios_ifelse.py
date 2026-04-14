# Exercicio 1
# Peça ao usuário para digitar a temperatura atual em Celsius
# Se for maior ou igual a 30, exiba "hoje está muito quente!". 
# Se estiver acima ou igual a 20 e abaixo de 30, exiba "hoje está agradável".
# Se estiver abaixo de 20, exiba "hoje está frio!".

temp = int(input("Informe a temperatura: "))

if temp >= 30:
    print("Hoje está muito quente!")
elif (temp >= 20) and (temp < 30):
    print("Hoje está agradável.")
else: 
    print("Hoje está frio!")  

# Exercício 2
# Peça ao usuário para digitar a idade de uma pessoa.
# Com base nessa idade, informe o valor da tarifa de transporte
# que terá que ser paga. Se a idade for menosr que 6 anos, a tarifa é gratuita.
# Se a idade for entre 6 e 18 anos, a tarifa é de R$ 10,00. 
# Se a idade for entre 19 e 60 anos, a tarifa é de R$ 20,00. 
# Se a idade for acima de 60 anos, a tarifa é também gratuita.

idade = int(input("Informe sua idade: "))
if idade < 6:
    tarifa = 0.00
elif (idade >= 6) and (idade <= 18):
    tarifa = 10.00
elif (idade > 18) and (idade <=60):
    tarifa = 20.00
else:
    tarifa = 0.00

print(f"A tarifa é de R$ {tarifa:.2f}")

# Exercício 3
# Peça ao usuário para digitar um username
# e uma senha. Considere que o usúario correto é 
# "admin" e a senha correta é "1234". Se as credenciais
# estiverem corretas, exiba "Acesso concedido". Do contrário,
# exiba que as credenciais estão incorretas.

username_correto = "admin"
senha_correta = "1234"

username_entrada = input("Digite o username: ")
senha_entrada = int(input("Digite a senha: "))



if (username_entrada == username_correto) and (senha_entrada == senha_correta):
    print("Acesso concedido!")
else: 
    print("Credenciais incorretas!")        
