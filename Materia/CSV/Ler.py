import csv

#Lista vazia para guardar os dados do ficheiro
Dados = []

#Abrir ficheiro para leitura
with open("Ficheiro.csv", "r", encoding="utf-8") as Ficheiro:
    #Criar o objeto para ler o csv
    Ler = csv.DictReader(Ficheiro)

    #Ler cada linha do ficheiro e adicionar à lista
    for Linha in Ler:
        Dados.append(Linha)

print(Dados)