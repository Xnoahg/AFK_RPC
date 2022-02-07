# this MODULE sets the rich presence to whatever it needs to be set to 
# -~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~ 
# to use this module; presence.update(details, status, largeImage, smallImage)
# note: small and large image aren't required
# -~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~ 
# for more customization running straight up commands is a thing; presence.cmd()
# -~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~ 

from pypresence import Presence
from asyncio.windows_events import NULL

# setting up the rich presence display
client_id = '885935483933306901'
RPC = Presence(client_id)
RPC.connect()

def cmd(command):
    exec(command)

def update(details = " ", status = " ", largeImage = " ", smallImage = " "):
    # check to see if details is blank
    if details == "":
        details = "---~==~==~---"
    # check to see if status is blank
    if status == "":
        status = "---~==~==~---"
    
        # check to see if nothing is set at all
    if details == "---~==~==~---":
        if status == "---~==~==~---":
            details = "For some reason"
            status = "the status isnt set to anything"
    
    # check to see if length is to high or low to display
    if len(status) < 2:
        status = "to short to display"
        print('to short to display')
    elif len(status) > 128:
        status = "to long to display"
        print('status cant be greater than 128 in length')
    
    # check to see if length is to high or low to display
    if len(details) < 2:
        details = "to short to display"
        print('details cant be less than 2 in length')
    elif len(details) > 128:
        details = "to long to display"
        print('details cant be greater than 128 in length')
    
    RPC.update(details=details, state=status, large_image=largeImage, small_image=smallImage)