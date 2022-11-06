from music21 import *
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def collect_interval(stream, interval_list):
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
                    interval_obj = interval.Interval(prev_element, element)
                    #print(interval_obj)
                    interval_list.append(interval_obj)

                prev_element = element
                

    return interval_list



def list_to_plot(interval_list, output_path, dataset_name):
    
    interval_list_str = []
    for interval in interval_list:
        interval_list_str.append(interval.name)

    interval_label_list = ["P1", "m2", "M2", "m3", "M3", "P4", "A4/d5", "P5", "m6", "M6", "m7", "M7", "P8", "m9", "M9", "m10", "M10"]

    interval_dict = {}
    for label in interval_label_list:
        if label == "A4/d5": 
            interval_dict[label] = interval_list_str.count("A4") + interval_list_str.count("P5")
        else:
            interval_dict[label] = interval_list_str.count(label)

    #print(interval_dict)

    interval_df = pd.DataFrame(data=interval_dict, index=[0])

    fig = sns.barplot(data=interval_df)
    fig.set(xlabel='intervals', ylabel='counts')
    fig = fig.get_figure()
    #plt.show()
    fig.savefig(output_path + dataset_name + ".png")