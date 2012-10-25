#MenuTitle: Sketch
import sys
import os
from GlyphsApp import *
import objc
from AppKit import *
from Foundation import *
from operator import attrgetter

'''
This is just a Sketch for experimenting. It's hardly recommanded not to use this script. 
If there is something useful in it you will find it in another script with a discription.
'''

def main():
	doc = Glyphs.currentDocument
	font = doc.font
	myChar = font.glyphs['A']
	myLayer = myChar.layers[0]
	
	print len(myLayer.paths)
	
	for path in myLayer.paths:
	#	print path.nodes
		print max(node.y for node in path.nodes)
		print max(path.nodes, key=attrgetter("y"))

if __name__ == '__main__':
	main()