from music21 import *
import os
from midi_interval import *
from interval_transition import *






def plot_interval_transition(dataset_name, dataset_path, output_path):

    interval_transition_df = create_interval_transition_df()

    counter = 0

    for root, dirs, files in os.walk(dataset_path + dataset_name):
        for file in files:

            interval_list = []

            if ".krn" in file or ".mid" in file:
                #print("file", file)
                path = root + "/" + file
                stream = converter.parse(path)
                collect_midi_interval(stream, interval_list)
                interval_transition_df = interval_transition(interval_list, interval_transition_df, gram=2)

                counter += 1
                #if counter > 10: break


    print(interval_transition_df)


    plot_interval_transition_df(interval_transition_df, output_path, dataset_name)





    




dataset_path = "../data/"
output_path = "../results/interval_transition/"




dataset_name = "CoCoPops"
plot_interval_transition(dataset_name, dataset_path, output_path)




dataset_name = "han"
plot_interval_transition(dataset_name, dataset_path, output_path)




dataset_name = "POP909"
plot_interval_transition(dataset_name, dataset_path, output_path)