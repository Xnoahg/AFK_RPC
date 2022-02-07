# This MODULE is used to INTERFACE presence.py with all of it's components without causing problems

import presence as rp
import time

def update(details = " ", status = " ", largeImage = " ", smallImage = " "):
    while clearState == 0:
        rp.update(details = " ", status = " ", largeImage = " ", smallImage = " ")


# setting the clearState variable to 0 indicating NOT to clear the rich presence
clearState = 0



# main loop (updates the presence)
def update(details = " ", status = " ", largeImage = " ", smallImage = " "):
        rp.update(details, status, largeImage, smallImage)
        time.sleep(5)