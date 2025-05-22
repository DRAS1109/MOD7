"""Modulo para estatisticas 
- Raridade mais comum
- Preço da coleção
- Obra mais antiga
- Todos os autores
- Horario mais visitado
"""
import Utils, Obras, Visitas, Visitantes, datetime

def MenuVisitantes():
    """Menu para visitas"""

    Existe_Obras = Obras.LerBinario()
    Existe_Visitas = Visitas.LerBinario()
    Existe_Visitantes = Visitantes.LerCSV()

    while True:
        Op = Utils.Menu(["Raridades", "Valor da coleção","Obra mais antiga", "Todos os autores", "Visitas Futuras", "Voltar"], "Menu de estatisticas")
        print("")

        if Op == 0:
            break

        elif Op == 1 :
            E_Raridades()

        elif Op == 2:
            E_Preco()

        elif Op == 3:
            E_Antiga()

        elif Op == 4:
            E_Autores()
        
        elif Op == 5:
            Visitas_Futuras()
    

def E_Raridades():
    if len(Obras.Colecao) < 1:
        print("Não tem obras na sua coleção")
        return
    
    Raridades = {"Comum": 0, "Raro": 0, "Epico": 0, "Lendario": 0, "Mitico": 0}

    #Contar quantas raridades tem a coleção
    for Obra in Obras.Colecao:
        Raridades[Obra["Raridade"]] += 1

    #Encontrar o mais utilizado
    Maior = 0
    for Raridade in Raridades:
        if Raridades[Raridade] > Maior:
            Maior = Raridades[Raridade]
            R_Maior = Raridade

    print(f"A raridade mais comum da coleção é: {R_Maior}, presente em {Maior} Obras")

def E_Preco():
    #Preço total da coleção
    Preco_Total = 0
    for Obra in Obras.Colecao:
        Preco_Total += Obra["Preco Atual"]

    print(f"A coleção tem um preço estimado de {Preco_Total}")

def E_Antiga():
    if len(Obras.Colecao) < 1:
        print("Não tem obras na sua coleção")
        return

    # Encontrar a obra mais antiga
    Antiga = Obras.Colecao[0]["Ano"]
    for Obra in Obras.Colecao:
        if Obra["Ano"] < Antiga:
            Antiga = Obra["Ano"]

    # Guardar todas as obras com esse ano
    L_O_Antiga = []
    for Obra in Obras.Colecao:
        if Obra["Ano"] == Antiga:
            L_O_Antiga.append(Obra)

    print(f"\nObras mais antigas (ano {Antiga}):")
    Obras.Listar(L_O_Antiga, "Obras mais Antigas", {"Id": 0, "Tipo": 0, "Ano": 0, "Autor": 0, "Preco Atual": 0, "Raridade": 0, "Descricao": 0})

def E_Autores():
    if len(Obras.Colecao) < 1:
        print("Não tem obras na sua coleção")
        return
    
    Autores = {Obras.Colecao[0]["Autor"]}
    for Obra in Obras.Colecao:
        Autores.add(Obra["Autor"])

    print("Autores de todas as obras da coleção:")
    for Autor in Autores:
        print(f" - {Autor}")

def Visitas_Futuras():
    Total = 0
    for Visitas in Visitantes.Datas.values():
            for Grupos in Visitas.values():
                Total += sum(Grupos.values())

    print(f"Total de pessoas com visitas futuras agendadas: {Total}")