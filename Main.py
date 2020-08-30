import os
import shutil
from os import walk
from datetime import datetime


def findmonth(filedate):
    if filedate == 1:
        fmonth = "Jan"
    elif filedate == 2:
        fmonth = "Feb"
    elif filedate == 3:
        fmonth = "Mar"
    elif filedate == 4:
        fmonth = "Apr"
    elif filedate == 5:
        fmonth = "May"
    elif filedate == 6:
        fmonth = "Jun"
    elif filedate == 7:
        fmonth = "Jul"
    elif filedate == 8:
        fmonth = "Aug"
    elif filedate == 9:
        fmonth = "Sep"
    elif filedate == 10:
        fmonth = "Oct"
    elif filedate == 11:
        fmonth = "Nov"
    elif filedate == 12:
        fmonth = "Dec"
    return fmonth


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
years = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
         "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]


def checkfile(fmonth):
    for item in os.listdir(DOWNLOADS):
        y = 0
        x = 0
        if os.path.isdir(os.path.join(DOWNLOADS, item)):
            for ye in years:
                if item == years[y]:
                    break
                else:
                    dirs.append(item)
        for files in dirs:
            dirspath = (os.path.abspath(os.path.join(DOWNLOADS, dirs[x])))
            dirpaths.append(dirspath)

    a = 0
    bool = False
    for files in dirs:
        if dirs[a] == fmonth:
            bool = True
        else:
            bool = False
            a = a+1
    return bool


def createFolder(fmonth):
    newdir = os.path.join(DOWNLOADS, fmonth)
    os.mkdir(newdir)
    return newdir


for item in os.listdir(DOWNLOADS):
    y = 0
    x = 0
    if os.path.isfile(os.path.join(DOWNLOADS, item)):
        fileName.append(item)
    elif os.path.isdir(os.path.join(DOWNLOADS, item)):
        for ye in years:
            if item == years[y]:
                dirs.append(item)
                y = y+1
            else:
                fileName.append(item)
                y = y+1
    for files in dirs:
        dirspath = (os.path.abspath(os.path.join(DOWNLOADS, dirs[x])))
        dirpaths.append(dirspath)
        x = x+1
x = 0
for files in fileName:
    path = (os.path.abspath(os.path.join(DOWNLOADS, fileName[x])))
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


z = 0

for date in datetimes:
    filedate = datetimes[z].month
    fmonth = findmonth(filedate)
    bool = checkfile(fmonth)
    if bool:
        exdir = os.path.join(DOWNLOADS, fmonth)
        shutil.move(paths[z], exdir)
        z = z+1
    else:
        newdir = createFolder(fmonth)
        shutil.move(paths[z], newdir)
        z = z+1
