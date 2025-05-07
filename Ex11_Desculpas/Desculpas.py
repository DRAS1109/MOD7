"""
Programa para formar uma desculpa.
Nome dos ficheiros:
intro.txt
culpado.txt
desculpa.txt
"""
import os, sys, random

INTRO = "intro.txt"
CULPADO = "culpado.txt"
DESCULPA = "desculpa.txt"



def Parte_Desculpa(Nome_Ficheiro):
    """Recebe o nome do ficheiro e devolve uma parte da desculpa"""
    if os.path.exists(Nome_Ficheiro) == False:
        print(f"Falta o ficheiro: {Nome_Ficheiro}")

    with open(Nome_Ficheiro, "r", encoding="utf-8") as Ficheiro:
        Lista = Ficheiro.readlines()

    Aleatorio = random.choice(Lista)
    Aleatorio = Aleatorio.replace("\n" , "")
    return Aleatorio

print(f"{Parte_Desculpa(INTRO)} {Parte_Desculpa(CULPADO)} {Parte_Desculpa(DESCULPA)}.")