"""
Programa para ler até ao final do ficheiro
"""
import os

NOME_FICHEIRO = "Geral.txt"

if os.path.exists(NOME_FICHEIRO) == False:
    print("O ficheiro não existe")

#Versão 1
with open("Geral.txt", "r", encoding="utf-8") as Ficheiro:
    Linhas = Ficheiro.readlines()

for Linha in Linhas:
    print(Linha, end="")

#Versão 2
with open("Geral.txt", "r", encoding="utf-8") as Ficheiro:
    while True:
        Linha = Ficheiro.readline()
        #Verificar se encontrou o fim do ficheiro:
        if not Linha:
            break
        print(Linha, end="")