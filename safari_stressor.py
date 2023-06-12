x#
#
# Lucas Oakley
# quick 'n' dirty safari stress tester in python to open a bunch of new random pages. 
# Used for debugging webkit issues on a Mac 
# 27 march 2015
#


import subprocess
from random import randrange
import urllib
from HTMLParser import HTMLParser


class MyHTMLParser2(HTMLParser):
	def handle_starttag(self, tag, attrs):
		for attr in attrs:
			if attr == "href":
				print("    attr: ", attr)

class MyHTMLParser(HTMLParser):
	def handle_starttag(self, tag, attrs): 
		print("Start tag: ", tag)
		if tag == "href":
			print("    attrs: ", attrs)
		#for attr in attrs: 
			#if tag == "href":
				#print("    attr: ", attr)





CUR_PAGE = ''

def randomPage():
	options =['http://stackoverflow.com/',
		'http://google.com/', 'http://apple.com/'
	]
	return options[randrange(0, len(options))]

def parsePage(page):
	# array of lines
	raw = urllib.urlopen(page).read()
	#href="https://mail.google.com/mail/?tab=wm"
	viable = []
	parser = MyHTMLParser()
	#for line in raw: 
	tempParsed = parser.feed(raw)
	#for name, value in tempParsed.attrs:
	#	if name == "href":
	#		viable.append(value)
	return viable[randrange(0, len(viable))]

# what?    duh,   new tab flag, program, 		url
tab_args = ['/usr/bin/open', '-a', 'Safari'] 
# new process flag -n
process_args = ['/usr/bin/open', '-n', '-a', 'Safari']



print(parsePage(randomPage()))