from music21 import *
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt



def collect_midi_interval(stream, interval_list):
    """
    input: music21 stream object
    """

    for part_stream in stream.parts.stream():
        #print(part_stream.show('text'))

        prev_element = None
        for element in part_stream.recurse():
            if isinstance(element, note.Note):
                if prev_element is not None:
                    midi_interval = element.pitch.midi - prev_element.pitch.midi

                    if midi_interval != 0:
                        interval_list.append(midi_interval)

                prev_element = element
                

    return interval_list



