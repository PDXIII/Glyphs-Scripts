#MenuTitle: ExportHhxpMetrics.py
import sys
import os
from GlyphsApp import *
import objc
from AppKit import *
from Foundation import *

from operator import itemgetter, attrgetter
import json

'''
This scripts gets the metrics of all the fonts wich are open in Glyphs app
'''

def main():
  glyphArray = ['H','k','x','p']
  doc = Glyphs.currentDocument
  os.chdir(os.path.join(os.path.expanduser('~'), 'Desktop'))

  try:
    # This tries to open an existing file but creates a new file if necessary.
    metricsJSONFile = open('Metrics.json', 'w')
  except IOError:
    pass
  
  allMetrics = []
  
  for font in Glyphs.fonts:
    
    glyphsMetrics = []

    fontName = font.familyName
    
    for glyph in glyphArray:
      tempArray = []
      
      if glyph == 'p':
        for path in font.glyphs[glyph].layers[0].paths:
    
          tempArray.append(min(node.y for node in path.nodes))
        glyphsMetrics.append(min(tempArray))
      
      else:
        for path in font.glyphs[glyph].layers[0].paths:
        
          tempArray.append(max(node.y for node in path.nodes))
        glyphsMetrics.append(max(tempArray))
      
      tempArray = None

    myHkxpArray = []
    for value in glyphsMetrics:
      myHkxpArray.append(value/glyphsMetrics[0])
    
    currentFont = {"FontName": fontName, "HkxpArray": myHkxpArray}
    print(fontName)
    print(myHkxpArray)
      
    allMetrics.append(currentFont)
    glyphsMetrics = None
    
  sortedMetrics = sorted(allMetrics, key=itemgetter("FontName"))
  metricsJSONFile.write(json.dumps(sortedMetrics, indent=2))
  metricsJSONFile.close()

if __name__ == '__main__':
  main()