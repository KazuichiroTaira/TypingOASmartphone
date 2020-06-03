import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os
'''

DATA_FOLDER = 'data'
FIG_FOLDER = 'fig'

os.makedirs(FIG_FOLDER, exist_ok=True)

data_file = os.path.join(DATA_FOLDER, 'smartphone-typing.csv')
df = pd.read_csv(data_file)

# Number of people 'low' for the month 1, month 2, etc. for visiting

'''


age_group = ['young', 'old']


sentence_volume_range = ([1, 20], [20,40], [40,60], [60,80], [80,100])

number_of_letters_range = ([1,20], [20,40], [40,60], [60,80], [80,100])

trial_time_range = ([1,1000], [1000,5000], [5000,10000], [10000,15000],
                    [15000,20000], [20000,50000], [50000,100000], [100000,150000], [150000,200000])

error_percent_range = ([0,0.5], [0.5,1.0], [1.0,1.5], [1.5,2.0])


#plt.hist(x, bins)
#bins = np.(low, high, num of poll)
#x = np.random.normal(low, high, num of poll)