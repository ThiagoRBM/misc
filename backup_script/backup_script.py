import argparse
import os
import re
import hashlib
from pathlib import Path
import shutil
from datetime import datetime
import csv

now = datetime.now()
dt_string = now.strftime("%d/%m/%Y_%H:%M:%S")

parser = argparse.ArgumentParser()

parser.add_argument(
    "-f",
    "--from",
    help="Pasta de onde os arquivo serao copiados",
    required=True,
    type=str,
)
parser.add_argument(
    "-t",
    "--to",
    help="""\
    Pasta para onde os arquivo serao copiados.\n
        Se deixado em branco, irá para '/media/thiagorbm/hd_1_tera/backups_ssd/'
    """,
    required=False,
    type=str,
    default="/media/thiagorbm/hd_1_tera/backups_ssd/",
)

args = vars(parser.parse_args())

folder_from = args["from"]
folder_from_basename = os.path.basename(
    folder_from
)  # extrai o último nome do caminho

## pega os nomes dos arquivos da pasta que será copiada em files_from
## pega os os caminho para os arquivos em files_from_root
files_from = []
files_from_root = []
files_from_path = []
for root, dirs, files in os.walk(folder_from):
    for file in files:
        files_from.append(file)
        files_from_root.append(root)
        files_from_path.append(os.path.join(root, file))

folder_to = args["to"]
folder_to_basename = os.path.basename(folder_to)

## se o diretório não existir, cria ele
if folder_to_basename is not folder_from_basename:
    try:
        if not bool(re.search(f"(?<={folder_from_basename}/).*$", folder_to)):
            folder_to = os.path.join(folder_to, folder_from_basename)
            os.mkdir(folder_to)
    except FileExistsError:
        print(
            f"Pasta '{os.path.join(folder_to, folder_from_basename)}' existe, copiando para lá"
        )
        pass

# removendo as instâncias dos diretórios "from" da lista
files_from_root = [i for i in files_from_root if i != folder_from]

path_to = []
for caminho in set(files_from_root):
    # criando as subpastas
    if not os.path.isfile(caminho):
        # print(caminho)
        path_basename_on = re.search(
            f"(?<={folder_from_basename}/).*$", caminho
        ).group(0)
        path_backup = os.path.join(folder_to, path_basename_on)
        path_to.append(path_backup)

        if not os.path.exists(path_backup):
            # se subpasta não existir, cria uma subpasta
            os.makedirs(path_backup)

files_from_path.sort()
path_to.sort()
for i, file in enumerate(files_from_path):
    if os.path.isfile(file):
        # p_to = [i for i in ls_folder_to if bool(re.search(os.path.dirname(file), i)) == True][0]
        # breakpoint()
        p_to = file.replace(folder_from, folder_to)
        print(p_to)
        shutil.copy(file, os.path.dirname(p_to))

    if i == len(files_from_path) - 1:
        bckp = {"backup feito em": dt_string}
        with open(
            os.path.join(folder_from, "backup_datas.csv"), "a", newline="\n"
        ) as f_:
            writer = csv.DictWriter(f_, fieldnames=["backup feito em"])
            writer.writerow(bckp)

        print(f"\n\nbackup feito")
