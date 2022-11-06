from music21 import *
import os
from count_interval import *




dataset_path = "../data/CoCoPops"
interval_list = []

for root, dirs, files in os.walk(dataset_path):
    for file in files:
        if ".krn" in file:
            print("file", file)
            path = root + "/" + file
            stream = converter.parse(path)
            collect_interval(stream, interval_list)


            #remove
            break


#print(interval_list)

interval_list_str = []
for interval in interval_list:
    interval_list_str.append(interval.name)

print(interval_list_str)

print(interval_list_str.count("P5"))


