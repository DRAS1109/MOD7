"""
Modulo para gerir as visitas Guiadas ao museu
- Horários de visitas
    - Pre-definidos
    - Adicionar
    - Editar
    - Apagar

-Visitas
    - Adicionar mais pessoas a uma visita
        - Perguntar nº de pessoas, apresentar visitas com esses espaços disponiveis, escolher visita, aumentar a lotação da visita e atribuir id do grupo

    - Retirar pessoas a uma visita (necessario identificaçao de id para ninguem cancelar a visita de outras pessoas)
        - Perguntar o id da visita, perguntar se deseja cancelar a visita, cancelar, atualizar lotação da visita e eliminar id

    - Listar (Visita 9-10: 30 pessoas | Visita 11-12: 27 pessoas)
"""
import Utils
import os, struct

NOME_FICHEIRO = "Visitas.bin"
Formato = "i5sii120s"

Visitas = []

#Dicionario para guardar os campos e o comprimento da maior palavra de cada campo
Campos = {"Visita": 0, "Horario": 0, "Lotacao": 0,"Lotacao Maxima": 0}

#Adicionar Horario
def Adicionar_Horario():
    Utils.F_Titulo("Adicionar novo horario de visita")

    #Horario
    Horario = Utils.Ler_Strings(2, "Qual o horario (Exemplo: 8-9): ")
    Horario = Horario.strip()

    #Verificar se o horario é valido
    Horarios_Visitas = set()
    for Visita in Visitas:
        Horarios_Visitas.add(Visita["Horario"])

    L_Horario = Horario.split("-")

    if len(L_Horario) != 2:
        print("Horario inválido. Deve ter o seguinte formato: X-Y")
        return
    
    if L_Horario[0].isdigit() and L_Horario[1].isdigit():
        L_Horario[0] = int(L_Horario[0])
        L_Horario[1] = int(L_Horario[1])

        if (L_Horario[0] < 0 or L_Horario[0] > 23) or (L_Horario[1] < 0 or L_Horario[1] > 23):
            print("Horario inválido. Deve ser composto por numeros entre 0 e 23")
            return

        if Horario in Horarios_Visitas: #Verificar se ja existe alguma visita guiada para aquele horario
            print("Já tem uma visita guiada para este horário")
            return
    else:
        print("Horario inválido. Deve ser composto por digitos separados por -")
        return

    #Lotacao Maxima
    Lotacao_Maxima = Utils.Ler_Inteiro_Limites(1, None, "Qual a lotação máxima? ")

    #Numero da visita (id)
    NVisita = 1
    if len(Visitas) > 0:
        NVisita = Visitas[len(Visitas) - 1]["Visita"] + 1 #Gera o numero da visita a partir do nº da ultima

    Nova_Obra ={"Visita": NVisita,
                "Horario": Horario,
                "Lotacao": 0, 
                "Lotacao Maxima": Lotacao_Maxima,
                "Id": {}}
    
    Visitas.append(Nova_Obra)
    print(f"Visita adicionada com sucesso. \n")

    #Verificar se o tamanho dos campos Visita, Horario, Lotacao Maxima é maior do que os anteriores
    if len(str(NVisita)) > Campos["Visita"]:
        Campos["Visita"] = len(str(NVisita))
    
    if len(Horario) > Campos["Horario"]:
        Campos["Horario"] = len(Horario)

    if len(str(Lotacao_Maxima)) > Campos["Lotacao Maxima"]:
        Campos["Lotacao Maxima"] = len(str(Lotacao_Maxima))

