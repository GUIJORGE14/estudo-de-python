# Variavel no escopo global.
meu_nome = "Guilherme"

def exibir_nome():
    # Espaço do escopo local
    print(f"Seu nome é {meu_nome}.")

exibir_nome()

# Escopo global NÂO enxerga o que está no escopo local.
# Escopo local ENXERGA o que está no escopo global.