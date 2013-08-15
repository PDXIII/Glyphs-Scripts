#MenuTitle: Make clockwise paths

import GlyphsApp
import random
random.seed()

'''
This script sets the direction of all paths to clockwise
'''

Doc = Glyphs.currentDocument
Font = Glyphs.font
glyphen = [x.parent for x in Doc.selectedLayers()]
listOfNames = [thisGlyph.name for thisGlyph in glyphen]
clearBackground = None;

def main():
  print(listOfNames)

  for glyph in glyphen:
    for currLayer in glyph.layers:
      for path in currLayer.paths:
        if path.direction < 0:
          path.reverse()

if __name__ == '__main__':
  main()