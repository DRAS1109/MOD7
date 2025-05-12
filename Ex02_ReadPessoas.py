"""
Programa para ler todos os nomesdo ficheiro Geral
"""

with open("Geral.txt", "r", encoding="utf=8") as Ficheiro:
    Lista_Texto = Ficheiro.readlines()
    for Texto in Lista_Texto:
        print(Texto, end="")