#Editar Horarios
def Editar():
    if Verificar() == True:
        return
    
    #Mostrar as visitas
    Listar(Visitas)
    #print("")

    #Utilizador escolher a visita a editar
    Max = len(Visitas)
    N_Visita = Utils.Ler_Inteiro_Limites(0, Max,f"Visita a editar (Numero) ou 0 (Cancelar): ")

    if N_Visita == 0:
        return

    Visita_Encontrada = Visitas[N_Visita - 1] #Dicionario da visita encontrada

    #Lista com os campos que pode editar editar
    Lista_Campos = ["Horario", "Lotacao Maxima"]

    #Escolher o campo a editar
    Op = Utils.Menu(Lista_Campos, "Qual o campo a editar? ")
    Campo = Lista_Campos[Op - 1]

    #Se o campo a editar for Horario
    if Campo == Lista_Campos[0]:
        Horarios_Visitas = []
        for Visita in Visitas:
            Horarios_Visitas.append(Visita["Horario"])

        Horario = Utils.Ler_Strings(3, "Qual o horario (Exemplo: 8-9): ")
        Horario = Horario.strip()

        #Verificar se o horario é válido
        L_Horario = Horario.split("-")

        if len(L_Horario) != 2:
            print("Horario inválido. Deve ter o seguinte formato: X-Y")
            return
    
        if L_Horario[0].isdigit() and L_Horario[1].isdigit():
            L_Horario[0] = int(L_Horario[0])
            L_Horario[1] = int(L_Horario[1])

            if (L_Horario[0] < 0 or L_Horario[0] > 24) or (L_Horario[1] < 0 or L_Horario[1] > 23):
                print("Horario inválido. Deve ser composto por numeros entre 0 e 23")
                return

            if Horario in Horarios_Visitas: #Verificar se ja existe alguma visita guiada para aquele horario
                print("Já tem uma visita guiada para este horário")
                return
        else:
            print("Horario inválido. Deve ser composto por digitos separados por -")
            return

        Novo_Valor = Horario #O codigo ficaria confuso com o nome da variavel a Novo_Valor

    #Se o campo a editar for Lotação maxima
    if Campo == Lista_Campos[1]:
        Novo_Valor = Utils.Ler_Inteiro_Limites(1, None, "Qual a lotação máxima? ")

    #Guardar o novo valor:
    Visita_Encontrada[Campo] = Novo_Valor
    print("Edição concluida com sucesso.")

    #Verificar se o tamanho dos campos Visita, Horario, Lotacao Maxima é maior do que os anteriores
    if len(str(Novo_Valor)) > Campos["Lotacao Maxima"]:
        Campos["Lotacao Maxima"] = len(str(Novo_Valor))

#Apagar
def Apagar():
    if Verificar() == True:
        return
    
    #Mostrar as visitas
    Listar(Visitas)

    #Utilizador escolher 
    Max = len(Visitas)
    N_Visita = Utils.Ler_Inteiro_Limites(0, Max,f"Visita a apagar (Numero) ou 0  para cancelar: ")

    if N_Visita == 0:
        return
    
    Visita_Encontrada = Visitas[N_Visita - 1] #Dicionario da visita encontrada
    Visitas.remove(Visita_Encontrada)
    print(f"Visita removida com sucesso")

    for N in range(N_Visita-1, Max-1):
        Visitas[N]["Visita"] -= 1

    #Determinar a maior palavra de cada campo
    for Visita in Visitas:
        for Campo in Campos:
            if len(str(Visita[Campo])) > Campos[Campo]:
                Campos[Campo] = len(str(Visita[Campo]))


#Adicionar Visitantes
def Adicionar_Visitantes():
    if Verificar() == True:
        return
    
    #Numero de Pessoas
    N_Pessoas = Utils.Ler_Inteiro_Limites(1, None, "Quantas pessoas são? ")

    #Listar todas com espaços livres para o nº de pessoas
    Visitas_Encontradas = []
    L_Visitas_Encontradas = []
    for Visita in Visitas:
        if Visita["Lotacao Maxima"] - Visita["Lotacao"] >= N_Pessoas:
            Visitas_Encontradas.append(Visita)
            L_Visitas_Encontradas.append(Visita["Visita"])

    if len(Visitas_Encontradas) < 1:
        print("Não foram encontradas visitas disponiveis")
        return
    Listar(Visitas_Encontradas)

    #Utilizador escolher qual visita
    Max = Visitas[len(Visitas) - 1]["Visita"] #N da ultima visita
    N_Visita = Utils.Ler_Inteiro_Limites(0, Max,f"Visita (Numero) ou 0 para cancelar: ")

    if N_Visita not in L_Visitas_Encontradas:
        if N_Visita != 0:
            print("Visita não corresponde às encontradas")
        return
    Visita = Visitas[N_Visita - 1] #Dicionario da visita encontrada

    #Id
    Id = 1
    if len(str(Visita["Lotacao"])) > 0:
        Id = len(Visita["Id"]) + 1 #Gera o id a partir do id da ultima visita
    print(f"Visita: {Visita['Visita']}, Horario: {Visita["Horario"]}, Id: {Id}")

    Visita["Lotacao"] += N_Pessoas
    Visita["Id"].update({Id:N_Pessoas})

    #Verificar se o tamanho do campo Lotacao é maior do que os anteriores
    if len(str(Visita["Lotacao"])) > Campos["Lotacao"]:
        Campos["Lotacao"] = len(str(Visita["Lotacao"]))

#Cancelar Visitas
def Cancelar_Visitantes():
    if Verificar() == True:
        return
    
    #Utilizador escolhe qual visita
    Max = len(Visitas)
    N_Visita = Utils.Ler_Inteiro_Limites(0, Max,f"Visita (Numero) ou 0 (Cancelar): ")
    if N_Visita == 0:
        return
    
    Visita = Visitas[N_Visita - 1]

    Id = Utils.Ler_Inteiro("Qual o id atribuido? ")

    if Id not in Visita["Id"]: #TODO: Percorrer dicionarios e ver qual tem
        print("O id indicado não existe")
        return

    N_Pessoas = Visita["Id"][Id]
    Visita["Lotacao"] -= N_Pessoas
    del Visita["Id"][Id]


