# Exercícios

# 01 - Crie uma lista com os números de 1 a 10 e use um loop para imprimir cada número elevado ao quadrado.

# numeros = list(range(1,11))

# for i in numeros:
#     print(i ** 2)


# # 03 Crie um dicionário para armazenar informações de um livro, incluindo título, autor e ano de publicação. Imprima cada informação
    

# informacoes_livro: dict = {
    
#     "titulo": "Nosso título", 
#     "Autor": "John Arias", 
#     "ano": "2023"
#     }

# # Abaixo mostro as formas de imprir o ítem como um todo (chave - valor) e como imprimir separadamente a chave e o valor

# for item in informacoes_livro.items():
#     print(f"{item}")

# # for chave, valor in informacoes_livro.items():
# #     print(f"{chave}: {valor}")




# # 05 Dada a lista ["maçã", "banana", "cereja"] e o dicionário {"maçã": 0.45, "banana": 0.30, "cereja": 0.65}, calcule o preço total da lista de compras.

# # lista01: list = ["maçã", "banana", "cereja"]

# # dicionario01: dict = {"maçã": 0.45, "banana": 0.30, "cereja": 0.65}

# # total = sum(dicionario01[item] for item in lista01)
# # print(f"Preço total: {total}")

# lista_compras = ["maçã", "banana", "cereja"]
# precos = {"maçã": 0.45, "banana": 0.30, "cereja": 0.65}

# total = sum(precos[item] for item in lista_compras)

# print(f"Preço total: {total}")