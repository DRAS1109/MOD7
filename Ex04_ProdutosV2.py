"""
Programa para adicionar o nome de um produto e o preço
"""
import os
NOME_FICHEIRO = "Geral.txt"


def Adicionar():
    #Se o ficheiro existir adiciona, se não existir cria
    Acao = "w"
    if os.path.exists(NOME_FICHEIRO) == True:
        Acao = "a"

    with open(NOME_FICHEIRO, Acao, encoding="utf=8") as Ficheiro:
        while True:
            Nome  = input(f"Nome do Produto (Enter para cancelar): ").strip().capitalize()

            if Nome != "":
                Preco = float(input(f"Preço do Produto: "))
                print("")

                Ficheiro.write(f"{Nome} - {Preco} \n")
            
            else:
                break

def Ler():
    #Verificar se o ficheiro existe
    if Ficheiro_Existe() == False:
        return

    with open("Geral.txt", "r", encoding="utf-8") as Ficheiro:
        while True:
            Linha = Ficheiro.readline()
            #Verificar se encontrou o fim do ficheiro:
            if not Linha:
                break

            Partes = Linha.split("-")
            Nome = Partes[0].strip()
            Preco = float(Partes[1].strip())
            print(f"Produto: {Nome} | Preço: {Preco}")
        print("\n")

def Editar():
    #Verificar se o ficheiro existe
    if Ficheiro_Existe() == False:
        return

    #Ler o nome do produto a editar
    Nome = input("Qual o produto a editar? ")

    #Abrir o ficheiro dos produtos para ler
    Ficheiro_Ler      = open(NOME_FICHEIRO, "r", encoding="utf-8")

    #Abrir ficheiro temporario para ler
    Ficheiro_Escrever = open("Temp.txt", "w", encoding="utf-8")

    while True:
        #Ler um produto
        Linha = Ficheiro_Ler.readline()
        if not Linha:
            break

        #Verificar se é o produto a editar
        Partes = Linha.split("-")
        if Nome == Partes[0].strip():
            #Se sim ler os novos dados
            Novo_Nome = input("Novo nome para o produto: ")
            Novo_Preco = float(input("Novo preço do porduto: "))
            Linha = f"{Novo_Nome} - {Novo_Preco} \n"
        
        #Gravar no ficheiro temporario
        Ficheiro_Escrever.write(Linha)

    #Fechar os 2 ficheiros
    Ficheiro_Escrever.close()
    Ficheiro_Ler.close()

    #Apagar o ficheiro
    os.remove(NOME_FICHEIRO)

    #Mudar o nome do ficheiro temporario para produtos
    os.rename("Temp.txt", NOME_FICHEIRO)
    print("Produto editado com sucesso! ")
    
def Apagar():
    #Verificar se o ficheiro existe
    if Ficheiro_Existe() == False:
        return

    #Ler o nome do produto a apagar
    Nome = input("Qual o produto a apagar? ")

    #Abrir o ficheiro dos produtos para ler
    Ficheiro_Ler      = open(NOME_FICHEIRO, "r", encoding="utf-8")

    #Abrir ficheiro temporario para ler
    Ficheiro_Escrever = open("Temp.txt", "w", encoding="utf-8")

    while True:
        #Ler um produto
        Linha = Ficheiro_Ler.readline()

        #EOF
        if not Linha:
            break

        #Verificar se é o produto a editar
        Partes = Linha.split("-")
        if Nome == Partes[0].strip():
            continue
        
        #Gravar no ficheiro temporario
        Ficheiro_Escrever.write(Linha)

    #Fechar os 2 ficheiros
    Ficheiro_Escrever.close()
    Ficheiro_Ler.close()

    #Apagar o ficheiro
    os.remove(NOME_FICHEIRO)

    #Mudar o nome do ficheiro temporario para produtos
    os.rename("Temp.txt", NOME_FICHEIRO)
    print("Produto apagado com sucesso! ")

def Ficheiro_Existe():
    if os.path.exists(NOME_FICHEIRO) == False:
        print("Ainda não tem produtos")
        return False

def Menu():
    Op = 0
    while True:
        print("1) Adicionar \n2) Ler \n3) Editar \n4) Apagar \n5) Sair")
        Op = int(input())

        if Op == 5:
            break
        
        if Op == 1:
            Adicionar()
        
        if Op == 2:
            print("")
            Ler()

        if Op == 3:
            Editar()

        if Op == 4:
            Apagar()

if __name__ == "__main__":
    Menu()