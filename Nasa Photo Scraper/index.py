import httplib2
from bs4 import BeautifulSoup, SoupStrainer
import requests
import time

import warnings
warnings.filterwarnings("ignore", category=UserWarning, module='bs4')

http = httplib2.Http()
status, response = http.request('https://apod.nasa.gov/apod/archivepixFull.html')

def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\r"):
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print(f'\r|{bar}| {percent}% {suffix}', end = printEnd)
    # Print New Line on Complete
    if iteration == total: 
        print()

beforeTime = int(round(time.time()))

listOfHtmls = []
for link in BeautifulSoup(response, features="html.parser", parse_only=SoupStrainer('a')):
    if link.has_attr('href') and link['href'][0] == 'a' and link['href'][1] == 'p' and len(listOfHtmls) < 100:
        listOfHtmls.append(link['href'])
    
    elif len(listOfHtmls) > 5:
        break

print(len(listOfHtmls))

listOfImages = []
for j in listOfHtmls:
    status, response = http.request('https://apod.nasa.gov/apod/'+j)

    for link in BeautifulSoup(response, features="html.parser", parse_only=SoupStrainer('img')):
        if link.has_attr('src'):
            listOfImages.append('https://apod.nasa.gov/apod/'+link['src'])

counter = 0
for k in listOfImages:
    img_data = requests.get(k).content
    with open('Images/'+str(counter)+'.jpg', 'wb') as handler:
        handler.write(img_data)
    
    counter+=1
    print(printProgressBar(counter, len(listOfImages)))

afterTime = int(round(time.time()))

print()
print()

print(f'Time elapsed: {afterTime - beforeTime} seconds.')
# status, response = http.request('https://apod.nasa.gov/apod/'+listofHtmls[0])