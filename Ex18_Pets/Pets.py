"""
Pets.dat
Raça    String 30   30
Peso    Float       4
Género  String 1    1
Preço   Float       4
Total: 39 Bytes

Funções:
1. Adicionar
2. Listar Todos
3. Apagar
4. Editar
5. Sair
"""

import Utils
import os, struct

NOME_FICHEIRO = "Pets.dat"
TAMANHO_REGISTO = 39

def Menu():
    while True:
        Op = Utils.Menu(["Adicionar", "Listar", "Apagar", "Editar", "Sair"], "Menu de pets")
        if Op == 0:
            Resultado = Sair()
            if Resultado == "return":
                return
            
        if Op == 1:
            Adicionar()

        if Op == 2:
            Listar()

        if Op == 3:
            Apagar()

        if Op == 4:
            Editar()
     
def Adicionar():
    """Função para adicionar um pet"""
    #Ler os dados
    Raca = input("Qual a raça? ")
    Peso = Utils.Ler_Decimal("Qual o peso? ")
    Genero = Utils.Ler_Strings(1, "Qual o género ([F]emenino / [M]asculino)? ")
    Preco = Utils.Ler_Decimal("Qual o preço? ")

    Acao = "ab"
    if Existe() == False:
        Acao = "wb"
    
    #Adicionar ao ficheiro
    with open(NOME_FICHEIRO, Acao) as Ficheiro:
        #Raça
        Ficheiro.write(struct.pack("30s", Raca.encode("utf-8")))

        #Peso
        Ficheiro.write(struct.pack("f", Peso))

        #Género
        Ficheiro.write(struct.pack("1s", Genero.encode("utf-8").upper()))

        #Preço
        Ficheiro.write(struct.pack("f", Preco))

    print("Dados guardados com sucesso")

def Listar():
    """Função para listar todos os pets"""
    if Existe() == False:
        print("Ainda não tem dados")
        return
        
    with open(NOME_FICHEIRO, "rb") as Ficheiro:
        while True:
            #Ler os dados todos de uma vez só
            Dados_Binarios = Ficheiro.read(30)

            if not Dados_Binarios:
                break
                
            Dados = struct.unpack("30s", Dados_Binarios)
            Raca = Dados[0].decode("utf-8").rstrip("\x00")
            print("Raça:", Raca)

            #Ler os dados todos de uma vez só
            Dados_Binarios = Ficheiro.read(4)
            Dados = struct.unpack("f", Dados_Binarios)
            print("Peso:", round(Dados[0], 3))

            #Ler e mostrar os dados todos de uma vez só
            Dados_Binarios = Ficheiro.read(1)
            Dados = struct.unpack("1s", Dados_Binarios)
            Genero = Dados[0].decode("utf-8").rstrip("\x00")
            print("Género:", Genero)

            #Ler os dados todos de uma vez só
            Dados_Binarios = Ficheiro.read(4)
            Dados = struct.unpack("f", Dados_Binarios)
            print("Preço:", round(Dados[0], 3))

def Apagar():
    if Existe() == False:
        print("Ainda não tem dados")
        return

    with open(NOME_FICHEIRO, "rb") as F_Ler:
        #Criar um ficheiro temporário
        with open("Temp.bin", "wb") as F_Escrever:
            while True:
                #Ler os dados todos de uma vez só
                Raca_Binarios = F_Ler.read(30)

                if not Raca_Binarios:
                    break
                
                #ler um registo
                Peso_Binario = F_Ler.read(4)
                Genero_Binario = F_Ler.read(1)
                Preco_Binario = F_Ler.read(4)

                #Mostrar ao utilizador
                Raca = struct.unpack("30s", Raca_Binarios)
                print("Raça:", Raca[0].decode("utf-8").rstrip("\x00"))
                #se NÂO é para apagar gravar o ficheiro temp
                Op = input("Pretende apagar este animal? ")
                if Op not in ("sS"):
                    F_Escrever.write(Raca_Binarios)
                    F_Escrever.write(Peso_Binario)
                    F_Escrever.write(Genero_Binario)
                    F_Escrever.write(Preco_Binario)

    #apagar o ficheiro de dados
    os.remove(NOME_FICHEIRO)

    #Mudar o nome do ficheiro temporario
    os.rename("temp.bin", NOME_FICHEIRO)
    print("Animal removido com sucesso")

def Editar():
    if Existe() == False:
        print("Ainda não tem dados")
        return
    
    #Abrir o ficheiro para leitura e escrita
    with open(NOME_FICHEIRO, "rb+") as Ficheiro:
        while True:
            #Ler um registo
            Raca_Binario = Ficheiro.read(30)
            if not Raca_Binario:
                break
                    
            Peso_Binario = Ficheiro.read(4)
            Genero_Binario = Ficheiro.read(1)
            Preco_Binario = Ficheiro.read(4)
        
            #Mostrar ao utilizador
            Raca = struct.unpack("30s", Raca_Binario)[0]
            Raca = Raca.decode("utf-8").rstrip("\x00")
            Peso = struct.unpack("f", Peso_Binario)[0]
            Genero = struct.unpack("1s", Genero_Binario)[0]
            Genero = Genero.decode("utf-8").rstrip("\x00")
            Preco = struct.unpack("f", Preco_Binario)[0]

            print(f"{Raca} | {round(Peso,3)} | {Genero} | {round(Preco,3)}")
            Op = input("Pretende editar este animal [S]im / [N]ão?")

            #Perguntar se quer alterar
            if Op in "sS":
                Raca = input("Qual a raça? ")
                Peso = Utils.Ler_Decimal("Qual o peso? ")
                Genero = Utils.Ler_Strings(1, "Qual o género ([F]emenino / [M]asculino)? ")
                Preco = Utils.Ler_Decimal("Qual o preço? ")

                #Se alterar gravar novamente o mesmo registo
                Ficheiro.seek(-39, 1)
                Ficheiro.write(struct.pack("30s", Raca.encode("utf-8")  ))
                Ficheiro.write(struct.pack("f"  , Peso ))
                Ficheiro.write(struct.pack("1s" , Genero.encode("utf-8")))
                Ficheiro.write(struct.pack("f"  , Preco))

def Sair():
    """Função para sair do programa. Foi dificil..."""
    return "return"

def Existe():
    if os.path.exists(NOME_FICHEIRO):
        return True
    return False

if __name__ == "__main__":
    Menu()