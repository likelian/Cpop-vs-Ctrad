from music21 import *
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from itertools import product
import json




def change_dict_key_to_string(interval_direction_dict):

    new_interval_direction_dict = {}

    for key in interval_direction_dict.keys():
        new_key = str(key)

        new_interval_direction_dict[new_key] = interval_direction_dict[key]

    return new_interval_direction_dict





def change_dict_keys(interval_direction_dict):

    new_interval_direction_dict = {}


    for key in interval_direction_dict.keys():
        new_key = key.replace("\'", "")
        new_key = new_key.replace("(", "")
        new_key = new_key.replace(")", "")
        new_key = new_key.replace(",", "")

        new_interval_direction_dict[new_key] = interval_direction_dict[key]
        
    return new_interval_direction_dict



    

def plot_interval_direction_dict(interval_direction_dict, output_path, dataset_name):

    interval_direction_dict = change_dict_key_to_string(interval_direction_dict)

    interval_direction_dict = change_dict_keys(interval_direction_dict)

    with open(output_path + dataset_name + ".json", "w") as outfile:
        json.dump(interval_direction_dict, outfile)



    interval_direction_df = pd.DataFrame(data=interval_direction_dict, index=[0])

    fig = sns.barplot(data=interval_direction_df, orient="h")
    fig.set(xlabel='counts', ylabel='directions')
    fig.set(title='Interval Direction Distribution of ' + dataset_name)
    plt.tight_layout()
    fig = fig.get_figure()
    fig.savefig(output_path + dataset_name + ".png")
    plt.close()

    



def create_interval_direction_dict(gram=4):

    interval_direction_dict = {}

    
    for i in product(["⬆️","⬇️"], repeat=gram):
    #for i in product(["up","down"], repeat=gram):
        interval_direction_dict[i] = 0

    return interval_direction_dict



def interval_direction(interval_list, interval_direction_dict, gram=4):
    """
    list
    count the directions in a midi_interval list

    output:
        dictionary of directions and their counts
    """

    interval_arr = np.array(interval_list)

    #interval_direction_list = np.where(interval_arr > 0, "up", "down")
    interval_direction_list = np.where(interval_arr > 0, "⬆️","⬇️")

    for idx in range(len(interval_direction_list)-(gram-1)):
        direction_list = []
        for i in range(gram):
            direction_list.append(interval_direction_list[idx+i])

        for key in interval_direction_dict.keys():
            if key == tuple(direction_list):
                interval_direction_dict[key] += 1

    return interval_direction_dict



