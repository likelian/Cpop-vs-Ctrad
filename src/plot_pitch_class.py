from music21 import *
import os
from pitch_class import *




def plot_dataset_interval(dataset_name, dataset_path, output_path):

    pitch_class_dict = {}

    for root, dirs, files in os.walk(dataset_path + dataset_name):
        for file in files:
            if ".krn" in file or ".mid" in file:
                #print("file", file)
                path = root + "/" + file
                stream = converter.parse(path)
                collect_pitch_class(stream, pitch_class_dict)

    dict_to_plot(pitch_class_dict, output_path, dataset_name)





dataset_path = "../data/"
output_path = "../results/pitch_class_distribution/"




dataset_name = "CoCoPops"
plot_dataset_interval(dataset_name, dataset_path, output_path)




dataset_name = "han"
plot_dataset_interval(dataset_name, dataset_path, output_path)




dataset_name = "POP909"
plot_dataset_interval(dataset_name, dataset_path, output_path)