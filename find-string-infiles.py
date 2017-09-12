#!/usr/bin/env python

# Search for string in the files content of the folder recursively
#
# Set up: None
#
# Command line inputs: $1 - Search string, $2 - folder path
# In file inputs: None
# Runtime inputs: None

import os
import sys

def check(stringname, filename):
	datafile = file(filename)
	linenum = 0
	for line in datafile:
		linenum = linenum + 1
		if stringname in line:
			print str(linenum) +" FILE: " + filename

def traverse_dir(stringname, dirname='.'):
	for path, subdirs, files in os.walk(dirname): #('\Users\user\Desktop\Test_Py'):
		for filename in files:
			f = os.path.join(path, filename)
			check (stringname, f)

print "Checking for " + sys.argv[1] + " in " + sys.argv[2]
traverse_dir (sys.argv[1], sys.argv[2])