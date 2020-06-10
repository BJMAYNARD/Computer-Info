#Computer Info

import os
import sys
import platform
import random
import subprocess
import pip

#Installing pip modules

def install_and_import(psutil,beautifultable):
    import importlib
    try:
        importlib.import_module(psutil)
        importlib.import_module(beautifultable)
    except ImportError:
        import pip
        pip.main(['install', psutil])
        pip.main(['install', beautifultable])
    finally:
        globals()[psutil] = importlib.import_module(psutil)
        globals()[beautifultable] = importlib.import_module(beautifultable)


install_and_import('psutil', 'beautifultable')

import psutil

#Gathering up the info of the computer

h=platform.platform(terse=True)
j=psutil.cpu_count(logical=True)
d=psutil.cpu_count(logical=False)
k=psutil.cpu_freq(percpu=False)
n=psutil.disk_usage('/')
m=psutil.virtual_memory()

#Displays info into a table

from beautifultable import BeautifulTable
table = BeautifulTable()
table.column_headers = ["Platform Info", "Logical CPU Count", "Virtual CPU Count", "CPU Frequency", "Disk Space Usage", "Memory Installed"]
table.append_row([(h), (j), (d), (k), (n), (m)])
print (table)


#Secondary processes - The "Hogs" Section
#Gathering up info for the "Hogs"

#Getting PIDS for Memory Hogs
mp=([(p.pid, p.info) for p in sorted(psutil.process_iter(attrs=['name', 'memory_percent']), key=lambda p: p.info['memory_percent'])][-5:])

#Getting PIDS for CPU % Usage
cu=([(p.pid, p.info) for p in sorted(psutil.process_iter(attrs=['name', 'cpu_percent']), key=lambda p: p.info['cpu_percent'])][-5:])

#Displays the Hogs in a Nice Table

from beautifultable import BeautifulTable
table = BeautifulTable()
table.column_headers = ["Memory Percentage Hogs", "CPU Percentage Hogs"]
table.append_row([(mp), (cu)])

print (table)
