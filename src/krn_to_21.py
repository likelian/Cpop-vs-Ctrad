from music21 import *
import os
from count_interval import *





dataset_name = "CoCoPops"
dataset_path = "../data/"
output_path = "../results/"

interval_list = []

for root, dirs, files in os.walk(dataset_path + dataset_name):
    for file in files:
        if ".krn" in file or ".mid" in file:
            print("file", file)
            path = root + "/" + file
            stream = converter.parse(path)
            collect_interval(stream, interval_list)

            #remove
            break


list_to_plot(interval_list, output_path, dataset_name)


