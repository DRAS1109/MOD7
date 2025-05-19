"""Programa para ler um ficheiro com o módulo pickle"""

import pickle

#Lista Vazia
Lista = []

#Gravar no ficheiro serializando a lista de uma vez só
with open("Minha_Lista.pkl", "rb") as Ficheiro:
    Lista = pickle.load(Ficheiro)

print(Lista)