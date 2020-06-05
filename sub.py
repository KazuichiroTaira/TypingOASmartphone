import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os

DATA_FOLDER = 'data'
data_file = os.path.join(DATA_FOLDER, 'smartphone-typing.csv')
df = pd.read_csv(data_file)

print(df)



age_group = ['young', 'old']

n_age_group = len(age_group)


is_young = df['age.group'] == 'young'

# is_sentence_in_0_10 = [x in np.arange(0,10) for x in df['sentence']]
# print(type(is_young))
#print('n entries', len(df))
#print(is_sentence_in_0_10)

sentence_young = df[is_young]['sentence']
print('max value', max(sentence_young))

fig, ax = plt.subplots()
ax.hist(sentence_young, bins=np.arange(0, 51,10))
ax.set_xlabel('sentence')
ax.set_ylabel('# observations')
plt.show()


#print(df[True, ])
#print(df[])



#print(df[df]['sentence'])







'''
        'sentence':[list(sentence.keys())]}

#bin_edges = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

_ = plt.hist(data_file[f'smartphone-typing.csv'], bins=bin_edges)
            # Or (df_swing['smartphone-typing.csv'], bins=10)


# To layout x for each segment of deta.

_ = plt.xlabel('sentence_volume_range')

# _ = plt.xlabel; number_of_letters_range, trial_time_range, error_percent_range, frequency_of_backspace_range

#To discrive each segments of data in age group compariosn

_ = plt.ylabel('young','old')
'''

