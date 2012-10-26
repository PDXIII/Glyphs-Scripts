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
  glyphArray = ['A','l','x','p']
  glyphsMetrics = []
  doc = Glyphs.currentDocument
  
  for glyph in glyphArray:
    tempArray = []
    
    if glyph == 'p':
      for path in doc.font.glyphs[glyph].layers[0].paths:
  
        tempArray.append(min(node.y for node in path.nodes))
      glyphsMetrics.append(min(tempArray))
  
      
    else:
      for path in doc.font.glyphs[glyph].layers[0].paths:
      
        tempArray.append(max(node.y for node in path.nodes))
      glyphsMetrics.append(max(tempArray))
        
  print(glyphsMetrics)

if __name__ == '__main__':
  main()