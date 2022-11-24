#!/usr/bin/env python3.10

"""Script simples para criar um arquivo txt e um pdf juntando as anotações de aula que fiz em arquivo separados.
Espera que dentro de uma pasta existam subpastas, uma para cada aula, com um
arquivo 'anotacoes.txt'.
Executar na pasta da matéria, onde estão as subpastas com as aulas.
"""

#from fpdf import FPDF
import sys
import os
import math

if len(sys.argv[0:]) == 1:
    path = input(
        "Indique o caminho da pasta em que o script deve criar o sumário de aulas: "
    ).strip()
    if path == ".":
        path = os.path.abspath(".")

diretorio = [item for item in os.listdir(path)]
diretorio.sort()


#print(diretorio)

arquivos = []
for d in diretorio:
    caminho = os.path.join(path, d)
    #print(caminho)
    if os.path.isfile(caminho):
        continue
    arquivo = os.path.join(caminho, "anotacoes.txt")
    arquivos.append(arquivo)

#print(arquivos)

ordem_criacao = [(i, os.path.getctime(i)) for i in arquivos]
ordem_criacao = sorted(
    ordem_criacao,
    key=lambda t: t[1],
    reverse=False
)

#breakpoint()
anotacoes = []
for arq in ordem_criacao:
    anotacoes.append(f"{'*' * 90}\n\n")
    with open(arq[0]) as txt:
        for linha in txt:
            anotacoes.append(linha)
            if "aula" in linha.lower():
                anotacoes.append("\n\n")
        #print(aula)
#breakpoint()

form = []
with open("anotacoes_conteudo.txt", "w") as arq:
    # cria um arquivo txt e armazena as linhas em uma lista para criar
    # um pdf
    for linha in anotacoes:
        #print(linha)
        #arq.write(linha)
        if linha != "\n\n":
            arq.write(linha)
            form.append(linha)

print("TXT CRIADO")
