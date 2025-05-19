import Utils, Emprestimos
from datetime import datetime

def MenuEstatisticas():
    Op = 0
    while Op != 5:
        Op = Utils.Menu(["Livro mais requisitado", "Leitor com mais requisições", "Empréstimos fora de praso", "Top meses", "Voltar"], "Menu Estatísticas")
        
        if Op == 5:
            break 

        if Op == 1:
            LivroMais()

        if Op == 2: 
            LeitorMais()
        
        if Op == 3:
            EmprestimosForaPrazo()
        
        if Op == 4:
            MesMais()

def LivroMais():
    """Função para encontrar o livro mais requisitado no ultimo mês (mês anterior ao mês atual)"""
    if len(Emprestimos.Emprestimos) == 0:
        print("Não tem empréstimos")

    #Mes e ano a pesquisar
    Data_Atual = datetime.now()
    Data_Atual = Data_Atual.strftime("%Y-%m-%d")
    Partes = Data_Atual.split("-")
    Ano = int(Partes)

    if Mes == 0:
        Mes = 12
        Ano = Ano + 1

    #Criar um Dicionario {Titulo : Contagem}
    Dicionario_Livros = {}

    #Percorrer Emprestimos
    for Emprestimo in Emprestimos.Emprestimos:
        #Verificar se é do mês anterior (comparar mes e ano)S
        Data_Emprestimo = Emprestimo["Data Emprestimo"]
        Ano_emprestimo = int(Data_Emprestimo[0])
        Mes_emprestimo = int(Data_Emprestimo[1])
        if Ano_emprestimo == Ano and Mes_emprestimo == Mes:
            #contar se sim
            if Emprestimo['livro']['titulo'] in Dicionario_Livros:
                Dicionario_Livros[Emprestimo['livro']['titulo']] += 1
        else:
            Dicionario_Livros[Emprestimo["Livro"]["Titulo"]]
        
    #percorrer o dicionário e encontrar o maior
    Maior = 0
    titulo_maior =""
    for livro in Dicionario_Livros:
        if Dicionario_Livros[livro]>Maior:
            titulo_maior = livro
            Maior = Dicionario_Livros[livro]
    print(f"O livro mais emprestado no mês anterior ({Mes}/{Ano}) foi {titulo_maior} com {Maior} empréstimos.")

def LeitorMais():
    """Função para mostrar o leitor com mais empréstimos"""
    if len(Emprestimos.Emprestimos) == 0:
        print("Não tem empréstimos")
    

    Dicionario_Leitores = {}
    for Emprestimo in Emprestimos.Emprestimos:
        Nome = Emprestimo["Leitor"]["Nome"]
        if Nome in Dicionario_Leitores:
            Dicionario_Leitores[Nome] += 1

        else:
            Dicionario_Leitores[Nome] = 1

    Nome_Maior = "" 
    Maior = 0

    for Leitor in Dicionario_Leitores:
        if Dicionario_Leitores[Leitor] > Maior:
            Maior = Dicionario_Leitores[Leitor]
            Nome_Maior = Leitor
    
    print(f"O leitor com mais empréstimos é {Nome_Maior}")

def EmprestimosForaPrazo():
    """Função para listar os emprestimos que ainda não acabaram e estão fora do prazo de entrega"""
    if len(Emprestimos.Emprestimos) == 0:
        print("Não tem emprestimos \n")
        return
        
    # Criar variavel para data atual
    Data_Atual = datetime.now()

    # Converter para inteiro
    IData_Atual = int(Data_Atual.strftime("%Y%m%d"))

    #Contar o nº de emprestimos fora do praso
    Contar = 0

    # Percorrer a listas dos empréstimos
    for Emprestimo in Emprestimos.Emprestimos:
        # Converter a data dos emprestimos em inteiro
        Data_Devolucao = Emprestimo["Data Devolução"]
        IData_Devolucao = int(datetime.strptime(Data_Devolucao, "%Y-%m-%d").strftime("%Y%m%d"))

        # Comparar com data atual
        if IData_Atual > IData_Devolucao and Emprestimo["Estado"] == True:
            Dias_Atraso = IData_Atual - IData_Devolucao
            print(f"o leitor {Emprestimo["Leitor"]["Nome"]} tem o livro {Emprestimo["Livro"]["Titulo"]} por entregar fora do praso à {Dias_Atraso} dias.")
            Contar += 1
    print("")

    Percentagem = (Contar / len(Emprestimos.Emprestimos)) * 100
    print(f"{Percentagem}% de empréstimos fora do prazo")

def MesMais():
    """Mostra o mês em que existem mais requisições, independente do ano"""
    if len(Emprestimos.Emprestimos) == 0:
        print("Não tem emprestimos \n")
        return
    
    Meses = []
    for i in range(12):
        Meses.append(0)

    #Percorrer os empréstimos
    for Emprestimo in Emprestimos.Emprestimos:
        #Extrair o mês da data do empréstimo
        Partes = Emprestimo["Data Emprestimo"].split("-")
        Mes_Emprestimo = int(Partes[1]) 
        
        #Somar 1 na lista dos meses na posição do mês do emprestimo
        Meses[Mes_Emprestimo - 1] += 1

    #Percorrer a lista dos meses e encontrar o maior
    Posicao_Maior = 0
    for i in range(len(Meses)):
        if Meses[i] > Meses[Posicao_Maior]:
            Posicao_Maior = i
    
    #Mostrar a posição do maior +1
    print(f"O mês que tem mais empréstimos é {Posicao_Maior + 1} com {Meses[Posicao_Maior]}")