import main as rpc
import time

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
print('setting status to indicate that you are no longer afk')
rpc.update('No Longer AFK', 'your welcome for this info')
stop()
exit()
