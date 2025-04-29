"""
Programa para adicionar o nome de um produto e o preço
"""
NOME_FICHEIRO = "Geral.txt"

Tamanho = int(input("Quantos produtos são? "))

with open(NOME_FICHEIRO, "w", encoding="utf=8") as Ficheiro:
    Ficheiro.write("Nº- Produtos: Preco\n")
    for i in range (Tamanho):
        Nome  = input(f"Nome do {i + 1}ª Produto: ").strip().capitalize()
        Preco = float(input(f"Preço do {i + 1}ª Produto: "))
        print("")
        Ficheiro.write(f"{i+1}- {Nome}: {Preco}")
        if i != Tamanho-1:
            Ficheiro.write("\n")