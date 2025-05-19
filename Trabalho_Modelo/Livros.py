"""
Modulo de Gestão dos livros
"""
import Utils
import os, pickle

#Lista dos Livros
Livros = []

#Menu Livros
def MenuLivros():
    """SubMenu para gerir os livros"""
    os.system("cls")

    Op = 0
    while Op != 6:
        Op = Utils.Menu(["Adicionar", "Listar", "Editar", "Apagar", "Pesquisar", "Voltar"], "Menu de Livros")
        print("")

        if Op == 6:
            break

        if Op == 1 :
            Adicionar()

        if Op == 2 :
            Listar(Livros)

        if Op == 3 :
            Editar()

        if Op == 4 :
            pass

        if Op == 5 :
            Pesquisar_Listar()

#Campos que não podem ser editados pelo utilizador
Livros_Campos_Privados = ["Id", "Estado", "Leitor", "Nr Emprestimos"]

def Configurar():
    #Lista de Livros de exemplo
    Exemplo_Livros = [
    {"Id": 1, "Titulo": "Livro 1", "Autor": "Autor A", "Assunto": "Assunto 1", "Editora": "Editora A", "Ano": 2001, "Estado": "Disponivel", "Leitor": None, "Nr Emprestimos": 0},
    {"Id": 2, "Titulo": "Livro 2", "Autor": "Autor B", "Assunto": "Assunto 2", "Editora": "Editora B", "Ano": 2002, "Estado": "Disponivel", "Leitor": None, "Nr Emprestimos": 0},
    {"Id": 3, "Titulo": "Livro 3", "Autor": "Autor C", "Assunto": "Assunto 3", "Editora": "Editora C", "Ano": 2003, "Estado": "Disponivel", "Leitor": None, "Nr Emprestimos": 0}]

    """Insere dados de exemplo"""
    Livros.extend(Exemplo_Livros)

def Get_Livro(Id):
    """Função devolve o livro com base no Id indicado"""
    for Livro in Livros:
        if Livro["Id"] == Id:
            return Livro
    return None

#Adicionar Livro
def Adicionar():
    Utils.F_Titulo("Adicionar novo Livro")

    #Titulo
    Titulo = Utils.Ler_Strings(3, "Introduza o título: ")

    #Autor
    Autor = Utils.Ler_Strings(3, "Introduza o autor: ")

    #Assunto
    Assunto = Utils.Ler_Strings(3, "Introduza o assunto: ")

    #Editora
    Editora = Utils.Ler_Strings(3, "Introduza a editora: ")

    #Ano edição
    Ano = Utils.Ler_Inteiro_Limites(1500, 2030, "Introduza o ano de edição: ")

    #Id
    Id = 1
    if len(Livros) > 0:
        Id = Livros[len(Livros) - 1] ["Id"] + 1 #Gera o id a partir do id do ultimo livro

    Novo = {"Id": Id,
            "Titulo": Titulo,
            "Autor": Autor,
            "Assunto": Assunto,
            "Editora": Editora,
            "Ano": Ano,
            "Estado": "Disponivel",
            "Leitor": None,
            "Nr Emprestimos": 0}
    
    Livros.append(Novo)
    print(f"Livro registado com sucesso. Tem {len(Livros)} livros \n")

#Editar Livros
def Editar():
    #Pesquisar o livro a editar
    Livros_Editar = Pesquisar()

    #Mostrar os dados de cada um dos livros encontrados
    if len(Livros_Editar) == 0:
        print("Não foram encontrados livros.")
        return
    
    #Mostrar todos os livros
    Listar(Livros_Editar)

    #Permitir alterar os dados
    Id = Utils.Ler_Inteiro("Introduza o Id do livro a editar ou 0 (zero) para cancelar: ")

    if Id == 0:
        return

    #Livro com o Id indicado
    Livro = None
    for l in Livros_Editar:
        if l["Id"] == Id:
            Livro = l
            break

    if Livro == None:
        print("O Id indicado não existe.")
        return

    #Criar lista com todos os campos do livro
    Lista_Campos = list(Livro.keys())

    #Remover os campos privados
    for C in Livros_Campos_Privados:
        Lista_Campos.remove(C) 

    #Escolher o campo a editar
    Op = Utils.Menu(Lista_Campos, "Qual o campo a editar? ")
    Campo = Lista_Campos[Op - 1]
    
    #Mostrar o valor atual do campo a editar
    print(f"O campo {Campo} tem o valor {Livro[Campo]}\n")
    Novo_Valor = Utils.Ler_Strings(3, "Novo Valor: ")

    #Guardar o novo valor:
    Livro[Campo] = Novo_Valor
    print("Edição concluida com sucesso.")

#Apagar Livros
def Apagar():
    #Verificar se a lista está vazia
    if len(Livros) == 0:
        print("Não existem livros para apagar.")
        return
    
    #Pesquisar os livros com título semelhante
    L_Livros = Pesquisar()

    #Verificar se encontrou pelo menos 1
    if len(L_Livros) == 0:
        print("Não foi encontrado nenhum livro.")
        return


    #Confirmar para cada um dos leitores se deseja apagar
    for Livro in L_Livros:
        print(f"Titulo: {Livro["Titulo"]} | Autor: {Livro("Autor")} | Id: {Livro["Id"]}")
        Op = input("Deseja remover este livro (s/n)?")
        if Op in "Ss":
            #TODO: Confirmar se o livro não esta emprestado
            Livros.remove(Livro)
            break
    
    print(f"Livro removido com sucesso. Tem {len(Livros)} livros")

#Listar Livros
def Listar(Livros):
    """Função para listar todos os livros"""
    
    Utils.F_Titulo("Lista de Livros")

    print("-" * 80)
    for Livro in Livros:
        print(f"Id: {Livro["Id"]} | Nome: {Livro["Titulo"]} | Autor: {Livro["Autor"]} | Estado: {Livro["Estado"]} ")
        print("-" * 80)
    
    print("")

#Pesquisar Livros
def Pesquisar_Listar():
    Resultado = Pesquisar
    Listar(Resultado)

def Pesquisar(Titulo = "Escolha o campo de pesquisa: "):
    """Devolver a lista dos livros que correspondem a um critério"""
    #Deixar o utilizador escolher o campo de pesquisa
    Op = Utils.Menu(["Autor","Titulo"],Titulo)

    #Criar uma lista para os resultados
    L_Resultado = []
    if Op == 1:
        Campo = "Autor"
    else:
        Campo = "Titulo"
    Pesquisa = Utils.Ler_Strings(1,f"{Campo} a pesquisar: ")

    #Adicionar à lista os livros que correspondem ao resultado da pesquisa
    for Livro in Livros:
        if Pesquisa.lower() in Livro[Campo].lower():
            L_Resultado.append(Livro)

    return(L_Resultado)

def GuardarDados():
    with open("Livros.dat", "wb") as Ficheiro:
        pickle.dump(Livros, Ficheiro)

def LerDados():
    global Livros
    if os.path.exists("Livros.dat") == False:
        return
    
    with open("Livros.dat", "rb") as Ficheiro:
        Livros = pickle.load(Ficheiro)