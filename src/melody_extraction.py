from music21 import *
import os
#import re

"""
author: likelian

possible way to extract tracks from midi file
https://web.mit.edu/music21/doc/moduleReference/moduleHumdrumSpineParser.html

"""

def extract_melody_track(stream):
    """
    input: a music21 stream object
    output: a music21 steam object, track name is "melody"
    """
    for part in stream.parts:
        if part[0].bestName() == "MELODY":
            return part
    
    return None




dataset_path = '../data/POP909-Dataset/POP909/'
output_path = '../data/POP909-Dataset/extracted/'


for root, dirs, files in os.walk(dataset_path):
    for file in files:
        if ".mid" in file and "-" not in file:
            #print("root", root)
            #print("dirs", dirs)
            print("file", file)
            path = root + "/" + file
            stream = converter.parse(path)
            part = extract_melody_track(stream)
            if part is not None:
                part.write('midi', fp='../data/POP909-Dataset/melodies/'+file)




