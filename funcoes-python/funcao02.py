def produto (x, y):
    resultado = x * y
    return resultado # A palavra-chave return é usada para retornar um valor da função. Quando a função é chamada, ela executa o código dentro dela e retorna o valor especificado após a palavra-chave return. O valor retornado pode ser armazenado em uma variável ou usado diretamente em outras expressões.

multiplicacao1 = produto(14, 7)
multiplicacao2 = produto(6, 7)
multiplicacao3 = produto(4, 5)                    # Para chamar a função produto, é necessário definir os valores de x e y antes de chamar a função.
print(f"Resultado de 14 x 7 = {multiplicacao1}")  # Para que a funnção seja exibida no terminal é preciso armazenar o resultado da função em uma variável ou usar a função print para exibir o resultado diretamente.
print(f"Resultado de 6 x 7 = {multiplicacao2}")   # Já que a variável multiplicacao é igual a função produto, da hora de realizar o print, a variável multiplicacao pode ser substituida pela função produto. O resultado será o mesmo.
print(f"Resultado de 4 x 5 = {multiplicacao3}")   # Já que a variável multiplicacao é igual a função produto, da hora de realizar o print, a variável multiplicacao pode ser substituida pela função produto. O resultado será o mesmo.