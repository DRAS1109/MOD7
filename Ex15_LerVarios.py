"""
Ler os dados de um ficheiro binário os dados de um cliente: nome, idade e saldo
Nome  -> String -> 20 bytes 
Idade -> int    -> 4  bytes
Saldo -> float  -> 4  bytes
"""

import struct

#Adicionar ao ficheiro
with open("Dados.bin", "rb") as Ficheiro:
    #Ler os dados todos de uma vez só
    Dados_Binarios = Ficheiro.read(28)
    Dados = struct.unpack("20sif", Dados_Binarios)

#Converter a string binária numa string
Nome = Dados[0].decode("utf-8").rstrip("\x00")
print(Dados)
print("Nome: " , Nome)
print("Idade: ", Dados[1])
print("Saldo: ", Dados[2])