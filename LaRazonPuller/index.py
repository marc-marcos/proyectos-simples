from laRazon import getLaRazonNews
import time, json

# d = {localtime:getLaRazonNews(15)}

while True:
    news = getLaRazonNews(15)
    localtime = time.asctime( time.localtime(time.time()) )

    f = open('data.json', encoding="utf-8")
    data = json.load(f)
    f.close()

    data[str(localtime)] = news

    out = json.dumps(data)

    with open('data.json', 'a',encoding="utf-8") as file:
        file.write(out)

    print(f"Se han escrito datos a fecha de {localtime}")

    time.sleep(240)


