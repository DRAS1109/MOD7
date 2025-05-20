"""
Modulo de gestão de obras
"""
import Utils
from datetime import datetime
import os, struct

#Nome do ficheiro
NOME_FICHEIRO = "Obras.bin"
#Formato em que os dados são armazenadas
Formato = "i35si35sf8s100s"

#Lista das obras:
Colecao = []

#Lista de raridades das obras
Raridades = ["Comum", "Raro", "Epico", "Lendario", "Mitico"]

#Dicionario para guardar os campos e o comprimento da maior palavra de cada campo
Campos = {"Id": 0, "Tipo": 0, "Ano": 0, "Autor": 0} 

#Menu Obras
def MenuObras():
    """SubMenu para as obras"""

    while True:
        Op = Utils.Menu(["Adicionar", "Editar", "Apagar", "Listar", "Pesquisar", "Voltar"], "Menu de Obras")
        print("")

        if Op == 0:
            break

        elif Op == 1:
            Adicionar()

        elif Op == 2:
            Editar()
        
        elif Op == 3:
            Apagar()

        elif Op == 4:
            Listar(Colecao)
        
        elif Op == 5:
            Pesquisar_Listar()

#Adicionar
def Adicionar():
    Utils.F_Titulo("Adicionar nova obra")

    #Tipo
    Tipo = Utils.Ler_Strings(2, "Qual o tipo da obra? ")
    if len(Tipo) > Campos["Tipo"]:
        Campos["Tipo"] = len(Tipo)

    #Ano
    Ano = Adicionar_Ano()

    #Autor
    Autor = Utils.Ler_Strings(2, "Qual o autor da obra? ")
    if len(Autor) > Campos["Autor"]:
        Campos["Autor"] = len(Autor)

    #Preço Atual
    while True:
        Preco_Atual = Utils.Ler_Decimal("Qual o preço atual da obra? ")
        if Preco_Atual > 0:
            break

        else:
            print("O preço precisa ser um valor positivo")

    #Raridade
    N_Raridade = Utils.Menu(Raridades, "Qual a raridade da obra? ")
    Raridade = Raridades[N_Raridade - 1]

    #Descrição
    Descricao = Utils.Ler_Strings(2, "Introduza uma pequena descrição da obra: \n")

    #Id
    Id = 1
    if len(Colecao) > 0:
        Id = Colecao[len(Colecao) - 1]["Id"] + 1 #Gera o id a partir do id da ultima obra
    
    if len(str(Id)) > Campos["Id"]:
        Campos["Id"] = len(str(Id))

    Nova_Obra ={"Id": Id,
                "Tipo": Tipo,
                "Ano": Ano,
                "Autor": Autor,
                "Preco Atual": Preco_Atual,
                "Raridade": Raridade,
                "Descricao": Descricao}
    
    Colecao.append(Nova_Obra)
    print(f"Obra registada com sucesso. Tem {len(Colecao)} obras no seu Museu \n")

#Editar
def Editar():
    if Verificar() == True:
        return
    
    #Pesquisar a obra a editar
    Resultado = Pesquisar("Campo a pesquisar")

    if Resultado == None:
        return

    #Mostrar se não encontrar nenhuma obra
    if len(Resultado) == 0:
        print("Não foram encontradas obras com esse critério")
        return
    
    #Mostrar todas as obras encontradas
    Listar(Resultado, None)

    #Se forem varios deixar o utilizador escolher e caso a pesquisa encontre apenas 1, deixar o utilizador cancelar a ação
    Id = Utils.Ler_Inteiro("Introduza o Id da Obra a editar (0 para cancelar): ")
    if Id == 0:
        return
    
    Obra_Encontrada = None #Caso não encontre nenhuma obra, a variavel fica criada
    for Obra in Resultado:
        if Obra["Id"] == Id:
            Obra_Encontrada = Obra
    
    if Obra_Encontrada == None: #Caso não exista nenhuma Obra com o Id indicado (Se estiver a None), alertar o utilizador
        print(f"Não foi encontrada nenhuma obra com o id {Id}")
        return
    
    #Criar lista com todos os campos da obra (Exceto id)
    Lista_Campos = list(Obra_Encontrada.keys())
    Lista_Campos.remove("Id")

    #Escolher o campo a editar
    Op = Utils.Menu(Lista_Campos, "Qual o campo a editar? ")
    Campo = Lista_Campos[Op - 1]

    #Mostrar o valor atual do campo a editar
    print(f"O campo {Campo} tem o valor {Obra_Encontrada[Campo]}\n")

    if Campo == "Ano":
        Novo_Valor = Adicionar_Ano()

    elif Campo == "Preco Atual":
        #Preço Atual
        while True:
            Novo_Valor = Utils.Ler_Decimal("Qual o preço atual da obra? ")
            if Novo_Valor > 0:
                break

            else:
                print("O preço precisa ser um valor positivo")

    elif Campo == "Raridade":
        #Raridade
        N_Raridade = Utils.Menu(Raridades, "Qual a raridade da obra? ")
        Novo_Valor = Raridades[N_Raridade - 1]

    else:
        Novo_Valor = Utils.Ler_Strings(3, "Novo Valor: ")

    #Guardar o novo valor:
    Obra_Encontrada[Campo] = Novo_Valor
    print("Edição concluida com sucesso.")

    if Campo in Campos:
        if len(str(Novo_Valor)) > Campos[Campo]:
            Campos[Campo] = len(str(Novo_Valor))

