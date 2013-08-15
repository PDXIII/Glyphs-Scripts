#MenuTitle: Making a Font outof images

import sys
import os
import os.path
from GlyphsApp import *
import objc
from AppKit import *
from Foundation import *

import Tkinter, tkFileDialog

'''
This script is still in development!!!
This script reads the structure of an folder and the images within and creates a glyph for every images.
I really need toknow how dialogs work in python 
'''
root = Tkinter.Tk()
sys.argv = 'Some Text' # This is not really correct, but it works. 

def main():
  
  dirname = tkFileDialog.askdirectory(parent=root,initialdir="/",title='Please select a directory')

  if len(dirname ) > 0:
    print "You chose %s" % dirname

if __name__ == '__main__':
  main()