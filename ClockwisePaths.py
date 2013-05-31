#MenuTitle: Make clockwise paths

import GlyphsApp
import random
random.seed()

'''
This is just a Sketch for experimenting. It is hardly recommanded not to use this script. 
If there is something useful in it you will find it in another script with a discription.
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