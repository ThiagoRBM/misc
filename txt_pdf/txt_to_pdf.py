#!/usr/bin/env python3.10

"""Script simples para criar um arquivo txt e um pdf juntando as anotações de aula que fiz em arquivo separados.
Espera que dentro de uma pasta existam subpastas, uma para cada aula, com um
arquivo 'anotacoes.txt'. 
Executar na pasta da matéria, onde estão as subpastas com as aulas.
"""

from fpdf import FPDF
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

anotacoes = []
for arq in arquivos:
    anotacoes.append(f"{'*' * 90}\n\n")
    with open(arq) as txt:
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
        if linha != "\n":
            arq.write(linha)
            form.append(linha)

# def quebra_linha(linha, caracteres):
# """Funcao que quebra as linhas do arquivo .txt na quantidade
# de caracteres especificada.
# Nao usei porque depois que a fiz, descobri que a lib fpdf
# tem a funcao fpdf.multi_cell que quebra as linhas automaticamente
# """
# tamanho = len(linha)
# #print(tamanho)
# cortes = math.ceil(tamanho / caracteres)
# n = 1
# quebra = ""
# pedacos = []
# inicio = 0
#
# for corte in range(0, cortes):
# #  calcula os cortes a serem feitos
# fim = inicio + caracteres
# pedacos.append([inicio, fim])
# inicio = fim
#
# quebras = []
# for pedaco in pedacos:
# #  cria a lista com os cortes
# inicio, fim = [*pedaco]
# split = linha[inicio:fim]
# quebras.append(split)
# return quebras

## loop para checar se a funcao funciona em todos os casos
# for i, linha in enumerate(form):
# print(linha)
# if len(linha) > 79:
# quebra_linha(linha, 79)
# print(i)
# print(linha)
# else:
# ...
# #print(i)
#breakpoint()

pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=11)

## LOOP para criar o pdf usando a funcao quebra_linha, que tinha feito
#  antes de descobri a funcao da lib fpdf
# for i, linha in enumerate(form):
# if len(linha) > 100:
# linha = quebra_linha(linha, 100)
# for item in linha:
# pdf.cell(1, 5, txt=item, ln=1)
# else:
# pdf.cell(1, 5, txt=linha, ln=1)

for linha in form:
    pdf.multi_cell(h=5.0, align='L', w=0, txt=linha, border=0)

print("PDF CRIADO")

pdf.output("anotacoes_conteudo.pdf")
