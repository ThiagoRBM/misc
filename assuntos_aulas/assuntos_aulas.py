#!/usr/bin/env python3

import os
from os.path import isfile, exists
import re
import sys
"""Script simples que para cada pasta de um diretório vai até o arquivo
'anotacoes.txt' e pega o numero da Aula e o assunto dela.
Espera que dentro de uma pasta existam subpastas, uma para cada aula, com um
arquivo 'anotacoes.txt' dentro, com o assunto logo em seguida, na mesma linha.
Exemplo:
'aula 12 vedações'.
Script busca pela palavra 'aula' dentro do arquivo.
Salva um arquivo '.txt' na pasta "mãe" (a que foi passada na chamada)
Executar na pasta da matéria, onde estão as subpastas com as aulas

>>>
./assuntos_aulas.py/home/thiagorbm/Documents/concursoUnDF/grancursos/legislacaoServidores/

Caso o caminho da pasta "mãe" não seja passado será perguntado:
'Indique o caminho da pasta em que o script deve criar o sumário de aulas:'
E aí se passa o caminho da pasta onde as subpastas com as aulas estão.
"""

# path = "/home/thiagorbm/Documents/concursos/secretaria_economia/direito_adm"

if len(sys.argv[0:]) == 1:
    path = input(
        "Indique o caminho da pasta em que o script deve criar o sumário de aulas: "
    ).strip()
    if path == ".":
        path = os.path.abspath(".")

if exists(f"{path}/assuntos.txt"):
    open(f"{path}/assuntos.txt", 'w').close()

diretorio = [
    int(re.search("[0-9]+", item).group(0)) for item in os.listdir(path)
    if "aula" in item
]
diretorio.sort()

subdiretorios = []
for dir_ in diretorio:
    caminho = os.path.join(path, f"aula{dir_}")
    if os.path.isfile(caminho):
        continue
    #breakpoint()
    arquivos = [
        os.path.join(caminho, item) for item in os.listdir(caminho)
        if "anotacoes.txt" in item
    ]
    #print(arquivos[0])
    #print(arquivos)
    for anotacoes in arquivos:
        conteudo = []
        aula = re.search("aula[0-9]+", anotacoes).group(0)
        #print(aula)
        #breakpoint()
        with open(anotacoes) as anot:
            assunto = [
                linha.strip().lower().split("\n")
                for linha in anot.readlines()
                if re.match("aula", linha, re.IGNORECASE)
            ]
            try:
                conteudo.append(assunto[0][0])
            except IndexError:
                conteudo.append(aula)
        #print(conteudo)
        # conteudo.append([
        #     linha.strip().lower().split("\n")
        #     for linha in anot.readlines()
        #     if re.match("aula", linha, re.IGNORECASE)
        # ])
        with open(f"{path}/assuntos.txt", "a") as ass:
            for item in conteudo:
                ass.writelines(f"{item}\n")
print(f"arquivo salvo em {path}")
