"""
Modulo para gerir as visitas Guiadas ao museu
- Horários de visitas
    - Adicionar
    - Editar
    - Apagar
"""
import Utils
import os, struct

NOME_FICHEIRO = "Visitas.bin"
Formato = "i5si"

Visitas = []

import Visitantes
Visitantes.LerCSV()

#Adicionar Horario
def Adicionar():
    Utils.F_Titulo("Adicionar novo horario de visita")

    #Horario
    Horario = Utils.Ler_Inteiro_Limites(0,23, "Inicio da Visita (em horas): ")
    Duracao = 2 #Numa variavel caso seja necessario trocar
    
    if (Horario + Duracao) > 23:
        Horario = f"{Horario}-{(Horario + Duracao) - 24}"
    
    else:
        Horario = f"{Horario}-{Horario + Duracao}"

    #Verificar se o horario é valido
    Horarios_Visitas = set()
    for Visita in Visitas:
        Horarios_Visitas.add(Visita["Horario"])

    if Horario in Horarios_Visitas: #Verificar se ja existe alguma visita guiada para aquele horario
        print("Já tem uma visita guiada para este horário")
        return

    #Lotacao Maxima
    Lotacao_Maxima = Utils.Ler_Inteiro_Limites(3, 100, "Qual a lotação máxima? ")

    #Numero da visita (id)
    NVisita = 1
    if len(Visitas) > 0:
        NVisita = Visitas[len(Visitas) - 1]["Visita"] + 1 #Gera o numero da visita a partir do nº da ultima

    Nova_Visita ={"Visita": NVisita,
                "Horario": Horario,
                "Lotacao": 0, 
                "Lotacao Maxima": Lotacao_Maxima,
                "Id": {}}
    
    Visitas.append(Nova_Visita)
    print(f"Visita adicionada com sucesso. \n")

#Editar Horarios
def Editar():
    if Verificar() == True:
        return
    
    #Mostrar as visitas
    Listar()

    #Utilizador escolher a visita a editar
    Max = len(Visitas)
    N_Visita = Utils.Ler_Inteiro_Limites(0, Max,f"Visita a editar (Numero) ou 0 (Cancelar): ")

    if N_Visita == 0:
        return
    
    for Data in Visitantes.Datas.values():
        if N_Visita in Data:
            print("Não é possivel editar a visita porque tem vitantes agendados!")
            return

    Visita_Encontrada = Visitas[N_Visita - 1] #Dicionario da visita encontrada

    #Lista com os campos que pode editar editar
    Lista_Campos = ["Horario", "Lotacao Maxima"]

    #Escolher o campo a editar
    Op = Utils.Menu(Lista_Campos, "Qual o campo a editar? ")
    Campo = Lista_Campos[Op - 1]

    #Se o campo a editar for Horario
    if Campo == Lista_Campos[0]:
        Horario = Utils.Ler_Inteiro_Limites(0,23, "Inicio da Visita: ")
        Duracao = Utils.Ler_Inteiro_Limites(1,8, "Duração da Visita (em Horas): ")
        
        if (Horario + Duracao) > 23:
            Horario = f"{Horario}-{(Horario + Duracao) - 24}"
        
        else:
            Horario = f"{Horario}-{Horario + Duracao}"

        #Verificar se o horario é valido
        Horarios_Visitas = set()
        for Visita in Visitas:
            Horarios_Visitas.add(Visita["Horario"])

        if Horario in Horarios_Visitas: #Verificar se ja existe alguma visita guiada para aquele horario
            print("Já tem uma visita guiada para este horário")
            return

        Novo_Valor = Horario #O codigo ficaria confuso com o nome da variavel a Novo_Valor

    #Se o campo a editar for Lotação maxima
    if Campo == Lista_Campos[1]:
        Novo_Valor = Utils.Ler_Inteiro_Limites(1, None, "Qual a lotação máxima? ")

    #Guardar o novo valor:
    Visita_Encontrada[Campo] = Novo_Valor
    print("Edição concluida com sucesso.")

#Apagar
def Apagar():
    if Verificar() == True:
        return

    #Mostrar as visitas
    Listar()

    #Utilizador escolher 
    Max = len(Visitas)
    N_Visita = Utils.Ler_Inteiro_Limites(0, Max,f"Visita a apagar (Numero) ou 0  para cancelar: ")

    if N_Visita == 0:
        return
    
    for Data in Visitantes.Datas.values():
        if N_Visita in Data:
            print("Não é possivel remover a visita porque tem vitantes agendados!")
            return
        
    Visita_Encontrada = Visitas[N_Visita - 1] #Dicionario da visita encontrada
    Visitas.remove(Visita_Encontrada)
    print(f"Visita removida com sucesso")

    for N in range(N_Visita-1, Max-1):
        Visitas[N]["Visita"] -= 1

