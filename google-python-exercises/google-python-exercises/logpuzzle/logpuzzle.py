#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import os
import re
import sys
import urllib

"""Logpuzzle exercise
Given an apache logfile, find the puzzle urls and download the images.

Here's what a puzzle url looks like:
10.254.254.28 - - [06/Aug/2007:00:13:48 -0700] "GET /~foo/puzzle-bar-aaab.jpg HTTP/1.0" 302 528 "-" "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.6) Gecko/20070725 Firefox/2.0.0.6"
"""
def sndsort(piclink):
  turples = re.findall('-(\w+)-(\w+).jpg',piclink)
  #print piclink
  pri = ''
  for turple in turples:
    pri = turple[1]
    #print pri
  return pri

def read_urls(filename):
  """Returns a list of the puzzle urls from the given log file,
  extracting the hostname from the filename itself.
  Screens out duplicate urls and returns the urls sorted into
  increasing order."""
  # +++your code here+++
  try:
    f = open(filename,'rU')
  except:
    print 'IOError'
  piclist =[] 
  for line in f:
    line = line.rstrip()
  #print line
    match = re.search(r'GET ([\S]+.jpg)',line)
    if match:
      jpg = 'http://code.google.com'+ match.group(1)
      if jpg not in piclist:
        piclist.append(jpg)

  #for items in sorted(piclist, key=sndsort):
    #print items
  return sorted(piclist, key = sndsort)



def download_images(img_urls, dest_dir):
  """Given the urls already in the correct order, downloads
  each image into the given directory.
  Gives the images local filenames img0, img1, and so on.
  Creates an index.html in the directory
  with an img tag to show each local image file.
  Creates the directory if necessary.
  """
  # +++your code here+++
  counter = 1
  imgstring = ''
  if os.path.exists(dest_dir):
    pass
  else:
    os.mkdir(dest_dir)
  #urls = read_urls(img_urls)
  for item in img_urls:
    print "Retrieving..."
    pos = os.path.join(dest_dir,('img%d.jpg'%counter))
    #print pos
    #print item
    imgstring = imgstring+('<img src="%s">'%item)
    urllib.urlretrieve(item, pos)
    counter = counter +1
  name = dest_dir + '/index.html'
  page = open(name,'w')
  content = '<verbatim><html><body>'+imgstring+ '</body></html>'
  page.write(content)
  return


def main():
  args = sys.argv[1:]

  if not args:
    print 'usage: [--todir dir] logfile '
    sys.exit(1)

  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]

  img_urls = read_urls(args[0])

  if todir:
    download_images(img_urls, todir)
  else:
    print '\n'.join(img_urls)

if __name__ == '__main__':
  main()
