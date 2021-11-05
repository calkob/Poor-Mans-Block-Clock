from tkinter import *
import datetime
import requests
import time
import json



#Gets Price
def btstamp():
    bitstamptick = requests.get('https://bitstamp.net/api/ticker')
    return bitstamptick.json()['last']

#Gets Block Height
def btstampheight():
    height = requests.get('https://mempool.space/api/blocks/tip/height')
    return height.json()#['height']

#This function calls/displays Time, Price and blockheight
def loop():
  today = datetime.datetime.now()
  today1 = today.strftime("%c")

  btstampUSDLive = float(btstamp())

  decimal = "{:.2f}".format(btstampUSDLive)

  blockheightlive = int(btstampheight())
  
  datelabel = Label(root, text = (today1), font= ("Helvetica", 11, "bold")).grid(row = 0, column = 1)
  pricelabel = Label(root, text = (decimal), font= ("Helvetica", 16, "bold")).grid(row = 1, column = 1)
  bhlabel = Label(root, text = (blockheightlive), font= ("Helvetica", 17, "bold")).grid(row = 2, column = 1)



#Main GUI Window
root = Tk()
root.geometry("750x160")
root.title(":)")

count =0
def counter():
  global count
  while(count<100000):     
    lab1 = Label(root, text = "Date", font= ("Helvetica", 12, "bold")).grid(row = 0, column = 0)
    lab2 = Label(root, text = "Price", font= ("Helvetica", 12, "bold")).grid(row = 1, column = 0)
    lab3 = Label(root, text = "BlockHeight", font= ("Helvetica", 12, "bold")).grid(row = 2, column = 0)

#Button updates price manually
    but1 = Button(root, text = "Update",font= ("Helvetica", 17, "bold"), height =2, width = 30, command = loop).grid(row = 3, column =0)

    loop()
    root.update() # allow window to catch up
    time.sleep(60)
    count += 1

count = counter()
root.mainloop()