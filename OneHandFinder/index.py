import string
import random

notAccepted = ['p', 'i', 'u', 'y', 'h', 'j', 'k', 'l', 'ñ', 'n', 'm', 'b', 'o', 'ó', 'í', 'ú', 'á', 'é']

def check(word):
    for i in notAccepted:
        if i in word:
            return False
    
    return True

with open('wordlist.txt', 'r', encoding="utf8") as f:
    lines = f.readlines()

final = []

for j in lines:
    if check(j) == True and len(j) > 1:
        final.append(j)

for i in range(10):
    print(final[random.randint(1, len(final))])

print(len(final))
