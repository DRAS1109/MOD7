"""Guardar num ficheiro binário os dados de um cliente: nome, idade e saldo
Destroi e escreve"""

import struct

#Ler os dados
Nome = input("Qual o nome? ")
Idade = int(input("Indique a idade: "))
Saldo = float(input("Qual o saldo: "))

#Adicionar ao ficheiro
with open("Dados.bin", "wb") as Ficheiro:
    #Nome -> String -> cada letra 1 byte -> 20 bytes 
    Dados_Empacotados = struct.pack("20s", Nome.encode("utf-8"))
    Ficheiro.write(Dados_Empacotados)

    #Idade -> int -> 4 bytes
    Dados_Empacotados = struct.pack("i", Idade)
    Ficheiro.write(Dados_Empacotados)

    #Saldo -> float -> 4 bytes
    Dados_Empacotados = struct.pack("f", Saldo)
    Ficheiro.write(Dados_Empacotados)

print("Dados guardados com sucesso")