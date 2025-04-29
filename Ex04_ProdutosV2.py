"""
Programa para adicionar o nome de um produto e o preço
"""
NOME_FICHEIRO = "Geral.txt"

Tamanho = int(input("Quantos produtos são? "))
def Adicionar():
    with open(NOME_FICHEIRO, "a", encoding="utf=8") as Ficheiro:
        L_Ultimo = Ficheiro.seek(-1)
        L_Ultimo = L_Ultimo.split("-")
        Ultimo = L_Ultimo[0]

        for i in range (Ultimo, Tamanho + Ultimo):
            Nome  = input(f"Nome do {i + 1}ª Produto: ").strip().capitalize()
            Preco = float(input(f"Preço do {i + 1}ª Produto: "))
            print("")
            Ficheiro.write(f"{i+1}- {Nome}: {Preco}")
            if i != Tamanho-1:
                Ficheiro.write("\n")

def Menu():
    Op = 0
    while True:
        print("1) Adicionar \n2) Ler \n3) Editar \n4) Apagar \n5) Sair \n")
        Op = int(input())

        if Op == 5:
            break
        
        if Op == 1:
            Adicionar()
        
        if Op == 2:
            Ler()

        if Op == 3:
            Editar()

        if Op == 4:
            Apagar()