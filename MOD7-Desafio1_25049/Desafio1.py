"""
Programa para gerir uma lista de tarefas utilizando ficheiros de texto para materialização dos dados
"""
import os
from datetime import datetime, timedelta

NOME_FICHEIRO = "Ficheiro.txt"
Lista = []

def Menu():
    Op = 0
    while Op != 7:
        Op = int(input("1. Adicionar \n2. Listar \n3. Listar Concluidas \n4. Listar Mes Atual \n5. Remover \n6. Concluida \n7. Sair \n"))

        if Op == 1:
            Adicionar()

        if Op == 2:
            Listar()

        if Op == 3:
            Listar_Concluidas()

        if Op == 4:
            Listar_Mes()

        if Op == 5:
            Remover()

        if Op == 6:
            Concluida()

def Adicionar():
    if Verificar() == False:
        Acao = "w"
    
    else:
        Acao = "a"

    while True:
        Descricao = input("Qual a descrição da tarefa? ")
        Descricao = Descricao.strip()

        Data = input("Qual a data da tarefa (dd/mm/aaaa)? ")
        Data = Data.strip()

        if Descricao != "" and len(Data) == 10:
            break

        else:
            print("Dados inválidos\n")

    with open(NOME_FICHEIRO, Acao, encoding="utf-8") as Ficheiro:
        Ficheiro.write(f"{Descricao} - {Data}\n")

    print("Tarefa adicionada com sucesso")

def Listar():
    Linhas = Ler()
    if Verificar() == False or len(Linhas) < 1:
        print("Ainda não tem tarefas")
        return
    
    print("Tarefas:")
    for i in range(len(Linhas)):
        print(f"{i+1}) {Linhas[i]}", end="")
    
    print("")

def Listar_Concluidas():
    Linhas = Ler()
    if Verificar() == False or len(Linhas) < 1:
        print("Ainda não tem tarefas")
        return
    
    print("Tarefas:")
    for i in range(len(Linhas)):
        if "[Concluida]" not in Linhas[i]:
            print(f"{i+1}) {Linhas[i]}", end="")
    print("")

def Listar_Mes():
    Data_Atual = datetime.now()
    Str_Data_Atual = str(Data_Atual)
    Data_Atual = Str_Data_Atual.split("-")

    Mes_Atual = Data_Atual[1]
    Ano_Atual = Data_Atual[0]


    #Verificação
    Linhas = Ler()
    if Verificar() == False or len(Linhas) < 1:
        print("Ainda não tem tarefas")
        return
    
    print("Tarefas:")
    for i in range(len(Linhas)):
        Linha = Linhas[i]
        Linha = Linha.split("/")
        Mes_Tarefa = Linha[1]
        Ano_Tarefa = Linha[2]
        Ano_Tarefa = Ano_Tarefa.replace("\n", "")

        if Mes_Tarefa == Mes_Atual and Ano_Tarefa == Ano_Atual:
            print(f"{i+1}) {Linhas[i]}", end="")
    print("")

def Remover():
    if Verificar() == False:
        return
    
    Linhas = Ler()
    Listar()

    #Identificar nº da tarefa a eliminar
    N_Remover = int(input("Qual o nº da data a remover? "))

    if len(Linhas) < N_Remover + 1:
        print("Tarefa não existe")
        return

    with open(NOME_FICHEIRO, "w", encoding="utf-8") as Ficheiro:
        #Escrever
        for i in range(len(Linhas)):
            if Linhas[i] != Linhas[N_Remover - 1]:
                Ficheiro.write(Linhas[i])

    print("Tarefa removida com sucesso! ")

def Concluida():
    if Verificar() == False:
        return
    
    Linhas = Ler()
    Listar()

    #Identificar nº da tarefa que foi concluida
    N_Concluida = int(input("Qual o nº da tarefa que concluiu? "))

    if len(Linhas) < N_Concluida:
        print("Tarefa não existe")
        return

    with open(NOME_FICHEIRO, "w", encoding="utf-8") as Ficheiro:
        #Escrever
        for i in range(len(Linhas)):
            if Linhas[i] == Linhas[N_Concluida - 1]:
                Ficheiro.write(f"[Concluida] {Linhas[i]}")

    print("Tarefa concluida com sucesso! ")

def Verificar():
    if os.path.exists(NOME_FICHEIRO) == False:
        return False
    return True

def Ler():
    with open(NOME_FICHEIRO, "r", encoding="utf-8") as Ficheiro:
        Linhas = Ficheiro.readlines()

    return Linhas

if __name__ == "__main__":
    Menu()