from tkinter import *
import datetime
import requests
import time
import json

def btstamp():
    bitstamptick = requests.get('https://bitstamp.net/api/ticker')
    return bitstamptick.json()['last']

def btstampheight():
    height = requests.get('https://mempool.space/api/blocks/tip/height')
    return height.json()#['height']



def loop():
  today = datetime.datetime.now()
  today1 = today.strftime("%c")

  btstampUSDLive = float(btstamp())

  blockheightlive = int(btstampheight())
  
  datelabel = Label(root, text = (today1)).grid(row = 0, column = 1)
  pricelabel = Label(root, text = (btstampUSDLive)).grid(row = 1, column = 1)
  bhlabel = Label(root, text = (blockheightlive)).grid(row = 2, column = 1)


root = Tk()
root.geometry("510x120")
root.title("Poor Mans BloCk clOcK")

lab1 = Label(root, text = "Date").grid(row = 0, column = 0)
lab2 = Label(root, text = "Price").grid(row = 1, column = 0)
lab3 = Label(root, text = "BlockHeight").grid(row = 2, column = 0)

but1 = Button(root, text = "Update", heigh =2, width = 30, command = loop).grid(row = 3, column =0)

root.mainloop()