#Apagar
def Apagar():
    if Verificar() == True:
        return
    
    #Pesquisar a obra a apagar
    Resultado = Pesquisar("Campo a pesquisar")

    #Mostrar se não encontrar nenhuma obra
    if len(Resultado) == 0:
        print("Não foram encontradas obras com esse critério")
        return
    
    #Mostrar todas as obras encontradas
    Listar(Resultado, None)

    #Deixar o utilizador escolher a obra a apagar e deixar o utilizador cancelar a ação
    Id = Utils.Ler_Inteiro("Introduza o Id da Obra a apagar (0 para cancelar): ")
    if Id == 0:
        return
    
    Obra_Encontrada = None #Caso não encontre nenhuma obra o programa não vai a baixo
    for Obra in Resultado:
        if Obra["Id"] == Id:
            Obra_Encontrada = Obra
    
    if Obra_Encontrada == None: #Caso não exista nenhuma Obra com o Id indicado (Se estiver a None), alertar o utilizador
        print(f"Não foi encontrada nenhuma obra com o id {Id}")
        return
    
    Colecao.remove(Obra_Encontrada)
    print(f"Obra removida com sucesso, tem {len(Colecao)} obras")

    #Determinar a maior palavra de cada campo pois o maior pode ter sido eliminado
    for Obra in Colecao:
        for Campo in Campos:
            if len(str(Obra[Campo])) > Campos[Campo]:
                Campos[Campo] = len(str(Obra[Campo]))

#Listar
def Listar(Colecao, Titulo = "Lista de Obras", Campos = Campos):
    """Função para listar os campos (Id, Tipo, Ano, Autor) de todas as obras"""
    if Verificar() == True:
        return

    #Determinar a maior palavra de cada campo
    for Obra in Colecao:
        for Campo in Campos:
            if len(str(Obra[Campo])) > Campos[Campo]:
                Campos[Campo] = len(str(Obra[Campo])) #Guardar o tamanho da maior palavra de cada campo

    #Descobiri o tamanho da linha --------------
    Tamanho = 0
    for Campo in Campos:
        Tamanho += Campos[Campo] + len(Campo)

    #Adicionar à variavel tamanho os "extras" (espaços, : e |)
    Extras = (len(Campos) *2) + (len(Campos) *3) + 1
        #*2 porque cada campo tem : e espaços
        #*3 porque cada campo tem espaço | espaço
        #+1 porque começa e termina com 1 |
    Tamanho += Extras  

    #Imprimir Titulo
    Utils.F_Titulo(Titulo)

    #Imprimir os dados
    print(Tamanho * "-")
    for Obra in Colecao:
        Linha = ""
        for Campo in Campos:
            CampoTexto = f"{Campo}: {Obra[Campo]}"
            Espacos = " " * (Campos[Campo] - len(str(Obra[Campo])))
            Linha += f"| {CampoTexto}{Espacos} "
        Linha += "|"
        print(Linha)
        print("-" * Tamanho)

#Pesquisar
def Pesquisar_Listar():
    """Apresenta lista de obras que correspondem ao critério"""
    Resultado = Pesquisar()
    if Resultado == None:
        return
    
    Listar(Resultado, "Obras encontradas")

