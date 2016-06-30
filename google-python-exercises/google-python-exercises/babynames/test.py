import os
import re
import sys
import urllib


def read_urls(filename):
  """Returns a list of the puzzle urls from the given log file,
  extracting the hostname from the filename itself.
  Screens out duplicate urls and returns the urls sorted into
  increasing order."""
  # +++your code here+++

  try:
  	f = open(filename,'rU')
  	text = f.read()
  except:
  	print 'IOError'

  for line in text:
  	print line


 read_urls('animal_code.google.com')