#Listar 
def Listar(Visitas = Visitas, Titulo = "Lista de Visitas"):
    """Função para listar os campos (Visita, Horario e Lotação maxima) de todas as Visitas"""
    if Verificar() == True:
        return
    
    #Dicionario para guardar os campos e o comprimento da maior palavra de cada campo
    Campos = {"Visita": 0, "Horario": 0,"Lotacao Maxima": 0}
    
    #Determinar a maior palavra de cada campo
    for Visita in Visitas:
        for Campo in Campos:
            if len(str(Visita[Campo])) > Campos[Campo]:
                Campos[Campo] = len(str(Visita[Campo])) #Guardar o tamanho da maior palavra de cada campo

    #Descobrir o tamanho da linha --------------
    Tamanho = 0
    for Campo in Campos:
        Tamanho += Campos[Campo] + len(Campo)

    #Adicionar à variavel tamanho os "extras" (espaços, : e |)
    Extras = (len(Campos) *2) + (len(Campos) *3) + 1 # Espaços, : e | + 1 para o primeiro e último |
    Tamanho += Extras  
    
    #Imprimir Titulo
    Utils.F_Titulo(Titulo)

    #Imprimir os dados
    print("-" * Tamanho)
    for Visita in Visitas:
        Linha = ""
        for Campo in Campos:
            CampoTexto = f"{Campo}: {Visita[Campo]}"
            Espacos = " " * (Campos[Campo] - len(str(Visita[Campo])))
            Linha += f"| {CampoTexto}{Espacos} "
        Linha += "|"
        print(Linha)
        print("-" * Tamanho)

#Menu para Horarios
def MenuVisitas():
    """SubMenu para os horarios das visitas"""

    while True:
        Op = Utils.Menu(["Adicionar", "Editar", "Apagar", "Listar", "Voltar"], "Menu dos horarios")
        print("")

        if Op == 0:
            break

        elif Op == 1:
            Adicionar()
            GuardarBinario()
            
        elif Op == 2:
            Editar()
            GuardarBinario()
        
        elif Op == 3:
            Apagar()
            GuardarBinario()
        
        elif Op == 4:
            Listar()

#Verificar se a lista de visitas está vazia
def Verificar():
    #Verificar se existem visitas guiadas
    if len(Visitas) == 0:
        print("Não existem visitas guiadas definidas")
        return True
    
#Configurar: Adiciona dados de teste
def Configurar():
    Visitas.append({"Visita": 1, "Horario": "9-10" , "Lotacao Maxima": 30})
    Visitas.append({"Visita": 2, "Horario": "11-12", "Lotacao Maxima": 30})
    Visitas.append({"Visita": 3, "Horario": "17-18", "Lotacao Maxima": 30})

#Guardar e ler os ficheiros binarios
def GuardarBinario():
    """Função para guardar os dados de Visitas num ficheiro binario""" 
    with open(NOME_FICHEIRO, "wb") as Ficheiro:
        for Visita in Visitas:
            NVisita        = Visita["Visita"] #Inteiro
            Horario        = Visita["Horario"] #String 5 caracteres
            Lotacao_Maxima = Visita["Lotacao Maxima"] #Inteiro

            #Adicionar ao ficheiro
            Dados_Empacotados = struct.pack(Formato,
                                            NVisita,
                                            Horario.encode("utf-8"),
                                            Lotacao_Maxima)
                                           
            Ficheiro.write(Dados_Empacotados)

def LerBinario():
    """Função para ler os dados de um ficheiro binario"""
    if os.path.exists(NOME_FICHEIRO) == False:
        return
    
    global Visitas
    Visitas.clear()

    with open(NOME_FICHEIRO, "rb") as Ficheiro:
        while True:
            try:
                #Ler os dados todos de uma vez só
                Dados_Binarios = Ficheiro.read(16)
                if not Dados_Binarios:
                    break

                #Converter os dados
                Dados = struct.unpack(Formato, Dados_Binarios)

                #Adicionar os dados
                Visita = {"Visita":         Dados[0], 
                          "Horario":        Dados[1].decode("utf-8").rstrip("\x00"),
                          "Lotacao Maxima": Dados[2]}

                #Adicionar as obras
                Visitas.append(Visita)

            except EOFError:
                break