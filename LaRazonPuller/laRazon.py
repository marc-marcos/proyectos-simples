from bs4 import BeautifulSoup
import requests

def getLaRazonNews(index):
    url = "https://www.larazon.es/"
    req = requests.get(url)

    soup = BeautifulSoup(req.text, "html.parser")

    t = soup.find_all("span")
    j = []

    for i in t:
        if "Anterior" in i or "Siguiente" in i or "Submenú" in i or "Menú" in i or "\xa0" in i:
            pass

        else:
            j.append(i.text)

    j.pop(0)
    j.pop(0)

    j = j[:index]

    return j
