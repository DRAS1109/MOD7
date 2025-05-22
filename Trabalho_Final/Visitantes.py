"""
Modulo para gerir as visitas Guiadas ao museu
    - Adicionar mais pessoas a uma visita
        - Perguntar nº de pessoas, apresentar visitas com esses espaços disponiveis, escolher visita, pedir data, aumentar a lotação da visita e atribuir id do grupo

    - Retirar pessoas a uma visita (necessario identificaçao de id para ninguem cancelar a visita de outras pessoas)
        - Perguntar a data e o id da visita, perguntar se deseja cancelar a visita, cancelar, atualizar lotação da visita e eliminar id
"""
import Utils, Visitas
import os, csv
import datetime, random

NOME_FICHEIRO = "Datas.csv"

LVisitas = Visitas.Visitas
Datas = {}

#Adicionar Visitantes
def Adicionar_Visitantes():
    if Verificar() == True:
        return
    
    #Numero de Pessoas
    N_Pessoas = Utils.Ler_Inteiro_Limites(1, None, "Quantas pessoas são? ")

    #Data
    Horario = str(datetime.datetime.now()).split(" ")
    Horario = Horario[0].split("-")

    Max = 28
    if int(Horario[1]) in [1,3,5,7,8,10,12]:
        Max = 31
    
    elif int(Horario[1]) in [4,6,9,11]:
        Max = 30
        

    Dia = Utils.Ler_Inteiro_Limites(1,Max, "Dia da visita? ")
    Mes = Utils.Ler_Inteiro_Limites(int(Horario[1]),12, "Mês da visita? ")
    if int(Horario[1]) == Mes and int(Horario[2]) > Dia:
        print("Impossivel marcar visitas para o passado")
        return
    
    Ano = Horario[0]
    Data = f"{Ano}-{Mes}-{Dia}"

    #Listar todas com espaços livres para o nº de pessoas
    Visitas_Encontradas = []
    L_Visitas_Encontradas = []
    for Visita in LVisitas: #Ciclo para percorrer os horarios das visitas
        
        if Data in Datas:
            Lotacao = 0
            for Visita_Data, Ids in Datas[Data].items(): #Cliclo para percorrer as visitas de cada data
                if Visita["Visita"] == Visita_Data:
                    for Pessoas_Grupo in Ids.values():
                        Lotacao+=Pessoas_Grupo
                    break
            
            if Visita["Lotacao Maxima"] - Lotacao >= N_Pessoas:
                Visitas_Encontradas.append(Visita)
                L_Visitas_Encontradas.append(Visita["Visita"])
        
        else:
            Visitas_Encontradas.append(Visita)
            L_Visitas_Encontradas.append(Visita["Visita"])

    if len(Visitas_Encontradas) < 1:
        print("Não foram encontradas visitas disponiveis")
        return
    Visitas.Listar(Visitas_Encontradas)

    #Utilizador escolher qual visita
    Max = LVisitas[len(LVisitas) - 1]["Visita"] #N da ultima visita
    N_Visita = Utils.Ler_Inteiro_Limites(0, Max,f"Visita (Numero) ou 0 para cancelar: ")

    if N_Visita not in L_Visitas_Encontradas:
        if N_Visita != 0:
            print("Visita não corresponde às encontradas")
        return
    Visita = LVisitas[N_Visita - 1] #Dicionario da visita encontrada

    #Id
    Id_Random = random.randint(1, 1000)
    Tds_Id = set()
    for TempData in Datas.values():
        for TempVisita in TempData.values():
            for TempId in TempVisita.keys():
                Tds_Id.add(TempId)

    while True:
        Id_Random = random.randint(1, 1000)
        if Id_Random not in Tds_Id:
            break

    print(f"Visita: {Visita["Visita"]}, Horario: {Visita["Horario"]}, Id: {Id_Random}")

    if Data in Datas:
        if Visita["Visita"] in Datas[Data]:
            Datas[Data][Visita["Visita"]].update({Id_Random:N_Pessoas})

        else:
            Datas[Data].update({Visita["Visita"]:{Id_Random:N_Pessoas}})

    else:
        Datas.update({Data:{Visita["Visita"]:{Id_Random:N_Pessoas}}})

#Cancelar Visitas
def Cancelar_Visitantes():
    if Verificar() == True:
        return
    
    Id = Utils.Ler_Inteiro("Qual o id atribuido? ")

    for TempData, Resto in Datas.items():
        for TempVisita, TempGrupos in Resto.items():
            for TempId in TempGrupos.keys():
                if TempId == Id:
                    del Datas[TempData][TempVisita][Id]
                    print("Visita cancelada com sucesso")
                    return
    print("Erro")

