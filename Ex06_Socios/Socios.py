"""Programa para identificar e mostrar os nomes das pessoas que estão em ambos os ficheiros (Academico.txt e Tondela.txt)"""
import os

def Socios():
    if os.path.exists("Tondela.txt") == False or os.path.exists("Academico.txt") == False:
        print("Os ficheiros não existem")
        return

    with open("Tondela.txt", "r", encoding="utf-8") as Tondela:
        Tondela_Linhas = Tondela.readlines()

    with open("Academico.txt", "r", encoding="utf-8") as Academico:
        Academico_Linhas = Academico.readlines()
    
    print("Traidores:")
    for Socio in Tondela_Linhas:
        if Socio in Academico_Linhas:
            print(Socio.strip())

Socios()