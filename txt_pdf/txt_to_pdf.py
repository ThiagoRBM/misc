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
import cv2
from pytesseract import pytesseract
from PIL import Image
import glob


def extract_code(path):
    """Funcao para extrair o codigo do print da aula do grancursos."""
    imgs = glob.glob(f"{path}/*.png")
    img_path = [img for img in imgs if bool(re.search("_1_.png", img))]
    imagem = cv2.imread(img_path[0])
    altura, largura, bandas = imagem.shape

    gray = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
    crop = gray[int(altura / 5 * 4) :, : int(largura / 4)]
    thresh = 40
    maxval = 255
    im_bin = (crop > thresh) * maxval
    # breakpoint()
    cv2.imwrite(os.path.join(path, "img.jpg"), im_bin)
    txt = pytesseract.image_to_string(
        Image.open(os.path.join(path, "img.jpg"))
    )

    try:
        codigo = re.search("(?<=\\: ).*?(?=\\))", txt).group(0).strip()

    except AttributeError:
        codigo = "sem codigo de aula"

    return codigo


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
    if d == 1:
        # breakpoint()
        codigo = extract_code(caminho)
        # print(codigo)
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
                anotacoes.append(f"Código da matéria: {codigo}\n\n")
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
