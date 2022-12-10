from music21 import *
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from itertools import product
import json






def plot_interval_transition_df(interval_transition_df, output_path, dataset_name):


    return None


    



def create_interval_transition_df():
    #"⬆️","⬇️"

    all_interval_list = list(reversed(range(-12, 13)))
    all_interval_list.remove(0)

    interval_transition_df = pd.DataFrame(0, columns=all_interval_list, index=all_interval_list)

    return interval_transition_df



def interval_transition(interval_list, interval_transition_df, gram=2):

    
    for idx in range(len(interval_list)-(gram-1)):
        gram_interval_list = []
        for i in range(gram):
            gram_interval_list.append(interval_list[idx+i])

        try:
            interval_transition_df[gram_interval_list[1]][gram_interval_list[0]] += 1
        except:
            pass


    return interval_transition_df



