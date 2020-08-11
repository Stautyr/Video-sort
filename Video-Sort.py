#############################
# Program: Video Sort       #
# Python Version: 3.7.3     #
# Date: 8-10-2020           #
#############################
from datetime import datetime
import os
import shutil
from pathlib import Path
DEBUG = True

def sort(fileName, ext):
	x = [fileName[0:4],fileName[5:7], fileName[9:11]]
	year = x[0]
	month = x[1]
	day = x[2]
	date = datetime(year, month, day) 
	print (date)

start = "F:\\Gameplay\\VODS"
os.chdir(start)
o = os.listdir(start)
for x in range(len(o)):
	file = o[x]
	fileName = os.path.splitext(file)[0]
	ext = os.path.splitext(file)[1].lower()
	if (DEBUG):
		print (fileName)
		print (ext)
	sort(fileName, ext)