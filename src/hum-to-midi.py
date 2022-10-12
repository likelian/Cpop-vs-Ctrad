from music21 import *



"""
author: likelian

possible way to extract tracks from midi file
https://web.mit.edu/music21/doc/moduleReference/moduleHumdrumSpineParser.html

"""


s = converter.parse('../data/han/han0001.krn')

s.analyze('key')

print(s.analyze('key'))

s = converter.parse('../data/POP909-Dataset/POP909/001/001.mid')

s.analyze('key')

print(s.analyze('key'))