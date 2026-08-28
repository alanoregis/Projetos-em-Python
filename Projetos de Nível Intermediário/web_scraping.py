from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time
import re


class WebScraping:
    def __init__(self, url):
        self.url = url
        self.soup = self.get_html()

    def get_html(self):
        options = Options()
        options.add_argument("--headless=new")  # roda sem abrir janela
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36")

        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=options)

        driver.get(self.url)
        time.sleep(5)  # espera o JS renderizar os cards

        html = driver.page_source
        driver.quit()

        soup = BeautifulSoup(html, "html.parser")
        return soup

    def get_rooms(self):
        cards = self.soup.find_all("div", class_="c965t3n atm_9s_11p5wf0 atm_dz_1osqo2v dir dir-ltr")

        resultados = []
        for card in cards:
            nome_tag = card.find(attrs={"data-testid": "listing-card-name"})
            titulo_tag = card.find(attrs={"data-testid": "listing-card-title"})
            preco_tag = card.find(attrs={"data-testid": "price-availability-row"})

            nome = nome_tag.get_text(strip=True) if nome_tag else None
            titulo = titulo_tag.get_text(strip=True) if titulo_tag else None

            preco_original = None
            preco_final = None
            if preco_tag:
                texto_preco = preco_tag.get_text(" ", strip=True)
                texto_preco = texto_preco.replace("\xa0", " ")  # normaliza o espaço

                # remove a parte da parcela (ex: "6x R$ 23") antes de extrair os valores
                texto_preco = re.sub(r"\d+x\s*R\$\s?[\d.,]+", "", texto_preco)

                valores = re.findall(r"R\$\s?[\d.,]+", texto_preco)
                valores_unicos = list(dict.fromkeys(valores))

                if len(valores_unicos) >= 2:
                    preco_original = valores_unicos[0]
                    preco_final = valores_unicos[1]
                elif len(valores_unicos) == 1:
                    preco_final = valores_unicos[0]

            resultados.append({
                "titulo": titulo,
                "nome": nome,
                "preco_original": preco_original,
                "preco_final": preco_final
            })

        return resultados