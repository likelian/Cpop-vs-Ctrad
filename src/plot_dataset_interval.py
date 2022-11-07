from music21 import *
import os
from count_interval import *




def plot_dataset_interval(dataset_name, dataset_path, output_path):

    interval_list = []

    counter = 0

    for root, dirs, files in os.walk(dataset_path + dataset_name):
        for file in files:
            if ".krn" in file or ".mid" in file:
                #print("file", file)
                path = root + "/" + file
                stream = converter.parse(path)
                collect_interval(stream, interval_list)

    list_to_plot(interval_list, output_path, dataset_name)

    interval_list = []




dataset_path = "../data/"
output_path = "../results/interval_distribution/"




dataset_name = "CoCoPops"
plot_dataset_interval(dataset_name, dataset_path, output_path)




dataset_name = "han"
plot_dataset_interval(dataset_name, dataset_path, output_path)




dataset_name = "POP909"
plot_dataset_interval(dataset_name, dataset_path, output_path)