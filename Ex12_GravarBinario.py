"""Programa para gravar um nº inteiro num fiheiro binário"""
import struct

Numero = 12345

#gravar o nº no ficheiro 
with open("int.dat", "wb") as Ficheiro:
    #empacotar o numero no formato inteiro e escrever no ficheiro
    Ficheiro.write(struct.pack("i", Numero))

print("Inteiro gravado com sucesso")