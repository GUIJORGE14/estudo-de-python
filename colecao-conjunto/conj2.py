a = {1, 2, 3}
b = {3, 4, 2, 5}

print(a | b) # União dos conjuntos a e b, resultando em {1, 2, 3, 4, 5}, o elemento (|) combina os elementos de ambos os conjuntos, eliminando duplicatas. 
print(a & b) # Interseção dos conjuntos a e b, resultando em {3}, o elemento (&) retorna apenas os elementos que estão presentes em ambos os conjuntos. Elementos comuns.
print(a - b) # Diferença entre os conjuntos a e b, resultando em {1}, o elemento (-) retorna os elementos que estão presentes no conjunto a, mas não no conjunto b. Elementos exclusivos de cada conjunto.
print(a ^ b) # Diferença simétrica entre os conjuntos a e b, resultando em {1,4, 5}, o elemento (^) retorna os elementos que estão presentes em um dos conjuntos, mas não em ambos. Elementos exclusivos de cada conjunto.