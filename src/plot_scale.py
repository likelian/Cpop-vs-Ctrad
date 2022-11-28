from music21 import *
import os
from scale import *




def plot_dataset_scale(dataset_name, dataset_path, output_path):

    scale_dict = {}
    key_dict = {'C':0, 'C#':0, 'D':0, 'E-':0, 'E':0, 'F':0, 'F#':0, 'G':0, 'A-':0, 'A':0, 'B-':0, 'B':0}
 
    for root, dirs, files in os.walk(dataset_path + dataset_name):
        for file in files:
            if ".krn" in file or ".mid" in file:
                #print("file", file)
                path = root + "/" + file
                stream = converter.parse(path)
                collect_scale(stream, key_dict, scale_dict)
    

    dict_to_plot(key_dict, scale_dict, output_path, dataset_name)




dataset_path = "../data/"
output_path = "../results/key_scale_distribution/"


dataset_name = "CoCoPops"
plot_dataset_scale(dataset_name, dataset_path, output_path)



dataset_name = "han"
plot_dataset_scale(dataset_name, dataset_path, output_path)


# POP909 has an official key and scale anotation, but we are not using it
dataset_name = "POP909"
plot_dataset_scale(dataset_name, dataset_path, output_path)