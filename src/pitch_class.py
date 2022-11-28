from music21 import *
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from collections import OrderedDict
import json


def collect_pitch_class(stream, pitch_class_dict):
    """
    input: music21 stream object
    """

    for part_stream in stream.parts.stream():

        pcCount = analysis.pitchAnalysis.pitchAttributeCount(stream, 'pitchClass')

        for n in sorted(pcCount):
            try:
                pitch_class_dict[n] += 1
            except:
                pitch_class_dict[n] = 1


    return pitch_class_dict





def dict_to_plot(pitch_class_dict, output_path, dataset_name):


    pitch_class_dict = OrderedDict(sorted(pitch_class_dict.items()))

    print(pitch_class_dict)

    pitch_class_df = pd.DataFrame(data=pitch_class_dict, index=[0])

    fig = sns.barplot(data=pitch_class_df)
    fig.set(xlabel='pitch classes', ylabel='counts')
    fig.set(title='Pitch Class Distribution of ' + dataset_name)
    fig = fig.get_figure()
    #plt.show()
    fig.savefig(output_path + dataset_name + ".png")
    plt.close()


    with open(output_path + dataset_name + ".json", "w") as outfile:
        json.dump(pitch_class_dict, outfile)

    return None

