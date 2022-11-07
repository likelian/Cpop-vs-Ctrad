from music21 import *
import os
from interval_duration import *
import pandas as pd




def plot_interval_duration(dataset_name, dataset_path, output_path):


    interval_label_list = ["m2", "M2", "m3", "M3", "P4", "A4/d5", "P5", "m6", "M6", "m7", "M7", "P8", "m9", "M9"]
    duration_list = np.arange(33) * 0.25
    interval_duration_df = pd.DataFrame(index=list(duration_list), columns=interval_label_list)
    interval_duration_df.fillna(0, inplace=True)

    counter = 0

    for root, dirs, files in os.walk(dataset_path + dataset_name):
        for file in files:
            if ".krn" in file or ".mid" in file:
                #print("file", file)
                path = root + "/" + file
                stream = converter.parse(path)
                collect_interval_duration(stream, interval_duration_df)

                #remove
                quit()

    interval_duration_plot(interval_list, output_path, dataset_name)

    interval_list = []




dataset_path = "../data/"
output_path = "../results/interval_duration/"


dataset_name = "POP909"
plot_interval_duration(dataset_name, dataset_path, output_path)


dataset_name = "CoCoPops"
plot_interval_duration(dataset_name, dataset_path, output_path)



dataset_name = "han"
plot_interval_duration(dataset_name, dataset_path, output_path)




