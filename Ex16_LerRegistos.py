"""
Programa para ler vários registos do ficheiro.
Cada registo tem 28 bytes (20sif -> nome, idade, saldo)
"""

import struct

#Adicionar ao ficheiro
with open("Dados.bin", "rb") as Ficheiro:
    while True:
        try:
            #Ler os dados todos de uma vez só
            Dados_Binarios = Ficheiro.read(28)
            if not Dados_Binarios:
                break
            Dados = struct.unpack("20sif", Dados_Binarios)

            #Converter a string binária numa string
            Nome = Dados[0].decode("utf-8").rstrip("\x00")
            print("Nome: " , Nome)
            print("Idade: ", Dados[1])
            print("Saldo: ", Dados[2])
        
        except EOFError:
            break