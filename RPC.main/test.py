import subprocess as sp

import psutil


def kill(proc_pid):
    process = psutil.Process(proc_pid)
    for proc in process.children(recursive=True):
        proc.kill()
    process.kill()



try:
    proc.wait(timeout=3)
except sp.TimeoutExpired:
    kill(proc.pid)