import sys
import re
import os
import shutil
import commands


def get_special_paths(dir):
	filenames = os.listdir(dir)
	results = []
	for file in filenames:
		if re.search('__\w+__',file):
			results.append(os.path.abspath(os.path.join(dir,file)))



	return results


def copy_to(paths,dir):




	return

def zip_to(paths,zippath):



	return


results = get_special_paths('.')
for item in results:
	print item