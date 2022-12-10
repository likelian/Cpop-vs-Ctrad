from music21 import *
import os
from midi_interval import *
from interval_direction import *






def plot_dataset_interval(dataset_name, dataset_path, output_path):

    interval_direction_dict = create_interval_direction_dict(gram=4)

    counter = 0

    for root, dirs, files in os.walk(dataset_path + dataset_name):
        for file in files:

            interval_list = []

            if ".krn" in file or ".mid" in file:
                #print("file", file)
                path = root + "/" + file
                stream = converter.parse(path)
                collect_midi_interval(stream, interval_list)
                interval_direction_dict = interval_direction(interval_list, interval_direction_dict, gram=4)


    
    plot_interval_direction_dict(interval_direction_dict, output_path, dataset_name)





    




dataset_path = "../data/"
output_path = "../results/interval_direction_distribution/"




dataset_name = "CoCoPops"
plot_dataset_interval(dataset_name, dataset_path, output_path)




dataset_name = "han"
plot_dataset_interval(dataset_name, dataset_path, output_path)




dataset_name = "POP909"
plot_dataset_interval(dataset_name, dataset_path, output_path)