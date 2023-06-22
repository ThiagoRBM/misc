import time
from pprint import pprint

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support import expected_conditions as EC

import os
import sys

##https://g1.globo.com/economia/agronegocios/globo-rural/noticia/2023/06/04/pesquisadores-estudam-cogumelos-desconhecidos-da-mata-atlantica-com-potencial-de-mercado.ghtml

caminho = os.path.dirname(os.path.abspath(__file__))

options = Options()
options.add_argument("-headless")

for i in range(1,151):

    urlpage = f"https://vod-tvg-df-04.video.globo.com/j/eyJhbGciOiJSUzUxMiIsImtpZCI6IjEiLCJ0eXAiOiJKV1QifQ.eyJjb3VudHJ5X2NvZGUiOiJCUiIsImRvbWFpbiI6InZvZC10dmctZGYtMDQudmlkZW8uZ2xvYm8uY29tIiwiZXhwIjoxNjg2MDg0NDQ3LCJpYXQiOjE2ODYwODE3MTIsImlzcyI6InBsYXliYWNrLWFwaS1wcm9kLWdjcCIsIm93bmVyIjoiIiwicGF0aCI6Ii9yMjQwXzcyMC92MC8yNS9iNS9hNS8xMTY3MDY2Nl9hNTBjYjdkYjAyYjM5ZWI1N2Q3YTAzZGZmN2UxY2E0YTQwZjgwNTRiLzExNjcwNjY2LWJQVTFqVi1tYW5pZmVzdC5pc20vMTE2NzA2NjYubTN1OCJ9.zgVIq6K1UzIB7VGEXNT1Uc3THm_KWgksMOs4MdJ_kc8iH46ynUelJdeS5Kp776DUqNvRI2Y9w_RoZYYP3Iy6iUl8emZTnQq21BzLHOPB7kPOqW2-dL7_2lKCuyfHsdS3swx-cMPrmTWlC8YlTSic1GaISwJbdqaoiytulJAmLvxncDdablhMMRBcKI8FCa6_N8eEkP238Tdcg3XObBpdKrZ4XmGli6Dy5TVCOI5qRJE0EEmhuvPnHQT-D1eHsB1bchfe-qJ554Ufdl_TwPw9B8XM-5BNtLsP8lyYUvvOC5lE1_m9YYgqCeSX4N_NTQ5SuDGKpXP9ScK1_eWqAWcbrg/r240_720/v0/25/b5/a5/11670666_a50cb7db02b39eb57d7a03dff7e1ca4a40f8054b/11670666-bPU1jV-manifest.ism/11670666-bPU1jV-manifest-audio_por=128002-video_por=750000-{i}.ts"

    print(f"baixando fatia: {i}\n")
    driver = webdriver.Firefox(options=options)

    time.sleep(1)
    driver.get(urlpage)
    # breakpoint()
    # with open(f"{caminho}/fatia_{i}.mp4", "wb") as video_file:
         # for chunk in video.iter_content(chunk_size=8192):
            # video_file.write(chunk)

    driver.quit()
