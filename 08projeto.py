# Jogo de adivinhação

# No jogo, o usuário deve adivinhar o número secreto.
# Ele pode tentar várias vezes até acertar o número.

numero_secreto =  14
tentativa = 0

while tentativa != numero_secreto:
  tentativa = int(input("Tenta adivinhar um número entre 1 e 20: "))

  if tentativa < numero_secreto:
      print("O número secreto é maior")
  elif tentativa > numero_secreto: 
      print("O número secreto é menor")  
  else: 
      print("Parabéns! Você acertou o número secreto!")  
  
