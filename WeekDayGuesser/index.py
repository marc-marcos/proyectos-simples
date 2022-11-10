# This project should provide the user with one date, formatted as 27/7/22 and also 27 July 20222.
# The script should also take in account if the user wants to be asked about the current year or about any year.
# The script should be able to grade the user input and correct it. It should also be able to time it.

import random
import time
from datetime import date

print("Cuántas fechas quieres que se te pregunte?[num]")
nFechas = int(input(">>> "))

print("Quieres que se te pregunte sólo sobre este año?[si/no]")
esteAno = input(">>> ")

def fromNumberToWeekday(num):
    switch = {0:'lunes', 1:'martes', 2:'miercoles', 3:'jueves', 4:'viernes',
            5:'sabado', 6:'domingo'}

    return switch.get(num, "invalid")

def fromWeekdayToNumber(weekday):
    switch = {'lunes':0, 'martes':1, 'miercoles':2, 'jueves':3, 'viernes':4,
            'sabado':5, 'domingo':6}

    return switch.get(weekday, "invalid")


start_dt = date.today().replace(day=1, month=1).toordinal()
end_dt = date.today().replace(day=31, month=12).toordinal()

dates = []
for i in range(nFechas):
    random_day = date.fromordinal(random.randint(start_dt, end_dt))
    weekday = random_day.weekday()
    dates.append([random_day, weekday])

estadisticas = {'aciertos':0, 'fallos':0}
timeBefore = time.time()
for i in dates:
    print(f"{i[0].day}/{i[0].month}/{i[0].year}")
    inp = input(">>> ")

    if inp == fromNumberToWeekday(i[1]):
        print("Correcto!")
        estadisticas['aciertos'] += 1

    else:
        print("Incorrecto!")
        estadisticas['fallos'] += 1

totalTime = time.time() - timeBefore
print()
print(f"Has acertado un {estadisticas['aciertos']/(estadisticas['aciertos']+estadisticas['fallos'])*100}% y has tardado {round(totalTime, 2)} segundos.")
