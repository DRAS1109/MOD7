"""Programa para gravar um dicionario com o módulo pickle"""

import pickle

#Lista
Registo = [1,2,True,"Quatro", {"Numero": "Cinco"}, [6,7]]

#Gravar no ficheiro serializando a lista de uma vez só
with open("Minha_Lista.pkl", "wb") as Ficheiro:
    pickle.dump(Registo, Ficheiro)

print("Dados adicionados com sucesso")