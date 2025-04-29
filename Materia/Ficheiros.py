"""
Ficheiros
R  - Leitura
W  - Escrever (Destroi tudo do ficheiro caso exista)
A  - Escrever (No final do ficheiro)
R+ - Leitura / Escrita
W+ - Leitura / Escrita (Cria ficheiro)
A+ - Leitura / Escrita (No final)
"""

def Criar():
    Ficheiro = open("Alunos.txt", "w", encoding="utf=8") #Cria o ficheiro Alunos.txt

    Ficheiro.write("Ola Mundo\n")
    Ficheiro.write("Olá Mundo 2")
    Ficheiro.write("Fim")

    Ficheiro.close()

def Ler():
    Ficheiro = open("Alunos.txt", "r", encoding="utf=8")

    Texto = Ficheiro.readline()
    print(Texto)

    Ficheiro.close()

def Close_Automatico():
    with open("Alunos.txt", "r", encoding="utf=8") as Ficheiro:
        Texto = Ficheiro.readline()
        print(Texto)

def Seek_Como_Utilizar():
    with open("Alunos.txt", "r", encoding="utf=8") as F:
        Texto = F.readline()
        print(Texto)
        F.seek(0)
        Texto = F.readline()
        print(Texto)