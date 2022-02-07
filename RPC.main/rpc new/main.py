# This MODULE is used to INTERFACE presence.py with all of it's components without causing problems

import presence as rp
import time

# setting the clearState variable to 0 indicating NOT to clear the rich presence
clearState = 0

# this function SHOULD be called when clearing the rich presence. 
def clear():
    print('Clearing Current Rich Presence')
    rp.update(details='Presence Service Offline', status='Clearing Rich Presence Display')
    clearState = 1

# this function SHOULD be called when stopping the rich presence. 
def stop():
    print('Stopping Rich Presence Service')
    clear()
    time.sleep(5)

# main loop (updates the presence)
while clearState == 0:
    rp.update()
    time.sleep(15)


