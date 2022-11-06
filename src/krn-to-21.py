from music21 import *
import os


dataset_path = "../data/CoCoPops"

for root, dirs, files in os.walk(dataset_path):
    for file in files:
        if ".krn" in file:
            print("file", file)
            path = root + "/" + file
            stream = converter.parse(path)
            
