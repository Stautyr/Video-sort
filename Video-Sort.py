#############################
# Program: Video Sort       #
# Python Version: 3.7.3     #
# Date: 8-10-2020           #
#############################
import datetime
import os
import shutil
from pathlib import Path




start = Path("F:/Gameplay")
o = os.listdir(start)
for x in o:
	file = o[x]
	ext = os.path.splitext(file)[-1].lower()
	print (exe)