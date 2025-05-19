"""
Modulo Emprestimos e devolocoes
"""
import Utils, Livros, Leitores
from datetime import datetime, timedelta
import os, pickle

#Livro, Leitor, Data_Emprestimo, Data_Devolução, Estado
Emprestimos = []

def MenuEmprestimos():
    """SubMenu para gerir os empréstimos"""
    os.system("cls")

    Op = 0
    while Op != 3:
        Op = Utils.Menu(["Empréstimos", "Devolução", "Listar", "Voltar"], "Menu de Empréstimos / Devoluções")

        if Op == 4:
            os.system("cls")
            break

        if Op == 1:
            Emprestimo()

        if Op == 2:
            Devolocao()
        
        if Op == 3:
            Listar()

def Emprestimo():
    #Dados do emprestimo a adicionar à lista
    Novo = {} 

    # Ler qual o livro a emprestar
    Livro_Emprestar = Livros.Pesquisar("Indique campo de pesquisa do livro a emprestar")

    if len(Livro_Emprestar) == 0:
        print("O livro não foi encontrado, Tente novamente. \n")
        return

    elif len(Livro_Emprestar) > 1:
        #Mostrar livros encontrados
        Livros.Listar(Livro_Emprestar)

        #Pedir o Id do livro a emprestar
        Id = Utils.Ler_Inteiro("Introduza o Id do livro a emprestar: ")

        for Livro in Livro_Emprestar:
            if Livro["Id"] == Id:
                if Livro["Estado"] != "Disponivel":
                    print("Este livro está emprestado. \n")
                    return
                
                Novo["Livro"] = Livro
                break

        if "Livro" not in Novo:
            print("O Id indicado não existe \n")
            return

    else: #Só encontrou 1 livro
        if Livro_Emprestar[0]["Estado"] != "Disponivel":
            print("Esse livro está emprestado. \n")
            return
        Novo["Livro"] = Livro_Emprestar[0]

    # Ler qual o leitor que leva o livro
    Leitor_Emprestimo = Leitores.Pesquisar("Indique o Leitor")

    if len(Leitor_Emprestimo) == 0:
        print("Leitor não encontrado \n")
        return

    elif len(Leitor_Emprestimo) > 1:
        print("leitores encontrados tgthget")
        Leitores.Listar(Leitor_Emprestimo)

        Id = Utils.Ler_Inteiro("Indique o Id do Leitor: ")

        for Leitor in Leitor_Emprestimo:
            if Leitor["Id"] == Id:
                Novo["Leitor"] = Leitor
                break

        if Leitor not in Novo:
            print("O Id indicado não existe. \n")
            return

    else:
        Novo["Leitor"] = Leitor_Emprestimo[0]

    #TODO: Verificar se o leitor pode levar o livro
    # Registar o empréstimo com data de devolução
    Data_Atual = datetime.now()
    Data_Entrega = Data_Atual + timedelta(days=30)

    #Transformar as datas em string
    Str_Data_Atual = Data_Atual.strftime("%Y-%m-%d")
    Str_Data_Entrega = Data_Entrega.strftime("%Y-%m-%d")

    #Adicionar ao dicionario a data atual e a data de entrega
    Novo["Data Emprestimo"] = Str_Data_Atual
    Novo["Data Devolução"] = Str_Data_Entrega
    Novo["Estado"] = True
    Emprestimos.append(Novo)

    # Atualizar o estado do livro
    Novo["Livro"]["Estado"] = "Emprestado"
    Novo["Livro"]["Leitor"] = Novo["Leitor"]

    print("Emprestimo registado com sucesso :D \n")
    print(f"Livro Emprestado: {Novo["Livro"]}")
    print(f"Leitor: {Novo["Leitor"]}")

def Devolocao():
    """
    Ideias:
    O que acontece se o livro não estiver em condições
    """
    # Ler o Id do Livro a devolver
    Id_Livro = Utils.Ler_Inteiro("Introduza o Id do livro a devolver: ")

    # Verificar se o livro está emprestado
    Livro = Livros.Get_Livro(Id_Livro)
    if Livro == None:
        print("Não existe nenhum livro com o Id indicado \n")

    if Livro["Estado"] != "Emprestado":
        print("Esse livro não está emprestado")

    # Verificar se a devolução está dentro do prazo
    Emprestimo_Devolover = None

    for Emprestimo in Emprestimos:
        if Emprestimo["Livro"] == Livro and Emprestimo["Estado"] == True:
            Emprestimo_Devolover = Emprestimo

    if Emprestimo_Devolover == None:
        print("Empréstimo não encontrado x_x \n")
        return
    
    Data_Devolucao = Emprestimo_Devolover["Data Devolução"]
    Data_Atual = datetime.now()

    #Comparar como datetime ou inteiro? Resposta Afonso: Inteirooooo
    IData_Atual = int(Data_Atual.strftime("%Y%m%d"))
    IData_Devolução = int(datetime.strptime(Data_Devolucao, "%Y-%m-%d").strftime("%Y%m%d"))

    if IData_Atual > IData_Devolução:
        print("Devolução fora de prazo \n")

        # Registar se houve infração do leitor
        Emprestimo_Devolover["Leitor"]["Infrações"] += "Entrega fora de Prazo"
    
    # Atualizar o nº de emprestimos do livro
    Livro["Nr Emprestimos"] += 1

    # Mudar o estado do Livro
    Livro["Estado"] = "Disponivel"
    Livro["Leitor"] = None

    # Mudar o estado do emprestimo
    Emprestimo_Devolover["Estado"] = False
    print("Devolução concluida com sucesso \n")

def Listar():
    # Perguntar se pretende ver todos os empréstimos
    # Só os empréstimos por concluir

    Op = Utils.Ler_Strings(1, "Listar [T]odos ou só [C]oncluir ")

    for Emp in Emprestimos:
        if Op in "Tt" or (Op in "Cc" and Emp["Estado"] == True):
            print(f"{Emp["Livro"]["Titulo"]} {Emp["Leitor"]["Nome"]} {Emp["Estado"]}")

def GuardarDados():
    Lista_Ficheiro = []

    for e in Emprestimos:
        Novo = {
        #Substituir a referência para lista leitores para o id
        "Id_Leitor": e["Leitor"]["Id"],

        #Substituir a referência para lista livros para o id
        "Id_Livro": e["Livro"]["Id"],

        "Data Emprestimo": e["Data Emprestimo"],
        "Data Devolução" : e["Data Devolução"],
        "Estado"         : e["Estado"]}

    with open("Emprestimos.dat", "wb") as Ficheiro:
        pickle.dump(Lista_Ficheiro, Ficheiro)
    
def LerDados():
    global Emprestimos

    Emprestimos = []
    Lista_Ficheiro = []
    if os.path.exists("Emprestimos.dat") == False:
        return

    with open("Emprestimos.dat", "rb") as Ficheiro:
        Lista_Ficheiro = pickle.load(Ficheiro)

    #Criar a lista empréstimos com as referências para livros e leitores
    for e in Lista_Ficheiro:
        Novo = {
        "Data Emprestimo": e["Data Emprestimo"],
        "Data Devolução" : e["Data Devolução"],
        "Estado"         : e["Estado"],
        "Leitor"         : Leitores.Get_Leitor(e["Id_Leitor"]),
        "Livro"          : Livros.Get_Livro(e["Id_Livro"])}

        Emprestimos.append(Novo)