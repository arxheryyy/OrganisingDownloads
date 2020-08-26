import os
import shutil
from os import walk
from datetime import datetime

DOWNLOADS = r'c:\Users\arxhe\Downloads'
whatsapp = r'c:\Users\arxhe\Downloads\WhatsAppSetup.exe'
fileName = []
paths = []
ctimes = []
dates = []
dirs = []
dirpaths = []
x = 0
for items in os.listdir(DOWNLOADS):
    if os.path.isfile(os.path.join(DOWNLOADS, items)):
        fileName.append(items)
        path = (os.path.abspath(os.path.join(DOWNLOADS, items)))
        paths.append(path)
        ctimes.append(os.path.getctime(paths[x]))
        dates.append(datetime.fromtimestamp(ctimes[x]).strftime('%Y-%m'))
        x = x+1
a = 0
for items in os.listdir(DOWNLOADS):
    if os.path.isdir(os.path.join(DOWNLOADS, items)):
        dirs.append(items)
        dirspath = (os.path.abspath(os.path.join(DOWNLOADS, items)))
        dirpaths.append(dirspath)
        a = a+1
z = 0
y = 0
for date in dates:
    if (dates[z] == dirs[y]):
        shutil.move(paths[dates[z].index], dirpaths[dirs[y].index])
        z = z+1
        y = y+1

    else:
        print("failed")
