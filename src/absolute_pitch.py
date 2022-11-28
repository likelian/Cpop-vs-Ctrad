from music21 import *
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from collections import OrderedDict
import json



def collect_abs_pitch(stream, abs_pitch_dict):
    """
    input: music21 stream object
    """
    for part_stream in stream.parts.stream():
        prev_element = None
        for element in part_stream.recurse():
            if isinstance(element, note.Note):
                abs_pitch_dict[element.pitch.midi] += 1

    return abs_pitch_dict





def list_to_plot(abs_pitch_dict, output_path, dataset_name):


    abs_pitch_dict = OrderedDict(sorted(abs_pitch_dict.items()))

    """
    for key in range(128):
        if abs_pitch_dict[key] != 0:
            print("low")
            print(key)
            break
    
    for key in reversed(range(128)):
        if abs_pitch_dict[key] != 0:
            print("high")
            print(key)
            break
    """

    abs_pitch_df = pd.DataFrame(abs_pitch_dict, index=[0])

    #print(abs_pitch_df)

    fig = sns.barplot(data=abs_pitch_df)
    fig.set(xlabel='midi pitches', ylabel='counts')
    fig.set(title='Midi Pitch Distribution of ' + dataset_name)

    labels = fig.get_xticklabels()

    c_midi_pitch_dict = {'24': "C1", '36': "C2", '48': "C3", '60': "C4", '72': "C5", '84': "C6", '96': "C7", '108': "C8"}

    new_labels = []
    for x in labels:
        if x.get_text() in c_midi_pitch_dict.keys():
            new_labels.append(c_midi_pitch_dict[x.get_text()])
        else:
            new_labels.append("")
    
    
    fig.set_xticklabels(new_labels)






    fig = fig.get_figure()
    #plt.show()
    fig.savefig(output_path + dataset_name + ".png")
    plt.close()


    with open(output_path + dataset_name + ".json", "w") as outfile:
        json.dump(abs_pitch_dict, outfile)
