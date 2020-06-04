import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os

DATA_FOLDER = 'data'
FIG_FOLDER = 'fig'

os.makedirs(FIG_FOLDER, exist_ok=True)

data_file = os.path.join(DATA_FOLDER, 'smartphone-typing.csv')
df = pd.read_csv(data_file)

# Number of people 'low' for the month 1, month 2, etc. for visiting

age_group = ['young', 'old']

sentence_volume_range = {'svr0': [1, 20], 'svr1': [20, 40], 'svr2': [40, 60], 'svr3': [60, 80], 'svr4': [80, 100]}
sentence_volume_range_labels = list(sentence_volume_range.keys())

number_of_letters_range = {'nlr0': [1, 20], 'nlr1': [20, 40], 'nlr2': [40, 60], 'nlr3': [60, 80], 'nlr4': [80, 100]}
number_of_letters_range = list(number_of_letters_range.keys())


trial_time_range = {'ttr0': [1, 1000], 'ttr2': [1000, 5000], 'ttr3': [5000, 10000], 'ttr4': [10000, 15000],
                    'ttr5': [15000, 20000], 'ttr6': [20000, 50000], 'ttr7': [50000, 100000],
                    'ttr8': [100000, 150000], 'ttr9': [150000, 200000]}
trial_time_range = (trial_time_range.keys())

error_percent_range = {'epr0': [0, 0.5], 'epr1': [0.5, 1.0], 'epr2': [1.0, 1.5], 'epr3': [1.5, 2.0]}
error_percent_range = (error_percent_range.keys())

frequency_of_backspace_range = {'fbr0': [0], 'fbr1': [1, 5], 'fbr2': [5, 10], 'fbr3': [10, 20], 'fbr4': [20, 30]}
frequency_of_backspace_range = (frequency_of_backspace_range.keys())

for ag in age_group:

    '''
    print('ag',ag)

    print('svr0',[1, 20], 'svr1', [20, 40], 'svr2',[40, 60], 'svr3',[60, 80], 'svr4',[80, 100])

    print('nlr0',[1, 20], 'nlr1',[20, 40], 'nlr2',[40, 60], 'nlr3',[60, 80], 'nlr4',[80, 100])

    print('ttr0',[1, 1000], 'ttr2',[1000, 5000], 'ttr3',[5000, 10000], 'ttr4',[10000, 15000],
                            'ttr5',[15000, 20000], 'ttr6',[20000, 50000], 'ttr7',[50000, 100000],
                            'ttr8',[100000, 150000], 'ttr9',[150000, 200000])

    print('epr0',[0, 0.5], 'epr1',[0.5, 1.0], 'epr2', [1.0, 1.5], 'epr3',[1.5, 2.0])

    print('fbr0',[0], 'fbr1',[1, 5], 'fbr2',[5, 10], 'fbr3',[10, 20], 'fbr4',[20,30])
    '''


    data = {}

    sentence_volume_range_labels = ['svr0', 'svr1', 'svr2', 'svr3', 'svr4']
    number_of_letters_range_labels = ['nlr0', 'nlr1', 'nlr2', 'nlr3', 'nlr4']
    trial_time_range_labels = ['ttr0', 'ttr2', 'ttr3', 'ttr4', 'ttr5', 'ttr6', 'ttr7', 'ttr8', 'ttr9']
    error_percent_range_labels = ['epr0', 'epr1', 'epr2', 'epr3', ]
    frequency_of_backspace_range_labels = ['fbr0', 'fbr1', 'fbr2', 'fbr3', 'fbr4']

    for svr_label in sentence_volume_range_labels:
        data[svr_label] = []

    for nlr_label in number_of_letters_range_labels:
        data[nlr_label] = []

    for ttr_label in trial_time_range_labels:
        data[ttr_label] = []

    for epr_label in error_percent_range_labels:
        data[epr_label] = []

    for fbr_label in frequency_of_backspace_range_labels:
        data[fbr_label] = []

    is_ag = df['condition'] == ag

    for (sentence_volume_range_labels) in sentence_volume_range.items():
        is_sentence_volume_range = df[sentence_volume_range_labels] == sentence_volume_range_labels
        count_sentence_volume_range_labels = len(df[is_sentence_volume_range])

        data[sentence_volume_range_labels].append(count_sentence_volume_range_labels)

    mean_sv = np.mean(df[is_ag])
    data['mean'].append(mean_sv)

    for (number_of_letters_range_labels) in number_of_letters_range.items():
        number_of_letters_range = df[number_of_letters_range_labels] == number_of_letters_range_labels
        count_number_of_letters_range_labels = len(df[number_of_letters_range_labels])

        data[number_of_letters_range_labels].append(count_number_of_letters_range_labels)

    mean_nl = np.mean(df[is_ag])
    data['mean'].append(mean_nl)

    for (trial_time_range_labels) in trial_time_range.items():
        trial_time_range = df[trial_time_range_labels] == trial_time_range_labels
        count_trial_time_range_labels = len(df[trial_time_range_labels])

        data[trial_time_range_labels].append(count_trial_time_range_labels)

    mean_tt = np.mean(df[is_ag])
    data['mean'].append(mean_tt)

    for (error_percent_range_labels) in error_percent_range.items():
        error_percent_range = df[error_percent_range_labels] == error_percent_range_labels
        count_error_percent_range_labels = len(df[error_percent_range_labels])

        data[error_percent_range_labels].append(count_error_percent_range_labels)

    mean_ep = np.mean(df[is_ag])
    data['mean'].append(mean_ep)

    for (frequency_of_backspace_range_labels) in frequency_of_backspace_range.items():
        frequency_of_backspace_range = df[frequency_of_backspace_range_labels] == frequency_of_backspace_range_labels
        count_frequency_of_backspace_range_labels = len(df[frequency_of_backspace_range_labels])

        data[frequency_of_backspace_range_labels].append(count_frequency_of_backspace_range_labels)

    mean_fb = np.mean(df[is_ag])
    data['mean'].append(mean_fb)

    if ag == 'young':
        condition_label = ag
    else:
        condition_label = 'old'

    title = f'Typing on Smartphone x {condition_label} ag'

    df_fig = pd.DataFrame(data, index=index)
    ax = df_fig.plot.bar(rot=0)
    ax.set_xlabel('range')
    ax.set_ylabel('frequency')
    ax.set_title(title)

    fig_name = f'{condition_label}.pdf'
    fig_file = os.path.join(FIG_FOLDER, fig_name)
    plt.savefig(fig_file)
    '''



'''
n = len(sentence_volume_range)
print(n)



for i in range(n):
    print(i)
    print(sentence_volume_range[i])
    print()
'''
