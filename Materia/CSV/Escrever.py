Lista = [{"Nome": "Joaquim", "Morada": "Viseu", "Idade": 30},
         {"Nome": "Maria"  , "Morada": "Sátão", "Idade": 24}   ]

#Ler e escrever em ficheiros com formato csv
import csv

#Cabeçalho do ficheiro csv
Chaves = Lista[0].keys()

with open("Ficheiro.csv", "w", encoding="utf-8", newline="") as Ficheiro:
    #Variavel para gurdar no ficheiro(Ficheiro, Campos do Dicionario)
    Escrever = csv.DictWriter(Ficheiro, fieldnames=Chaves)

    #Gravar no cabeçalho
    Escrever.writeheader()
    for i in range(len(Lista)):
        Escrever.writerow(Lista[i]) #Grava os dados correspondentes às chaves

print("Ficheiro criado com sucesso")