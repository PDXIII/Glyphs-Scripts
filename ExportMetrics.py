#MenuTitle: Export Metrics
import sys
import os
from GlyphsApp import *
import objc
from AppKit import *
from Foundation import *


def main():
	doc = Glyphs.currentDocument
	familyName = doc.font.familyName
	os.chdir(os.path.join(os.path.expanduser('~'), 'Desktop'))

	try:
		# This tries to open an existing file but creates a new file if necessary.
		metricsTextFile = open('%s-Metrics.txt' % familyName, 'w')
	except IOError:
		pass
	
	metricsTextFile.write('"familyName" : %s,\n' % str(familyName))
	metricsTextFile.write('"ascender" : %s,\n' % str(doc.selectedFontMaster().ascender))
	metricsTextFile.write('"capHeight" : %s,\n' % str(doc.selectedFontMaster().capHeight))
	metricsTextFile.write('"xHeight" : %s,\n' % str(doc.selectedFontMaster().xHeight))
	metricsTextFile.write('"descender" : %s' % str(doc.selectedFontMaster().descender))
	
	metricsTextFile.close()

if __name__ == '__main__':
	main()