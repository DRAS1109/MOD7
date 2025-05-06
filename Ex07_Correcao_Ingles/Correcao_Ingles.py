"""
Programa para verificar uma frase utilizando um ficheiro de texto como dicionário
"""
import os
 
NOME_FICHEIRO = "words.txt"
 
def FicheiroExiste():
    if os.path.exists(NOME_FICHEIRO) == False:
        print("Dicionário não existe.")
        return False
    return True
 
def LerFrase():
    Frase = input("Introduza uma frase:")
    Frase = Frase.strip().lower()
    return Frase.split(" ")
 
def LerFicheiro():
    """Função para ler todas as linhas de um ficheiro de texto e devolver uma lista"""
    with open(NOME_FICHEIRO,"r",encoding="UTF-8") as ficheiro:
        Linhas = ficheiro.readlines()

    #converter todas as palavras do dicionário para minusculas
    for i in range(len(Linhas)):
        Linhas[i] = Linhas[i].lower()
    return Linhas
 
def Verificar(palavras,Dicionario):
    """Função recebe as palavras a verificar e a lista de palavras do dicionário. Mostra as palavras
    que não existem no dicionário ou uma mensangem de não existencia de erros."""
    Erro = False
    for Palavra in palavras:
        if Palavra+"\n" not in Dicionario:
            print(f"A palavra {Palavra} não existe ou está errada.")
            Erro = True

    if Erro == False:
        print("A frase não tem erros.")
 
def main():
    if FicheiroExiste() == False:
        print("Ficheiro com o dicionário não encontrado.")
        return
    
    Palavras = LerFrase()
    Dicionario = LerFicheiro()
    Verificar(Palavras,Dicionario)
 
if __name__=="__main__":
    main()