# # Type Hint

# # Ajuda a tornar o código mais legível e seguro especificando o tipo de dados esperados por funções e variáveis.

# idade = "30"
# altura = 1.75
# nome = "Alice"
# is_estudante = True

# print(type(altura))

# idade: int = 30
# altura: float = 1.75
# nome: string = "Alice"
# is_estudante: bool = true


# Listas x dicionários

# Listas e dicionários são estruturas de dados versáteis que permitem armazenar e manipular coleções de dados de forma eficiente. Na engenharia de dados, essas estruturas são fundamentais para organizar dados coletados de diversas fontes, facilitando operações como filtragem, busca, agregação e transformação de dados.

# Exercícios

# 01 - Crie uma lista com os números de 1 a 10 e use um loop para imprimir cada número elevado ao quadrado.

numeros = list(range(1,11))

for i in numeros:
    print(i ** 2)