# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 14:24:08 2019

@author: Dell
"""

import os
from astropy.io import fits


findobject = '\'53733\''

os.chdir('I:/BASS')
path = os.getcwd()


def findinfo(strfile):
    phdulist = fits.open(strfile)
    objectname = phdulist[0].header['OBJECT']
    filtername = phdulist[0].header['FILTER']
    return objectname,filtername


for root, dirs, files in os.walk(path):
   for file in files:
       strfile = os.path.join(root, file)
       objectname,filtername = findinfo(strfile)
      # print(objectname)
       if (objectname == findobject):
           print(strfile)
           print(filtername)
