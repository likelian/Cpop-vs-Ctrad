from music21 import *
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np






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

                    print(interval_str)
                    print(duration)

                    if interval_str in interval_duration_df:
                        try:
                            interval_duration_df[interval_str][duration] += 1
                        except:
                            pass

                prev_element = element

    return interval_duration_df





def list_to_plot(interval_list, output_path, dataset_name):

    interval_list_str = []
    for interval in interval_list:
        interval_list_str.append(interval.name)

    interval_label_list = ["m2", "M2", "m3", "M3", "P4", "A4/d5", "P5", "m6", "M6", "m7", "M7", "P8", "m9", "M9"]

    interval_dict = {}
    for label in interval_label_list:
        if label == "A4/d5": 
            interval_dict[label] = interval_list_str.count("A4") + interval_list_str.count("d5")
        else:
            interval_dict[label] = interval_list_str.count(label)

    print(dataset_name)
    print(interval_dict)

    interval_df = pd.DataFrame(data=interval_dict, index=[0])

    fig = sns.barplot(data=interval_df)
    fig.set(xlabel='intervals', ylabel='counts')
    fig.set(title='Interval Distribution of ' + dataset_name)
    fig = fig.get_figure()
    #plt.show()
    fig.savefig(output_path + dataset_name + ".png")
    plt.close()