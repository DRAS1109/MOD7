"""
Trabalho Modelo - Módulo 7
--------------------------
Um programa para gerir livros e empréstimos de uma biblioteca
Requesitos funcionais:
    - Gestão Livros (CRUD)
    - Gestão leitores (CRUD)
    - Empréstimos e devoluções
    - Estatísticas (Empréstimos em atraso, Top Livros, Top Mês, Top Leitores, ...)

Para o módulo 7 foi acrescentado a materialização dos dados

"""
import Utils, Livros, Leitores, Emprestimos, Estatisticas
import os

#Deve estar True quando em testes e False quando em produção
DEBUG = False

def MenuPrincipal():
    if DEBUG:
        Livros.Configurar()
        Leitores.Configurar()
        
    #Ler Dasdos dos Ficheiros
    Livros.LerDados()
    Leitores.LerDados()
    Emprestimos.LerDados()

    Op = 0
    while Op != 5:
        os.system("cls")
        Op = Utils.Menu(["Livros", "Leitores", "Empréstimos / Devoluções", "Estatísticas", "Sair"], "Menu Principal")
        print("")

        if Op == 5:
            break

        if Op == 1:
            Livros.MenuLivros()

        if Op == 2:
            Leitores.MenuLeitores()
        
        if Op == 3:
            Emprestimos.MenuEmprestimos()
        
        if Op == 4:
            Estatisticas.MenuEstatisticas()

    #Guardar os dados
    Livros.GuardarDados()
    Leitores.GuardarDados()
    Emprestimos.GuardarDados()

if __name__ == "__main__":
    MenuPrincipal()