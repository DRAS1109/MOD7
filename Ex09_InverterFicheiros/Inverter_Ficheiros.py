"""
Programa para inverter as linhas de um ficheiro
"""
import sys #Para fornecer acesso aos parametros da linha de comandos
import os


def Trocar():
    #Verificar se o ficheiro existe
    if Ficheiro_Existe() == False:
        return

    #Abrir o ficheiro para ler
    Ficheiro_Ler      = open(NOME_FICHEIRO, "r", encoding="utf-8")

    #Abrir ficheiro temporario para escrever
    Ficheiro_Escrever = open("Temp.txt", "w", encoding="utf-8")

    Linhas = Ficheiro_Ler.readlines()

    for i in range(len(Linhas) -1, -1, -1):
        Ficheiro_Escrever.write(Linhas[i])

    #Fechar os 2 ficheiros
    Ficheiro_Escrever.close()
    Ficheiro_Ler.close()

    #Apagar o ficheiro
    os.remove(NOME_FICHEIRO)

    #Mudar o nome do ficheiro temporario para produtos
    os.rename("Temp.txt", NOME_FICHEIRO)
    print("Ordem trocada com sucesso! ")

def Ficheiro_Existe():
    if os.path.exists(NOME_FICHEIRO) == False:
        print(f"O ficheiro {NOME_FICHEIRO} não existe")
        return False
    
def main():
    global NOME_FICHEIRO

    #Ler argumentos da linha de comandos
    if len(sys.argv) <= 1:
        print("Utilização: py Linha_Comandos.py [NOME FICHEIRO]")
        return
    
    #Nome do ficheiro
    if len(sys.argv) == 2:
        NOME_FICHEIRO = sys.argv[1]

    Trocar()

if __name__ == "__main__":
    main()