#Listar 
def Listar(Titulo = "Lista de Visitantes"):
    """Função para listar os campos (Visita, Horario e Lotação maxima) de todas as Visitas"""
    if Verificar() == True:
        return
    
    #Imprimir Titulo
    Utils.F_Titulo(Titulo)

    #Imprimir os dados
    for Data, Visita in Datas.items():
        for Id_Visita, A in Visita.items():
            print(f"{Data} | Visita: {Id_Visita}")
            for Id, N_Pessoas in A.items():
                print(f"Id: {Id} Pessoas: {N_Pessoas}")
        print("")

#Função para remover visitas passadas
def Visitas_Anteriores():
    """Função para remover visitas guiadas anteriores"""
    if Verificar() == True:
        return
    
    #Data
    Horario = str(datetime.datetime.now()).split(" ")
    Horario = Horario[0].split("-")

    #Converter para inteiros
    Horario[0] = int(Horario[0])
    Horario[1] = int(Horario[1])
    Horario[2] = int(Horario[2])

    L_Datas_Remover = []
    for Data in Datas.keys():
            LData = Data.split("-")
            #Converter para inteiros
            LData[0] = int(LData[0])
            LData[1] = int(LData[1])
            LData[2] = int(LData[2])
            
            if LData < Horario:
                L_Datas_Remover.append(Data)

    for i in range(len(L_Datas_Remover)):
        del Datas[L_Datas_Remover[i]]

#Menu para Visitas Guiadas
def MenuVisitantes():
    """SubMenu para as visitas guiadas"""

    while True:
        Op = Utils.Menu(["Adicionar Visitantes", "Cancelar Visitas", "Listar visitantes", "Voltar"], "Menu das visitas guiadas")
        print("")

        if Op == 0:
            break

        elif Op == 1:
            Adicionar_Visitantes()

        elif Op == 2:
            Cancelar_Visitantes()
        
        elif Op == 3:
            Listar()
        
        Visitas_Anteriores()
        GuardarCSV()

#Verificar se a lista de visitas está vazia
def Verificar():
    #Verificar se existem visitas guiadas
    if len(LVisitas) == 0:
        print("Não existem visitas guiadas definidas")
        return True
    
#Configurar: Adiciona dados de teste
def Configurar():
    Teste = {"2025-05-30":{1:{1:8}}, 
             "2025-06-05":{2:{1:6,2:12,3:3}, 4:{1:6,2:12,3:3}}, 
             "2025-06-08":{3:{1:3,2:12}}}
    Datas.update(Teste)

#Guardar e ler os ficheiros binarios
def GuardarCSV():
    """Função para guardar os dados de Visitas num ficheiro binario"""
    if Verificar() == True:
        return
    
    with open(NOME_FICHEIRO, "w", encoding="utf-8", newline="") as Ficheiro:
        Chaves = ["Data", "Id_Visita", "Id_Grupo", "NPessoas"]

        #Variavel para gurdar no ficheiro(Ficheiro, Campos do Dicionario)
        Escrever = csv.DictWriter(Ficheiro, fieldnames=Chaves)

        #Gravar no cabeçalho
        Escrever.writeheader()
        for Data, Visitas in Datas.items():
            for Id_Visita, Grupos in Visitas.items():
                for Id_Grupo, NPessoas in Grupos.items():
                    Escrever.writerow({
                        "Data": Data,
                        "Id_Visita": Id_Visita,
                        "Id_Grupo": Id_Grupo,
                        "NPessoas": NPessoas})

def LerCSV():
    """Função para ler os dados de um ficheiro binario"""
    if os.path.exists(NOME_FICHEIRO) == False:
        return False

    Dados = {}
    with open(NOME_FICHEIRO, "r", newline="") as f:
        Ler = csv.DictReader(f)
        
        for Linha in Ler:
            Data = Linha["Data"]
            Id_Visita = int(Linha["Id_Visita"])
            Id_Grupo = int(Linha["Id_Grupo"])
            NPessoas = int(Linha["NPessoas"])
            
            if Data not in Dados:
                Dados[Data] = {}

            if Id_Visita not in Dados[Data]:
                Dados[Data][Id_Visita] = {}
            
            Dados[Data][Id_Visita][Id_Grupo] = NPessoas

            #Adicionar a Datas
            Datas.update(Dados)