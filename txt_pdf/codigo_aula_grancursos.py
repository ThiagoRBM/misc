import cv2
from pytesseract import pytesseract
from PIL import Image
import sys
import os
import glob
import re

"""Script que fiz para extrair automaticamente o código da aula do grancursos,
depois inclui como uma função no script txt_to_pdf.py, para incluir já no txt
o código
"""

if len(sys.argv[0:]) == 1:
    path = input(
        "Indique o caminho da pasta em que o script deve criar o sumário de aulas: "
    ).strip()
    path = os.path.join(path, "")
    if path == ".":
        path = os.path.abspath(".")


dirs = [
    f"aula{i}"
    for i in range(1, len([d for d in os.listdir(path) if "." not in d]) + 1)
]

imgs = glob.glob(f"{path}{dirs[0]}/*.png")

img_path = [img for img in imgs if bool(re.search("_1_.png", img))]

imagem = cv2.imread(img_path[0])

gray = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

crop = gray[850:, 150:316]

thresh = 45

im_bool = crop > thresh

maxval = 255

im_bin = (crop > thresh) * maxval

cv2.imwrite("teste6.jpg", im_bin)

txt = pytesseract.image_to_string(Image.open("teste6.jpg"))

codigo = re.search("(?<=\\: ).*?(?=\\))", txt).group(0).strip()

# print(codigo)

breakpoint()
