import winsound
import requests
import re
import time
import json

def get_floor(collection_name):
    url = f"https://api-mainnet.magiceden.dev/v2/collections/{collection_name}"
    payload = {}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload, allow_redirects=False)
    string = response.text
    dict = json.loads(string)
    global floor_price
    floor_price = int(dict["floorPrice"])* (10 ** -9)
    return floor_price

def beep():
    print("Processing ... ")
    while floor_price > floor_min:
        get_floor(collection_name)
        time.sleep(0.5)
    while True:
        print("Price is down..." + str(floor_price))
        winsound.Beep(440, 900)

collection_name = input("Creat a price alert! \n collection name: ")
floor_min = float(input("When floor price falls bellow: "))

get_floor(collection_name)
beep()

