# wtf else would this do
from asyncio.windows_events import NULL
import main as rpc
import pygetwindow as gw
import PySimpleGUI as sg
import time
import random
import psutil

# a bunch of data for the presence(s)

quotes = [
    'rpc.update(details="Famous Quote:", status="If you can dream it, you can achieve it.")',
    'rpc.update(details="Famous Quote:", status="Either write something worth reading or do something worth writing.")',
    'rpc.update(details="Famous Quote:", status="You become what you believe.")',
    'rpc.update(details="Famous Quote:", status="Fall seven times and stand up eight.")',
    'rpc.update(details="Famous Quote:", status="The best revenge is massive success.")',
    'rpc.update(details="Famous Quote:", status="Eighty percent of success is showing up.")',
    'rpc.update(details="Famous Quote:", status="Life is what happens to you while you’re busy making other plans.")',
    'rpc.update(details="Famous Quote:", status="Strive not to be a success, but rather to be of value.")',
    'rpc.update(details="Famous Quote:", status="The best time to plant a tree was 20 years ago. The second best time is now.")',
    'rpc.update(details="Famous Quote:", status="Everything you’ve ever wanted is on the other side of fear.")',
    'rpc.update(details="Intesting Fact", status="I am the OFFICIAL FireBlaster69", largeImage="FireBlaster69")',
    'rpc.update(details="Intresting Fact", status="your adopted")',
    'rpc.update(details="Intresting Fact", status="ur mom gay")',
    'rpc.update(details="Intresting Fact", status="u must be 13+ to use discord")',
    'rpc.update(details="Intresting Fact", status="there is always someone better")',
    'rpc.update(details="Teslas arent better for the enviroment", status="unless, they are charged using green energy")',
    'rpc.update(details="Intresting Fact", status="100% Of people who breathe will die")',
    'rpc.update(details="Intresting Fact", status="some things are better left alone")',
    'rpc.update(details="Famous Quote:", status="Nothing is imposible until proven otherwise.")',
    'rpc.update(details="Self Promotion:", status="https://www.youtube.com/channel/UCqkkByqL6hDobxNzbs7xUtQ")',
    'rpc.update(details="Watch This Video:", status="https://www.youtube.com/watch?v=dQw4w9WgXcQ")',
    'rpc.update(details="RAM: "+str(mem_per)+"%", status="CPU: "+str(cpu_per)+"%",largeImage=("gear"))',
    'rpc.update(details="Looking at:", status=str(focusedWindow))']

# GUI layout and setup

layout = [
    [sg.Titlebar(title='Fireblaster69s RPC')],
    [sg.Text('Fireblaster69s Discord Rich Presence Controller')],
    [sg.Text('Details: *Optional*'), sg.InputText(key='details')],
    [sg.Text('Status: *Optional*'), sg.InputText(key='status')],
    [sg.Text('Command: *Optional*'), sg.InputText(key='cmd')],
    [sg.Button('School'), sg.Button('Quotes'), sg.Button('Computer Stats'), sg.Button('Focused Windows')],
    [sg.Button('Apply'), sg.Button('Clear'), sg.Button('Exit'), sg.Button('execute command')]]

window = sg.Window('My Title', layout, finalize=True)
window.bring_to_front()
# window main loop 
while True: 
    event, values = window.Read()
    window.force_focus()
    if event == 'School':
        rpc.update(details="Currently at school", status="will be home at 2:45PM EST")
    
    if event == 'Quotes':
        print('Not Implemented')
    
    if event == 'Computer Stats':
        print('Not Implemented')
    
    if event == 'Focused Window':
        print('Not Implemented')
    
    if event == 'Apply':
        rpc.update(details=str(values['details']), status=str(values['status']))
    
    if event == 'Clear':
        rpc.clear()
    if event == sg.WIN_CLOSED or event == 'Exit':
        rpc.stop()
        break
    
    if event == 'execute command':
        exec(str(values['cmd']))

window.close()


