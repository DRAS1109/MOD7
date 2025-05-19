def Ler_Inteiro(Mensagem="Introduza um valor inteiro: ") -> int:
    """
    Função que lê do utilizador um número inteiro.
    Também garante que o valor inserido é válido.
    """

    while True:
        Dados = input(Mensagem)

        if len(Dados) == 0:
            continue

        #Verificar se existe um - no inicio da String
        if Dados[0] == "-":
            Testar = Dados.replace("-", "")

        else:
            Testar = Dados

        if Testar.isdigit():
            return int(Dados)
        print("Erro: O valor inserido não é válido \n")


def Ler_Inteiro_Limites(Min, Max=None, Mensagem="Introduza um valor inteiro: ") -> int:
    """
    Função que recebe o valor Min e Max a ler do utilizador.
    A função devolve o valor quando é um inteiro válido.
    """

    while True:
        X = Ler_Inteiro(Mensagem)

        if Max == None or Min == None or (X >= Min and X <= Max):
            return X
        
        else:
            print("O valor não é válido\n")

def Ler_Decimal(Mensagem="Introduza um valor inteiro: "):
    """
    Função que lê do utilizador um número decimal.
    Também garante que o valor inserido é válido e aceita como separador das casas decimais . ou , .
    """
    
    while True:
        Dados = input(Mensagem)

        if len(Dados) == 0:
            continue

        #Substituir , por .
        Dados = Dados.replace(",", ".")

        #Verificar se existe um - no inicio da String
        if Dados[0] == "-":
            Testar = Dados.replace("-", "")

        else:
            Testar = Dados

        #Contar os pontos decimais
        Pontos = Testar.count(".")

        #remover os pontos decimais
        Testar = Testar.replace(".", "")

        #Não pode ter mais de 1 ponto decimal e só pode ter digitos
        if Testar.isdigit() and Pontos <= 1:
            return float(Dados)
        print("Erro: O valor inserido não é válido \n")

def Ler_Decimal_Limites(Min, Max=None, Mensagem="Introduza um valor inteiro: ") -> int:
    """
    Função que recebe o valor Min e Max a ler do utilizador.
    Também garante que o valor inserido é válido e aceita como separador das casas decimais . ou , .
    """

    while True:
        X = Ler_Decimal(Mensagem)

        if Max == None or (X >= Min and X <= Max):
            return X
        
def Ler_Nome_Litimes(Min, Max=None, Mensagem="Introduza uma palavra: "):
    """
    Função que recebe o valor Min e Max de letras a ler do utilizador.
    Também garante que a palavra inserido é válido.
    """

    while True:
        Nome = input(Mensagem)
        if (Min == None and len(Nome) <= Max) or (Max == None and len(Nome) >= Min) or (len(Nome) >= Min and len(Nome) <= Max):
            return Nome

def Bubble_Sort(Vetor):
    Tamanho = len(Vetor)
    for i in range(Tamanho):
        for j in range(0, Tamanho - i - 1):
            if Vetor[j] > Vetor[j + 1]:
                Temp = Vetor[j]
                Vetor[j] = Vetor[j + 1]
                Vetor[j + 1] = Temp
    
    return Vetor

def Menu(Opcoes, Titulo=""):
    """Função recebe as opções a mostrar de um menu. Le a opção do utilizador e se for válida devolve essa opção"""
    #Mostrar o titulo do menu
    if Titulo != "":
        F_Titulo(Titulo)

    #Mostrar as opções com 1 nº
    for i in range(len(Opcoes)):
        print(f"{i + 1}) {Opcoes[i]}")

    #Ler a opção do uilizador
    Op = Ler_Inteiro_Limites(1, len(Opcoes), "Opção: ")

    #Se for valida devolvemos
    return Op

def Media(Valores):
    """Devolve a média dos valores de um tuple ou lista"""

    return sum(Valores/len(Valores))

#Alterado a 12-03-2025
def Ler_Strings(Tamanho_Min, Mensagen="Introduza um texto: "):
    """Função devolve uma string com um mínimo de letras. 
    Remove os espaços em branco do inicio e do final. 
    Mostra uma mensagem para a introdução do código"""
    while True:
        Texto = input(Mensagen)
        Texto = Texto.strip()
        if len(Texto) >= Tamanho_Min:
            return(Texto)
        
        print(f"O texto inserido não é válido. Tem de ter no mínimo {Tamanho_Min} de letras\n")

def F_Titulo(Mensagem):
    """Função que coloca a mensagem do Titulo entre linhas"""
    print(f" {"_"*(len(Mensagem) + 2)}\n| {Mensagem} |\n{" ̅"*(len(Mensagem) + 2)}")