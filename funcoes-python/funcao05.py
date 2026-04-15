# variavel no escopo global. 
res = 100

def diferenca(x, y):
    res = x - y # variavel no escopo local. 
    return res # A palavra reservada return é usada para retornar um valor da função. O valor retornado pode ser armazenado em uma variável ou usado diretamente.

diferenca(10, 4)
print(res)