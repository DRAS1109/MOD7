"""Programa para ler um ficheiro com o módulo pickle e mostrar todos os daados"""

import pickle

Lista = []

#Gravar num ficheiro
with open("So_Um.dat", "rb") as Ficheiro:
    while True:
        try:
            Dados = pickle.load(Ficheiro)
            print(Dados)
            Lista.append(Dados)

        except EOFError:
            break