#!/usr/bin/env python3

import os
import sys
import subprocess
import math
import argparse
"""Script simples que corta um video em pedaços. Os cortes sao salvos na mesma pasta do arquivo mantendo o nome original com o sufixo "_corte_n_"

exemplo de uso: ./corte_video.py --arquivo video.mp4 --cortes 4

"""

parser = argparse.ArgumentParser()
parser.add_argument('--arquivo',
                    help='Caminho para o arquivo a ser cortado.',
                    required=True)
parser.add_argument('--cortes',
                    help='Quantidade de cortas a ser gerada.',
                    type=int,
                    required=True)

args = parser.parse_args()

#breakpoint()

## obtem a duracao do video passado
duracao_video = float(
    subprocess.check_output(
        f"ffprobe -i {args.arquivo} -show_entries format=duration -v quiet -of csv='p=0'",
        shell=True))

# calcula quantos pedacos serao gerados
duracao_cortes = math.ceil(duracao_video / args.cortes)

# informa a duracao dos pedacos
print(f"Cada pedaço ficará com {duracao_cortes} segundos.")
if input("Aperte <enter> para continuar ou qualquer tecla para sair.") != "":
    sys.exit(0)

#breakpoint()

n = 0
for corte in range(args.cortes):
    nome_corte = f"{args.arquivo.split('.')[0]}_corte_{int(corte)+1}_"
    os.system(
        f"ffmpeg -i {args.arquivo} -y -ss {n} -t {duracao_cortes} -c:v copy -c:a copy {nome_corte}.mp4"
    )
    n = n + duracao_cortes
