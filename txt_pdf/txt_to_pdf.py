#!/usr/bin/env python3.10

"""Script simples para criar um arquivo txt e um pdf juntando as anotações de aula que fiz em arquivo separados.
Espera que dentro de uma pasta existam subpastas, uma para cada aula, com um
arquivo 'anotacoes.txt'.
Executar na pasta da matéria, onde estão as subpastas com as aulas.
"""

# from fpdf import FPDF
import sys
import os
import re


if len(sys.argv[0:]) == 1:
    path = input(
        "Indique o caminho da pasta em que o script deve criar o sumário de aulas: "
    ).strip()
    if path == ".":
        path = os.path.abspath(".")

diretorio = [
    int(re.search("[0-9]+", item).group(0))
    for item in os.listdir(path)
    if "aula" in item
]
diretorio.sort()

arquivos = []
for d in diretorio:
    caminho = os.path.join(path, f"aula{d}")
    # breakpoint()
    # print(caminho)
    if os.path.isdir(caminho):
        arquivo = os.path.join(caminho, "anotacoes.txt")
        arquivos.append(arquivo)


anotacoes = []
for arq in arquivos:
    anotacoes.append(f"{'*' * 90}\n\n")
    with open(arq) as txt:
        for linha in txt:
            anotacoes.append(linha)
            if "aula" in linha.lower():
                anotacoes.append("\n\n")
        # print(aula)
# breakpoint()

form = []
nome_arquivo = os.path.basename(path)

with open(f"anotacoes_{nome_arquivo}.txt", "w") as arq:
    # cria um arquivo txt e armazena as linhas em uma lista para criar
    # um pdf
    for linha in anotacoes:
        # print(linha)
        # arq.write(linha)
        if linha != "\n\n":
            arq.write(linha)
            form.append(linha)

print("TXT CRIADO")
