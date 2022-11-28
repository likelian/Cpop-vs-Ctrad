import music21
from music21 import *
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from collections import OrderedDict
import json



def collect_scale(stream, key_dict, scale_dict):
    """
    input: music21 stream object
    """

    try:
        key = stream.analyze('key')
    except:
        return key_dict, scale_dict
    #print(key.tonic.name, key.mode)

    try:
        key_dict[key.tonic.name] += 1
    except:
        key_dict[key.tonic.name] = 1

    try:
        scale_dict[key.mode] += 1
    except:
        scale_dict[key.mode] = 1
    

    return key_dict, scale_dict





def dict_to_plot(key_dict, scale_dict, output_path, dataset_name):

    print(key_dict)
    print(scale_dict)


    try:
        key_dict["A-"] += key_dict["G#"]
        del key_dict["G#"]
    except:
        pass

    key_df = pd.DataFrame(data=key_dict, index=[0])

    fig = sns.barplot(data=key_df)
    fig.set(xlabel='keys', ylabel='counts')
    fig.set(title='Key Distribution of ' + dataset_name)
    fig = fig.get_figure()
    #plt.show()
    fig.savefig(output_path + dataset_name + "_key.png")
    plt.close()

    with open(output_path + dataset_name + "_key.json", "w") as outfile:
        json.dump(key_dict, outfile)

    



    scale_df = pd.DataFrame(data=scale_dict, index=[0])

    fig = sns.barplot(data=scale_df)
    fig.set(xlabel='scale mode', ylabel='counts')
    fig.set(title='Scale Mode Distribution of ' + dataset_name)
    fig = fig.get_figure()
    #plt.show()
    fig.savefig(output_path + dataset_name + "_scale_mode.png")
    plt.close()

    with open(output_path + dataset_name + "_scale_mode.json", "w") as outfile:
        json.dump(scale_dict, outfile)

    return None

