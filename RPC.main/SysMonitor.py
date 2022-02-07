from pypresence import Presence
import psutil
import RichPresence as rp
import time
while True: 
    cpu_per = round(psutil.cpu_percent(),1) 
    mem = psutil.virtual_memory()
    mem_per = round(psutil.virtual_memory().percent,1)
    
    rp.update(details="RAM: "+str(mem_per)+"%", status="CPU: "+str(cpu_per)+"%", largeImage=("gear"))
    print("Details = " + "RAM: "+str(mem_per)+"%")
    print("Status  = " + "CPU: "+str(cpu_per)+"%")
    print("Large Image Set: Image = " + "gear")
    time.sleep(10)
exit()