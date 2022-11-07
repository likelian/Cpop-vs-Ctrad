from music21 import *
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import LogNorm




def collect_interval_duration(stream, interval_duration_df):
    """
    input: music21 stream object
    """

    for part_stream in stream.parts.stream():
        #print(part_stream.show('text'))

        prev_element = None
        for element in part_stream.recurse():
            if isinstance(element, note.Note):
                #get interval
                if prev_element is not None:
                    interval_str = interval.Interval(prev_element, element).name
                    duration = prev_element.duration.quarterLength

                    if interval_str == "A4" or interval_str == "d5":
                        interval_str = "A4/d5"

                    if interval_str in interval_duration_df:
                        try:
                            interval_duration_df[interval_str][duration] += 1
                        except:
                            pass

                prev_element = element

    return interval_duration_df





def interval_duration_plot(interval_duration_df, output_path, dataset_name):

    print(dataset_name)
    print(interval_duration_df)

    #cmap = sns.cm.rocket_r
    fig = sns.heatmap(interval_duration_df, norm=LogNorm())
    fig.set(xlabel='intervals', ylabel='duration')
    fig.set(title=dataset_name)
    plt.tight_layout()
    fig = fig.get_figure()
    #plt.show()
    fig.savefig(output_path + dataset_name + ".png")
    plt.close()


    return None