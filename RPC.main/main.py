from asyncio.windows_events import NULL
from pypresence import Presence
import time
import random
import psutil
import pygetwindow as gw
import PySimpleGUI as sg
import RichPresence as rp
import subprocess as sp


def kill(proc_pid):
    process = psutil.Process(proc_pid)
    for proc in process.children(recursive=True):
        proc.kill()
    process.kill()
    
quotes = [
    'rp.update(details="Famous Quote:", status="If you can dream it, you can achieve it.")',
    'rp.update(details="Famous Quote:", status="Either write something worth reading or do something worth writing.")',
    'rp.update(details="Famous Quote:", status="You become what you believe.")',
    'rp.update(details="Famous Quote:", status="Fall seven times and stand up eight.")',
    'rp.update(details="Famous Quote:", status="The best revenge is massive success.")',
    'rp.update(details="Famous Quote:", status="Eighty percent of success is showing up.")',
    'rp.update(details="Famous Quote:", status="Life is what happens to you while you’re busy making other plans.")',
    'rp.update(details="Famous Quote:", status="Strive not to be a success, but rather to be of value.")',
    'rp.update(details="Famous Quote:", status="The best time to plant a tree was 20 years ago. The second best time is now.")',
    'rp.update(details="Famous Quote:", status="Everything you’ve ever wanted is on the other side of fear.")',
    'rp.update(details="Intesting Fact", status="I am the OFFICIAL FireBlaster69", largeImage="FireBlaster69")',
    'rp.update(details="Intresting Fact", status="your adopted")',
    'rp.update(details="Intresting Fact", status="ur mom gay")',
    'rp.update(details="Intresting Fact", status="u must be 13+ to use discord")',
    'rp.update(details="Intresting Fact", status="there is always someone better")',
    'rp.update(details="Teslas arent better for the enviroment", status="unless, they are charged using green energy")',
    'rp.update(details="Intresting Fact", status="100% Of people who breathe will die")',
    'rp.update(details="Intresting Fact", status="some things are better left alone")',
    'rp.update(details="Famous Quote:", status="Nothing is imposible until proven otherwise.")',
    'rp.update(details="Self Promotion:", status="https://www.youtube.com/channel/UCqkkByqL6hDobxNzbs7xUtQ")',
    'rp.update(details="Watch This Video:", status="https://www.youtube.com/watch?v=dQw4w9WgXcQ")',
    'rp.update(details="RAM: "+str(mem_per)+"%", status="CPU: "+str(cpu_per)+"%",largeImage=("gear"))',
    'rp.update(details="Looking at:", status=str(focusedWindow))'
]

layout = [
    [sg.Titlebar(title='Fireblaster69s RPC')],
    [sg.Text('Fireblaster69s Discord Rich Presence Controller')],
    [sg.Text('Details: *Optional*'), sg.InputText(key='details')],
    [sg.Text('Status: *Optional*'), sg.InputText(key='status')],
    [sg.Text('Command: *Optional*'), sg.InputText(key='cmd')],
    [sg.Button('at school')],
    [sg.Button('Apply'), sg.Button('Exit '), sg.Button('execute command'), sg.Button('Clear')]]

window = sg.Window('Fireblaster69s RPC', layout)


while True: 
    
    event, values = window.Read()
    
    if event == 'execute command':
        exec(str(values['cmd']))
    if event == 'Apply':
        rp.update(details=str(values['details']), status=str(values['status']))
    if event == 'at school':
        rp.update(details="Currently at school", status="will be home at 2:45PM EST")
           
    if event == 'Clear':
        rp.update(details='For some reason', status='the status isnt set to anything')
    
