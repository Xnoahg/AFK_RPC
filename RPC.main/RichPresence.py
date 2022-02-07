from asyncio.windows_events import NULL
from pypresence import Presence
import time
import random
import psutil
import pygetwindow as gw

client_id = '885935483933306901'  # Put your Client ID here, this is a fake ID
RPC = Presence(client_id)  # Initialize the Presence class
RPC.connect()  # Start the handshake loop
cpu_per = round(psutil.cpu_percent(),1) 
mem = psutil.virtual_memory()
mem_per = round(psutil.virtual_memory().percent,1)

focusedWindow = gw.getActiveWindow().title
if focusedWindow == "": 
    focusedWindow = "Nothing" 
elif focusedWindow == " ": 
   focusedWindow = "Nothing"
else: 
   focusedWindow = gw.getActiveWindow().title

def cmd(command):
    exec(command)

def update(details = "", status = "", largeImage = " ", smallImage = " "):

    if details == "":
        details = "---~==~==~---"
    
    if status == "":
        status = "---~==~==~---"
    
    
    if len(status) < 2:
        status = "---~==~==~---"
        print('to short to display')
    elif len(status) > 128:
        status = "to long to display"
        print('status cant be greater than 128 in length')
    
    if len(details) < 2:
        details = "to short to display"
        print('details cant be less than 2 in length')
    elif len(details) > 128:
        details = "to long to display"
        print('details cant be greater than 128 in length')
    
    if details == "---~==~==~---":
        if status == "---~==~==~---":
            details = "For some reason"
            status = "the status isnt set to anything"
    
    RPC.update(details=details, state=status, large_image=largeImage, small_image=smallImage)
