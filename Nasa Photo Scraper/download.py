import requests
from os.path import basename
from bs4 import BeautifulSoup, SoupStrainer


r = requests.get("https://apod.nasa.gov/apod/image/rhea_vg1.gif")
soup = BeautifulSoup(r.content)

for link in soup.select("img"):
    with open(basename(link["src"]), "wb") as f:
        f.write(requests.get(link["src"]).content)