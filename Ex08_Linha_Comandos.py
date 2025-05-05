"""
Programa em python para adicionar palavras a um ficheiro
Quando o utilizador escrever uma linha em branco o programa termina
O utilizador escolhe o ficheiro:
py Linha_Comandos.py -l [NOME FICHEIRO] - abrir o ficheiro indicado ou o ficheiro predefinido e listar todo o seu conteúdo

py Linha_Comandos.py -a [NOME FICHEIRO] - adicionar ao ficheiro indicado ou ao ficheiro predefinido todas as linhas 
                                          que o utilizador escreve até introduzir uma linha em branco
"""
import sys #Para fornecer acesso aos parametros da linha de comandos
import os

NOME_FICHEIRO = "Linha_Comandos.txt"

def Ler():
    if os.path.exists(NOME_FICHEIRO) == False:
        print(f"Ficheiro {NOME_FICHEIRO} não existe")
        return
    
    #Abrir a leitura
    with open(NOME_FICHEIRO, "r", encoding="utf=8") as Ficheiro:
        Linhas = Ficheiro.readlines()
    
    for Linha in Linhas:
        print(Linha, end="")

#Abrir para adicionar:
def Adicionar():
    with open(NOME_FICHEIRO, "a", encoding="utf=8") as Ficheiro:
        while True:
            Frase = input(">").strip()

            #Se a frase está em branco terminar programa
            if not Frase:
                break
            Ficheiro.write(f"{Frase}\n")

def main():
    global NOME_FICHEIRO

    #Ler argumentos da linha de comandos
    if len(sys.argv) <= 1:
        print("Utilização: py Linha_Comandos.py -l | -a [NOME FICHEIRO]")
        return
    
    #Nome do ficheiro
    if len(sys.argv) == 3:
        NOME_FICHEIRO = sys.argv[2]

    #Opção
    Opcao = sys.argv[1]

    if Opcao.lower() == "-a":
        Adicionar()

    elif Opcao.lower() == "-l":
        Ler()

    else:
        print("Esta opção não existe")

if __name__ == "__main__":
    main()