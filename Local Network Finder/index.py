import subprocess
import json
import sys
from termcolor import cprint

def getDevices():
    count = 0
    out_lst = []
    lst = subprocess.check_output(['sudo', 'arp-scan', '--localnet']).decode('utf-8').split("\n")

    for i in lst:
        if (count >= 2 and count < len(lst)-4): 
            lst2 = i.split("\t")
            host_name = lst2[2]
            host_mac = lst2[1]

            out_lst.append([host_name, host_mac])

        count += 1
    
    return out_lst

def addTrustedDevice(device_mac, trusted_devices_file):
    with open(trusted_devices_file, 'r') as file:
        data = json.load(file)
    
    data.append(device_mac)

    with open(trusted_devices_file, 'w') as file:
        json.dump(data, file)

def listDevicesOnScreen(out_lst):
    with open("trusted.json", 'r') as file:
        trusted = json.load(file)

    with open("black_list.json", 'r') as file:
        black_list = json.load(file)

    for i in out_lst:
        if (i[1] in trusted): 
            cprint(f"{i[0]} ---- MAC address:   {i[1]}", "green")

        elif (i[1] in black_list):
            cprint(f"{i[0]} ---- MAC address:   {i[1]}", "red")

        else:
            print(f"{i[0]} ---- MAC address:   {i[1]}")

while True:
    print("1. Listar los dispositivos")
    print("2. Añadir un dispositivo a la lista de confianza")
    print("3. Añadir un dispositivo a la lista negra")
    option = input("[1, 2] >>> ")

    devices_list = getDevices()

    if option == "1":
        print(listDevicesOnScreen(devices_list))
    
    if option == "2":
        print("Introduce la dirección MAC para añadir a la lista de confianza")
        mac_address = input(">>> ")
        addTrustedDevice(mac_address, "trusted.json")

    if option == "3":
        print("introduce la dirección MAC para añadir a la lista negra")
        mac_address = input(">>> ")
        addTrustedDevice(mac_address, "black_list.json")