#Listar 
def Listar(Visitas, Titulo = "Lista de Visitas"):
    """Função para listar os campos (Visita, Horario e Lotação maxima) de todas as Visitas"""

    if Verificar() == True:
        return

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
def Menu_Horarios():
    """SubMenu para os horarios das visitas"""

    while True:
        Op = Utils.Menu(["Adicionar", "Editar", "Apagar","Voltar"], "Menu dos horarios")
        print("")

        if Op == 0:
            break

        elif Op == 1:
            Adicionar_Horario()

        elif Op == 2:
            Editar()
        
        elif Op == 3:
            Apagar()
            
#Menu para Visitas Guiadas
def Menu_Visitas_Guiadas():
    """SubMenu para as visitas guiadas"""

    while True:
        Op = Utils.Menu(["Adicionar Visitantes", "Cancelar Visitas", "Voltar"], "Menu das visitas guiadas")
        print("")

        if Op == 0:
            break

        elif Op == 1:
            Adicionar_Visitantes()

        elif Op == 2:
            Cancelar_Visitantes()

#Menu principal do modulo
def MenuVisitas():
    """Menu para visitas"""
    os.system("cls")
    LerBinario()

    while True:
        Op = Utils.Menu(["Horarios", "Visitante", "Listar", "Voltar"], "Menu de visitas")
        os.system("cls")

        if Op == 0:
            break

        elif Op == 1:
            Menu_Horarios()

        elif Op == 2:
            Menu_Visitas_Guiadas()

        elif Op == 3:
            Op2 = Utils.Menu(["Visitas", "Marcações"], "O que pretende listar?")

            if Op2 == 1:
                Listar(Visitas)
            
            if Op2 == 2:
                Listar(Visitas)
        
        GuardarBinario()


#Verificar se a lista de visitas está vazia
def Verificar():
    #Verificar se existem visitas guiadas
    if len(Visitas) == 0:
        print("Não existem visitas guiadas definidas")
        return True
    
#Configurar: Adiciona dados de teste
def Configurar():
    Visitas.append({"Visita": 1, "Horario": "9-10" , "Lotacao": 8,  "Lotacao Maxima": 30, "Id": {1:8}})
    Visitas.append({"Visita": 2, "Horario": "11-12", "Lotacao": 21, "Lotacao Maxima": 30, "Id": {1:6,2:12,3:3}})
    Visitas.append({"Visita": 3, "Horario": "17-18", "Lotacao": 15, "Lotacao Maxima": 30, "Id": {1:3,2:12}})

    #Maior tamanho de cada campo dos dados de teste
    Campos["Visita"] = 1
    Campos["Horario"] = 5
    Campos["Lotacao"] = 1
    Campos["Lotacao Maxima"] = 2

#Guardar e ler os ficheiros binarios
def GuardarBinario():
    """Função para guardar os dados de Visitas num ficheiro binario"""
    if Verificar() == True:
        return
    
    with open(NOME_FICHEIRO, "wb") as Ficheiro:
        for Visita in Visitas:
            NVisita        = Visita["Visita"] #Inteiro
            Horario        = Visita["Horario"] #String 5 caracteres
            Lotacao        = Visita["Lotacao"] #Inteiro
            Lotacao_Maxima = Visita["Lotacao Maxima"] #Inteiro
            Id = str(Visita["Id"])
            Id = Id.strip("{}")

            #Adicionar ao ficheiro
            Dados_Empacotados = struct.pack(Formato,
                                            NVisita,
                                            Horario.encode("utf-8"),
                                            Lotacao,
                                            Lotacao_Maxima,
                                            Id.encode("utf-8"))
                                           
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
                Dados_Binarios = Ficheiro.read(140)
                if not Dados_Binarios:
                    break

                #Converter os dados
                Dados = struct.unpack(Formato, Dados_Binarios)

                #Adicionar os dados
                Visita = {"Visita":         Dados[0], 
                          "Horario":        Dados[1].decode("utf-8").rstrip("\x00"),
                          "Lotacao":        Dados[2],
                          "Lotacao Maxima": Dados[3],
                          "Id":             {}}

                #Adicionar o id das visitas
                Ids = Dados[4].decode("utf-8").rstrip("\x00")
                if Ids != "":
                    Ids = Ids.split(",")
                    for Id in Ids:
                        L_Id = Id.split(":")
                        Visita["Id"].update({int(L_Id[0]):int(L_Id[1])})

                #Adicionar as obras
                Visitas.append(Visita)

            except EOFError:
                break