"""Programa para gravar um dicionario com o módulo pickle"""

import pickle

#Ler dados
Nome  = input("Nome? " )
Idade = input("Idade? ")
Email = input("Email? ")

#Criar dicionario
Registo = {"Nome" : Nome,
           "Idade": Idade,
           "Email": Email}

#Gravar num ficheiro
with open("So_Um.dat", "ab") as Ficheiro:
    #Serialização
    pickle.dump(Registo, Ficheiro)

print("Dados adicionados com sucesso")