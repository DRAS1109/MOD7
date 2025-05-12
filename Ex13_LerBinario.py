"""Ler um numero inteiro de ficheiro binário"""
import struct

with open("int.dat", "rb") as Ficheiro:
    Numero = struct.unpack("i", Ficheiro.read(4))

print(Numero)       #Mostra um tuple (12345,)
print(Numero[0])    #Mostra 12345