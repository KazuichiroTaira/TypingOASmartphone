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

sentence_volume_range = {'svr0':[1, 20], 'svr1':[20, 40], 'svr2':[40, 60], 'svr3':[60, 80], 'svr4':[80, 100]}

number_of_letters_range = {'nlr0':[1, 20], 'nlr1':[20, 40], 'nlr2':[40, 60], 'nlr3':[60, 80], 'nlr4':[80, 100]}

frequency_of_trial_range = {'ftr0': [1, 1000], 'ftr2':[1000, 5000], 'ftr3':[5000, 10000], 'ftr4':[10000, 15000],
                            'ftr5':[15000, 20000], 'ftr6':[20000, 50000], 'ftr7':[50000, 100000], 'ftr8':[100000, 150000],
                            'ftr9':[150000, 200000]}

error_percent_range = {'epr0':[0, 0.5], 'epr1':[0.5, 1.0], 'epr2':[1.0, 1.5], 'epr3':[1.5, 2.0]}


for ag in age_group:

    data = {}
    age_group_labels = ['young', 'old']
    sentence_volume_range_labels = ['svr0', 'svr1', 'svr2', 'svr3', 'svr4']
    number_of_letters_range_labels = ['nlr0', 'nlr1', 'nlr2', 'nlr3', 'nlr4']
    frequency_of_trial_range_labels = ['ftr0', 'ftr2', 'ftr3', 'ftr4', 'ftr5', 'ftr6', 'ftr7', 'ftr8', 'ftr9']

    for label in age_group_labels, sentence_volume_range_labels, number_of_letters_range_labels, frequency_of_trial_range_labels:
        data[label] = []

    is_ag = df['condition'] ==ag

''' 

n = len(sentence_volume_range)
print(n)



for i in range(n):
    print(i)
    print(sentence_volume_range[i])
    print()

    '''
    key_month = 'm' + str(i + 1)

    # is_low = df[key_month] == 1
    # sum_low = sum(df[is_low&is_control][key_month])
    # low.append(sum_low)

    for (mood_label, mood_value) in moods.items():
        is_mood = df[key_month] == mood_value
        count_mood = len(df[is_mood & is_ds][key_month])

        data[mood_label].append(count_mood)

    mean_mood = np.mean(df[is_ds][key_month])

    data['mean'].append(mean_mood)



x=0, .9<x<
back_space = {}

for ag in age_group:

    data = {}
    labels = ['young', 'old']
    for label in labels:
        data[label] = []


    is_ds = df['condition'] == ds

    # sum_m1 = sum(df[is_low&is_control]['m1'])
    # sum_m2 = sum(df[is_low&is_control]['m2'])
    # low.append(sum_m1)
    # low.append(sum_m2)

    for i in range(n_months):
        key_month = 'm' + str(i + 1)

        # is_low = df[key_month] == 1
        # sum_low = sum(df[is_low&is_control][key_month])
        # low.append(sum_low)

        for (mood_label, mood_value) in moods.items():

            is_mood = df[key_month] == mood_value
            count_mood = len(df[is_mood & is_ds][key_month])

            data[mood_label].append(count_mood)

        mean_mood = np.mean(df[is_ds][key_month])

        data['mean'].append(mean_mood)

    if ds == 'resident':
        condition_label = ds
    else:
        condition_label = 'visiting'

    title = f'Tension x {condition_label} dog'

    df_fig = pd.DataFrame(data, index=index)
    ax = df_fig.plot.bar(rot=0)
    ax.set_xlabel('month')
    ax.set_ylabel('frequency')
    ax.set_title(title)

    fig_name = f'{condition_label}.pdf'
    fig_file = os.path.join(FIG_FOLDER, fig_name)
    plt.savefig(fig_file)

'''