def Pesquisar(Titulo = "Escolha o campo de pesquisa: "):
    """Devolve a lista de obras que correspondem ao critério"""
    if Verificar() == True:
        return
    
    #Menu para o utilizador escolher o campo de pesquisa
    Op = Utils.Menu(["Tipo","Ano", "Autor", "Raridade", "Voltar"],Titulo)

    if Op == 0:
        return None

    #Criar uma lista para os resultados
    L_Resultado = []
    if Op >= 1 and Op <= 3:
        if Op == 1:
            Campo = "Tipo"

        if Op == 2:
            Campo = "Ano"

        if Op == 3:
            Campo = "Autor"

        Pesquisa = Utils.Ler_Strings(1,f"{Campo} a pesquisar: ")
    
    else:
        if Op == 4:
            Campo = "Raridade"
        
        Raridade = Utils.Menu(Raridades, "Qual a raridade da obra? ")
        Pesquisa = Raridades[Raridade - 1]

    #Adicionar à lista as Obras que correspondem ao resultado da pesquisa
    for Obra in Colecao:
        if Pesquisa.lower() in str(Obra[Campo]).lower():
            L_Resultado.append(Obra)

    return(L_Resultado)

#Verificar se a coleção está vazia
def Verificar():
    #Verificar se existem obras no museu
    if len(Colecao) == 0:
        print("Não existem obras na coleção")
        return True

#Adicionar Ano (com verificações)
def Adicionar_Ano():
    Data_Atual = datetime.now()
    Str_Data_Atual = Data_Atual.strftime("%Y-%m-%d")

    Str_Data_Atual = Str_Data_Atual.split("-")
    Ano_Atual = int(Str_Data_Atual[0])

    Ano = Utils.Ler_Inteiro_Limites(-4543000000, Ano_Atual, "Introduza o ano criação da obra: ")

    if len(str(Ano)) > Campos["Ano"]:
        Campos["Ano"] = len(str(Ano))
    return Ano

#Configurar
def Configurar():
    Exemplo_Obras = [
    {"Id": 1, "Tipo": "Livro", "Ano": 1984, "Autor": "O melhor", "Preco Atual": 15.99, "Raridade": "Comum", "Descricao": "Um clássico da ciencia."},
    {"Id": 2, "Tipo": "Moeda", "Ano": 1675, "Autor": "Julio César", "Preco Atual": 1390.26, "Raridade": "Raro", "Descricao": "Uma moeda Romana"},
    {"Id": 3, "Tipo": "Pintura", "Ano": 1214, "Autor": "Leonardo Da Vinci", "Preco Atual": 1394300, "Raridade": "Epico", "Descricao": "Uma rara pintura de Leonardo Da Vinci"}]

    #Adicionar as obras
    Colecao.extend(Exemplo_Obras) #append adiciona, extend junta

def GuardarDados():
    """Função para guardar os dados de Obras num ficheiro binario"""
    if Verificar() == True:
        return
    
    with open(NOME_FICHEIRO, "wb") as Ficheiro:
        for Obra in Colecao:
            Id          = Obra["Id"] #Inteiro
            Tipo        = Obra["Tipo"] #String 35 caracteres
            Ano         = Obra["Ano"] #Inteiro
            Autor       = Obra["Autor"] #String 35 caracteres
            Preco_Atual = Obra["Preco Atual"] #Float
            Raridade    = Obra["Raridade"] #String 8 caracteres
            Descricao   = Obra["Descricao"] #String 106 Caracteres

            #Adicionar ao ficheiro
            Dados_Empacotados = struct.pack(Formato,
                                            Id,
                                            Tipo.encode("utf-8"),
                                            Ano,
                                            Autor.encode("utf-8"),
                                            Preco_Atual,
                                            Raridade.encode("utf-8"),
                                            Descricao.encode("utf-8"))
            
            Ficheiro.write(Dados_Empacotados)

def LerDados():
    """Função para ler os dados de um ficheiro binario"""
    if os.path.exists(NOME_FICHEIRO) == False:
        return
    
    with open(NOME_FICHEIRO, "rb") as Ficheiro:
        while True:
            try:
                #Ler os dados todos de uma vez só
                Dados_Binarios = Ficheiro.read(192)
                if not Dados_Binarios:
                    break

                #Converter os dados
                Dados = struct.unpack(Formato, Dados_Binarios)

                #Adicionar os dados
                Obra = {"Id":          Dados[0], 
                        "Tipo":        Dados[1].decode("utf-8").rstrip("\x00"), 
                        "Ano":         Dados[2], 
                        "Autor":       Dados[3].decode("utf-8").rstrip("\x00"), 
                        "Preco Atual": Dados[4], 
                        "Raridade":    Dados[5].decode("utf-8").rstrip("\x00"), 
                        "Descricao":   Dados[6].decode("utf-8").rstrip("\x00")}

                #Adicionar as obras
                Colecao.append(Obra)

            except EOFError:
                break