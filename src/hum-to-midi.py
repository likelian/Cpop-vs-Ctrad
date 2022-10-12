from music21 import *



"""
author: likelian
"""


s = converter.parse('/Users/likelian/Desktop/Musicology/Cpop-vs-Ctrad/data/han/han0001.krn')

s.analyze('key')


print(s.analyze('key'))