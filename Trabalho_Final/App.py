"""
Trabalho final - Módulo 7
--------------------------
Um programa para gerir livros e empréstimos de uma biblioteca
Requesitos funcionais:
    - Gestão de Obras (CRUD)
    - Gestão de Visitas (CRUD)
    - Estatísticas (Valor total da coleção, Top items mais valiosos, Horarios mais visitados, ...)

Utilizar set:
    - caracterisicas (Tipos)

Para o módulo 7 foi acrescentado a materialização dos dados
"""
import Utils, Obras, Visitas, Estatisticas
import os

#Deve estar True quando em testes e False quando em produção
DEBUG = False

def MenuPrincipal():
    if DEBUG:
        Obras.Configurar()
        Visitas.Configurar()

    Obras.LerDados()
    Visitas.LerDados()

    while True:
        os.system("cls")
        Op = Utils.Menu(["Obras", "Visitas", "Estatísticas", "Sair"], "Menu Principal")
        print("")

        if Op == 0:
            Utils.F_Titulo("Criado por Dinis Sousa")
            os.system("cls")
            break
            
        if Op == 1:
            Obras.MenuObras()
        
        if Op == 2:
            Visitas.MenuVisitas()
        
        if Op == 3:
            Estatisticas.MenuEstatisticas()
        
        Obras.GuardarDados()
        Visitas.GuardarDados()

if __name__ == "__main__":
    MenuPrincipal()