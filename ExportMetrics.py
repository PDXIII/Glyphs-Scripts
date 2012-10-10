#MenuTitle: Export Metrics
import sys
import os
from GlyphsApp import *
import objc
from AppKit import *
from Foundation import *

'''
This script writes the basic metrics of the current font into an textfile. 
The syntax is a little bit pseudo .json for better handling in AdobeIndesign later.
'''

def main():
	doc = Glyphs.currentDocument
	familyName = doc.font.familyName
	os.chdir(os.path.join(os.path.expanduser('~'), 'Desktop/FontMetrics'))

	try:
		# This tries to open an existing file but creates a new file if necessary.
		metricsTextFile = open('%s-Metrics.json' % familyName, 'w')
	except IOError:
		pass
	
	metricsTextFile.write('{\n\t"familyName" : "%s",\n' % str(familyName))
	metricsTextFile.write('\t"metrics" : {\n')
	metricsTextFile.write('\t\t"ascender" : %s,\n' % str(doc.selectedFontMaster().ascender))
	metricsTextFile.write('\t\t"capHeight" : %s,\n' % str(doc.selectedFontMaster().capHeight))
	metricsTextFile.write('\t\t"xHeight" : %s,\n' % str(doc.selectedFontMaster().xHeight))
	metricsTextFile.write('\t\t"descender" : %s' % str(doc.selectedFontMaster().descender))
	metricsTextFile.write('\n\t}\n}')

	metricsTextFile.close()

if __name__ == '__main__':
	main()