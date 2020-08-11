#############################
# Program: Video Sort       #
# Python Version: 3.7.3     #
# Date: 8-10-2020           #
#############################
from datetime import datetime
import os
import shutil
from pathlib import Path
DEBUG = False

start = "F:\\Gameplay\\VODS"
os.chdir(start)

def sort(fileName, ext, file):
	if (ext == ".m4a" or ext == ".mp4"):
		x = [fileName[0:4],fileName[5:7], fileName[8:10]]
		year = int(x[0])
		month = int(x[1])
		day = int(x[2])
		date = datetime(year, month, day)
		date = date.strftime("%B %dth Clips")
		print (date)
		if (Path(start)/date).is_dir():
			if (DEBUG):
				print("folder found")
		else:
			if (DEBUG):
				print(str(Path(start)/date) + " does not exist")
			os.mkdir(date)
		shutil.move(Path(start)/file, Path(start)/date/file)

o = os.listdir(start)
for x in range(len(o)):
	file = o[x]
	fileName = os.path.splitext(file)[0]
	ext = os.path.splitext(file)[1].lower()
	if (DEBUG):
		print (fileName)
		print (ext)
	sort(fileName, ext, file)