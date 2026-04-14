# Simulando um Caixa Eletrônico

# O usuário tem um saldo inicial de R$ 1000. 
# Ele pode escolher entre as seguintes opções:
# 1. Sacar o dinherio total ou 2. encerrar a operação.

saldo = 1000

while saldo > 0: 
   saque = float(input("Informe o valor do saque (ou digite 0 para sair):"))

   if saque == 0:
       break

   if  saque > saldo: 
       print("Saldo insuficiente. Tente um valor menor.") 
   else:
       saldo -= saque
       print(f"Saque efetuado! Novo saldo: R$ {saldo:.2f}")

print("Operação encerrada. Obrigado por usar nosso caixa eletrônico!")       
             
   
