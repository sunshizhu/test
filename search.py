import os
import sys

def search(path, key):

	for f in os.listdir(path):
#		if os.path.isfile(os.path.join(path,f)) and key in os.path.split(f)[1]:
#			print os.path.abspath(f)
		if os.path.isdir(f):
			search(os.path.join(path,f),key)
		elif os.path.isfile(os.path.join(path,f)):
			if key in os.path.abspath(f):
				print os.path.abspath(f)

		else: pass




args = sys.argv
search(os.path.abspath('.'),args[1])