from music21 import *
import os
from absolute_pitch import *




def plot_dataset_pitch(dataset_name, dataset_path, output_path):

    abs_pitch_dict = {}

    for i in range(36, 99):
        abs_pitch_dict[i] = 0

    
    for root, dirs, files in os.walk(dataset_path + dataset_name):
        for file in files:
            if ".krn" in file or ".mid" in file:
                #print("file", file)
                path = root + "/" + file
                stream = converter.parse(path)
                collect_abs_pitch(stream, abs_pitch_dict)
    

    list_to_plot(abs_pitch_dict, output_path, dataset_name)






dataset_path = "../data/"
output_path = "../results/pitch_distribution/"


dataset_name = "CoCoPops"
plot_dataset_pitch(dataset_name, dataset_path, output_path)



dataset_name = "han"
plot_dataset_pitch(dataset_name, dataset_path, output_path)



dataset_name = "POP909"
plot_dataset_pitch(dataset_name, dataset_path, output_path)