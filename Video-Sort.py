#############################
# Program: Video Sort       #
# Python Version: 3.7.3     #
# Date: 8-10-2020           #
#############################
import datetime
import os
import shutil
from pathlib import Path

start = "F:\\Gameplay\\VODS"
os.chdir(start)
o = os.listdir(start)
for x in range(len(o)):
	file = o[x]
	fileName = os.path.splitext(file)[0]
	ext = os.path.splitext(file)[1].lower()
	print (fileName)
	print (ext)