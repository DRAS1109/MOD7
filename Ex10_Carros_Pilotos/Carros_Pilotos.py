"""
Programa para gravar e ler dados em ficheiros csv para carros e pilotos de corridas.
Carros.csv : marca, modelo, matricula
Pilotos.csv: Nome, Idade, Pais

Funcionalidades:
    Adiconar : carros, pilotos
    Listas   : carros, pilotos
    Pesquidar: Pilotos de um carro, carro de um piloto
"""
import csv, os

FICHEIRO_PILOTOS = "Pilotos.csv"
FICHEIRO_CARROS  = "Carros.csv"

Lista_Pilotos = []
Lista_Carros  = []

def Menu():
    global Lista_Pilotos, Lista_Carros
    Lista_Pilotos = LerFicheiro(FICHEIRO_PILOTOS)
    Lista_Carros  = LerFicheiro(FICHEIRO_CARROS)

    Op = 0
    while Op != 4:
        Op = int(input("1. Adicionar \n2. Listar \n3. Pesquisar \n4. Sair \n"))

        if Op == 1:
            Adicionar()

        if Op == 2:
            Listar()

        if Op == 3:
            Pesquisar()

def Escrever(Lista, Nome_Ficheiro):
    """Função para escrever os dados de uma lista num ficheiro csv"""

    #Cabeçalho do ficheiro csv
    Chaves = Lista[0].keys()

    with open(Nome_Ficheiro, "w", encoding="utf-8", newline="") as Ficheiro:
        #Variavel para gurdar no ficheiro(Ficheiro, Campos do Dicionario)
        Escrever = csv.DictWriter(Ficheiro, fieldnames=Chaves)

        #Gravar no cabeçalho
        Escrever.writeheader()
        for i in range(len(Lista)):
            Escrever.writerow(Lista[i]) #Grava os dados correspondentes às chaves

def LerFicheiro(Nome_Ficheiro):
    """Função para ler ficheiro csv e devolver lista com dados"""
    #Lista vazia para guardar os dados do ficheiro
    Dados = []

    #Verificar se existe
    if os.path.exists(Nome_Ficheiro) == False:
        return Dados
    
    #Abrir ficheiro para leitura
    with open(Nome_Ficheiro, "r", encoding="utf-8") as Ficheiro:
        #Criar o objeto para ler o csv
        Ler = csv.DictReader(Ficheiro)

        #Ler cada linha do ficheiro e adicionar à lista
        for Linha in Ler:
            Dados.append(Linha)

    return Dados

def Adicionar():
    Op = input("Adicionar [P]iloto ou [C]arro? ")

    if Op in "cC":
        #Ler os dados do carro
        Matricula = input("Qual a matricula do carro? ")
        if ValidarMatricula(Matricula) == True:
            print("Erro! Essa matricula já existe")
            return
        
        Marca  = input("Qual a marca do carro? ")
        Modelo = input("Qual o modelo do carro? ")

        #Criar um dicionario
        Dicionario = {"Marca": Marca, "Modelo": Modelo, "Matricula": Matricula}

        #Adicionar à lista
        Lista_Carros.append(Dicionario)

        #Escrever no Ficheiro dos carros
        Escrever(Lista_Carros, FICHEIRO_CARROS)
        print("Carro adicionado com susesso! ")

    if Op in "pP":
        #Ler os dados do carro
        Matricula = input("Qual a matricula do veículo? ")
        if ValidarMatricula(Matricula) == False:
            print("Erro! Essa matricula não existe na base de dados")
            return
        
        if ValidarNrMatriculas(Matricula) >= 2:
            print("Já existem 2 pilotos no carro")
            return
        
        Nome  = input("Qual a nome do piloto? ")
        Idade = input("Qual o idade do piloto? ")
        Pais  = input("Qual a país do piloto? ")


        #Criar um dicionario
        Dicionario = {"Nome": Nome, "Idade": Idade, "Pais": Pais, "Matricula": Matricula}

        #Adicionar à lista
        Lista_Pilotos.append(Dicionario)

        #Escrever no Ficheiro dos pilotos
        Escrever(Lista_Pilotos, FICHEIRO_PILOTOS)
        print("Piloto adicionado com susesso! ")

def Listar():
    Op = input("Listar [P]iloto ou [C]arro? ")
    if Op in "cC":
        print(Lista_Carros)
    
    if Op in "pP":
        print(Lista_Pilotos)

def Pesquisar():
    pass

def ValidarMatricula(Matricula):
    """Devolve True se a matricula existir, False se não existir"""
    for Carro in Lista_Carros:
        if Carro["Matricula"] == Matricula:
            return True
    return False

def ValidarNrMatriculas(Matricula):
    """Devolve nº de pilotos de um carro"""
    Contar = 0
    for p in Lista_Pilotos:
        if p["Matricula"] == Matricula:
            Contar += 1

    return Contar

if __name__ == "__main__":
    Menu()