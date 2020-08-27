import os
import shutil
from os import walk
from datetime import datetime

DOWNLOADS = r'c:\Users\arxhe\Downloads'
file1 = r'c:\Users\arxhe\Downloads\2020-08'
fileName = []
paths = []
ctimes = []
dates = []
dirs = []
dirpaths = []
datetimes = []
monthstr = []
yearstr = []
daystr = []
year = []
day = []
month = []
x = 0
for items in os.listdir(DOWNLOADS):
    if os.path.isfile(os.path.join(DOWNLOADS, items)):
        fileName.append(items)
        path = (os.path.abspath(os.path.join(DOWNLOADS, items)))
        paths.append(path)
        ctimes.append(os.path.getctime(paths[x]))
        yearstr.append(datetime.fromtimestamp(ctimes[x]).strftime('%y'))
        year.append(int(yearstr[x]))
        monthstr.append(datetime.fromtimestamp(ctimes[x]).strftime('%m'))
        month.append(int(monthstr[x]))
        daystr.append(datetime.fromtimestamp(ctimes[x]).strftime('%d'))
        day.append(int(daystr[x]))
        temp = datetime(year[x], month[x], day[x])
        datetimes.append(temp)

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
aug = datetime(2020, 8, 12)

for date in datetimes:
    if (datetimes[z].month == aug.month):
        shutil.move(paths[datetimes[z].index], file1)

    else:
        print("failed")
z = z+1
y = y+1
