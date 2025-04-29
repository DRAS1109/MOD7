"""
Programa para ler o nome de 9 pessoas e guarda o nome em um ficheiro
"""

with open("Geral.txt", "w", encoding="utf=8") as Ficheiro:
    Ficheiro.write("Nomes:\n")
    for i in range (9):
        Nome = input(f"{i + 1}ª Nome: ").strip().capitalize()
        Ficheiro.write(f"{i+1} - {Nome}")
        if i != 8:
            Ficheiro.write("\n")