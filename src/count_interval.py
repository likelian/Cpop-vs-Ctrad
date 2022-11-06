from music21 import *


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