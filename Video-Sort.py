#############################
# Program: Video Sort       #
# Python Version: 3.7.3     #
# Date: 8-10-2020           #
#############################
import datetime
import os
import shutil
from pathlib import Path
DEBUG = True

def sort(fileName, ext):
	date = datetime(fileName) 
	print date

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