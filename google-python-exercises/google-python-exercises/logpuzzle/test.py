import os
import re
import sys
import urllib

def sndsort(piclink):
	turples = re.findall('-(\w+)-(\w+).jpg',piclink)
	print piclink
	pri = ''
	for turple in turples:
		pri = turple[1]
		print pri
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

  for items in sorted(piclist, key=sndsort):
  	print items
  return sorted(piclist, key = sndsort)

a = read_urls('place_code.google.com')


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
  urls = read_urls(img_urls)
  for item in urls:
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
  
download_images('place_code.google.com', 'mixed')


