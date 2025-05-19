"""
Modulo de Gestão dos Leitores"
"""
import Utils
import os, pickle

"""
Ideias:
- Verificar Email
- Editar Melhorado
- Apagar
- Função para ver as informações do leitor
"""

#Lista dos Leitores
Leitores = []

#Menu Leitores
def MenuLeitores():
    """SubMenu para gerir os leitores"""
    os.system("cls")

    Op = 0
    while Op != 6:
        Op = Utils.Menu(["Adicionar", "Listar", "Editar", "Apagar", "Pesquisar", "Infrações", "Voltar"], "Menu de Leitores")
        print("")

        if Op == 7:
            break

        if Op == 1:
            Adicionar()

        if Op == 2:
            Listar(Leitores)

        if Op == 3:
            Editar()

        if Op == 4:
            Apagar()

        if Op == 5:
            Pesquisar_Listar()

        if Op == 6:
            pass

#Campos que não podem ser editados pelo utilizador
Leitores_Campos_Privados = ["Id", "Infracoes"]

def Configurar():
    #Lista de Leitores de exemplo
    Exemplo_Leitores = [
    {"Id": 1, "Nome": "Leitor 1", "Idade": 20, "Email": "Leitor1@gmail.com", "Infracoes": ""},
    {"Id": 2, "Nome": "Leitor 2", "Idade": 34, "Email": "Leitor2@gmail.com", "Infracoes": ""},
    {"Id": 3, "Nome": "Leitor 3", "Idade": 98, "Email": "Leitor3@gmail.com", "Infracoes": ""}]

    """Inserir dados de exemplo"""
    Leitores.extend(Exemplo_Leitores)

def Get_Leitor(Id):
    """Função devolve o leitor com base no Id indicado"""
    for Leitor in Leitores:
        if Leitor["Id"] == Id:
            return Leitor
    return None

#Adicionar Leitor
def Adicionar():
    Utils.F_Titulo("Adicionar novo Leitor")

    #Nome
    Nome = Utils.Ler_Strings(3, "Introduza o Nome: ")

    #Ano edição
    Idade = Utils.Ler_Inteiro_Limites(7, 150, "Introduza a Idade: ")

    #Email
    Email = Utils.Ler_Strings(3, "Introduza o Email: ")

    #Id
    Id = 1
    if len(Leitores) > 0:
        Id = Leitores[len(Leitores) - 1] ["Id"] + 1 #Gera o id a partir do id do ultimo leitor
    
    Novo = {"Id": Id,
            "Nome": Nome,
            "Idade": Idade,
            "Email": Email,
            "Infracoes": ""}
    
    Leitores.append(Novo)
    print(f"Leitor registado com sucesso. Tem {len(Leitores)} leitores \n")

#Editar leitors
def Editar():
    #Pesquisar o leitor a editar
    Leitores_Editar = Pesquisar()

    #Mostrar os dados de cada um dos leitors encontrados
    if len(Leitores_Editar) == 0:
        print("Não foram encontrados leitors.")
        return
    
    #Mostrar todos os Leitores
    Listar(Leitores_Editar)

    #Permitir alterar os dados
    Id = Utils.Ler_Inteiro("Introduza o Id do leitor a editar ou 0 (zero) para cancelar: ")

    if Id == 0:
        return

    #Leitor com o Id indicado
    Leitor = None
    for l in Leitores_Editar:
        if l["Id"] == Id:
            Leitor = l
            break

    if Leitor == None:
        print("O Id indicado não existe.")
        return

    #Criar lista com todos os campos do leitor
    Lista_Campos = list(Leitor.keys())

    #Remover os campos privados
    for C in Leitores_Campos_Privados:
        Lista_Campos.remove(C) 

    #Escolher o campo a editar
    Op = Utils.Menu(Lista_Campos, "Qual o campo a editar? ")
    Campo = Lista_Campos[Op - 1]
    
    #Mostrar o valor atual do campo a editar
    print(f"O campo {Campo} tem o valor {Leitor[Campo]}\n")
    Novo_Valor = Utils.Ler_Strings(1, "Novo Valor: ")

    #Guardar o novo valor:
    Leitor[Campo] = Novo_Valor
    print("Edição concluida com sucesso.")

#Apagar
def Apagar():
    #Verificar se a lista está vazia
    if len(Leitores) == 0:
        print("Não existem leitores para apagar. \n")
        return
    
    #Pesquisar os leitores com título semelhante
    L_Leitores = Pesquisar()

    for Leitor in Leitores:
        print(f"Id: {Leitor["Id"]} | Nome: {Leitor["Nome"]} | Idade: {Leitor["Idade"]} | Email: {Leitor["Email"]}")
        Op = input("Deseja remover este leitor? ")

        if Op in "Ss":
            #TODO:
            Leitores.remove(Leitor)
            print("Livro reovido com sucesso.")
            break

#Listar Leitores
def Listar(L_Leitores):
    """Função para listar todos os Leitores"""
    
    Utils.F_Titulo("Lista de Leitores")

    print("-" * 80)
    for Leitor in L_Leitores:
        print(f"Id: {Leitor["Id"]} | Nome: {Leitor["Nome"]} | Idade: {Leitor["Idade"]} | Email: {Leitor["Email"]} | Infrações: {Leitor["Infracoes"]} ")
        print("-" * 80)
    
    print("")

#Pesquisar Leitores
def Pesquisar_Listar():
    Resultado = Pesquisar()
    Listar(Resultado)

def Pesquisar(Titulo = "Escolha o campo de pesquisa: "):
    """Devolver a lista dos leitores que correspondem a um critério"""

    #Deixar o utilizador escolher o campo de pesquisa
    Op = Utils.Menu(["Id","Nome", "Email"], Titulo)

    #Criar uma lista para os resultados
    L_Resultado = []
    if Op == 1:
        Campo = "Id"

    if Op == 2:
        Campo = "Nome"

    if Op == 3:
        Campo = "Email"

    Pesquisa = Utils.Ler_Strings(1,f"{Campo} a pesquisar: ")

    #Adicionar à lista os leitores que correspondem ao resultado da pesquisa
    for Leitor in Leitores:
        if Pesquisa in str(Leitor[Campo]):
            L_Resultado.append(Leitor)

    return(L_Resultado)

def GuardarDados():
    with open("Leitores.dat", "wb") as Ficheiro:
        pickle.dump(Leitores, Ficheiro)

def LerDados():
    global Leitores
    if os.path.exists("Leitores.dat") == False:
        return
    
    with open("Leitores.dat", "rb") as Ficheiro:
        Leitores = pickle.load(Ficheiro)