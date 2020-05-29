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

sentence_volume = {'upto20': [1, 20], 'upto40': 21-40, 'uptp60': 41-60, 'upto80': 61-80, 'upto100': 81-100}

number_of_letters = {'less20': 1-19, 'less40': 20-39, 'less60': 40-59, 'less80': 60-79, 'less100': 20-99}

trial_time = {'less1000': 1-999, 'less5000': 1000-4999, 'less10000': 5000-9999, 'less15000': 10000-14999,
              'less20000': 15000-19999, 'less50000': 20000-49999, 'less100000': 50000-99999,
              'less150000': 100000-149999, 'less200000': 150000-199999}


error_percent = {'noerror':0, 'errorover0.5': 0.5-0.999 'errorover1.0': 1.0-1.4999    'errorover1.5': 1.5-2.0, }

x=0, .9<x<
back_space = {}

for ds in age_group:

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
