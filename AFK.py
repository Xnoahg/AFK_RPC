import main as rpc
import time
clearState = 0

# this function SHOULD be called when clearing the rich presence. 
def clear():
    print('Clearing Current Rich Presence')
    rpc.update(details='Presence Service Offline', status='Clearing Rich Presence Display')
    clearState = 1

# this function SHOULD be called when stopping the rich presence. 
def stop():
    print('Stopping Rich Presence Service')
    clear()
    time.sleep(5)
while clearState == 0:
    print('updating status')
    print('updated')
    print('updating again in 5 seconds')
    rpc.update('Currently AFK', 'Fireblaster69 is Currently AFK')