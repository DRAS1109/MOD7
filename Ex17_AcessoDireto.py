"""
Programa para ler os dados de registo com base no nº do registo
Cada registo ocupa 28 bytes (20sif - nome idade saldo)
"""
import os
import struct

TAMANHO_REGISTO = 28

#calcular o tamanho do ficheiro
Tamanho_Ficheiro = os.path.getsize("Dados.bin")

#Calcular o nº de registos
N_Registos = Tamanho_Ficheiro / TAMANHO_REGISTO

N_a_Ler = int(input(f"Tem {N_Registos} \nQual o que pretende ler? "))


if N_a_Ler > N_Registos:
    print("Não existe esse registo")

else:
    #Abrir o ficheiro para leitura em modo binário
    with open("Dados.bin", "rb") as Ficheiro:
        #Posicionar o cursor no byte correspondente ao registo a ler
        Byte_Ler = (N_a_Ler-1) * TAMANHO_REGISTO
        Ficheiro.seek(Byte_Ler)

        #Ler o registo
        Dados_Binarios = Ficheiro.read(28)

        #Faz o desenpacotamento
        Dados = struct.unpack("20sif", Dados_Binarios)
        print(Dados[0].decode("utf-8").rstrip("\x00"))
        print(Dados[1])
        print(Dados[2])