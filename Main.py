import os
import shutil
from os import walk
import glob

DOWNLOADS = r'c:\Users\arxhe\Downloads'
f = []
p = []
for files in os.walk(DOWNLOADS):
    f.extend(files)
y = 0
for x in p:
    print(os.path.getctime(f[y]))
    y = y+1
