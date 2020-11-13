import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import scipy.stats as stats
import numpy as np

import csv

#population_list = []
#with open('populations.csv') as csvfile:
#        for row in csv.reader(csvfile):
#                population_list.append(row[0])
#
#del population_list[0]
##print(population_list)


#definition of stars
def stars(p):
    if p < 0.0001:
        return '****'
    elif (p < 0.001):
        return '***'
    elif (p < 0.01):
        return '**'
    elif (p < 0.05):
        return '*'
    else:
        return 'ns'

organ = ['SB3', 'LB', 'MLN']
timepoint = '18-20'
data = pd.read_csv('JM&CT&SCC+macro.csv')
# data = data[data.Organ == organ]
data = data[data.Timepoint == timepoint]
data = data[data.Genotype == 'APC/WT']

#not equal unstim => JM/CT data isn't labelled stim or unstim
data = data[data.Mix == 'unstim']
#data = data[data.Who == 'JM']


Tcells = ['gdT/PD-1', 'gdT/NKG2D', 'gdT/CD107a']

i = 0
fig, axes_group = plt.subplots(1, len(Tcells), sharex=True, sharey=True, figsize=(8, 3))
for axes in axes_group.flatten():
    sns.swarmplot (x='Organ', y=Tcells[i], order = ['LB', 'SB3'], data = data, color='0.25', ax = axes)
    sns.boxplot (x='Organ', width=0.8, y=Tcells[i], order = ['LB', 'SB3'], data = data, palette='Set2', showfliers=False, ax = axes)
#     t1 = data[data.Genotype=='APC/WT'][Tcells[i]].dropna()
#     t2 = data[data.Genotype=='APC/KO'][Tcells[i]].dropna()
#     p1 = stats.ttest_ind(t1, t2, equal_var=True).pvalue
#     print(p1)
#    #    print('WT vs. KO', p1, stars(p1))
       
#     x1, x2 = 0, 1
#     y, h, col = data[Tcells[i]].max() + data[Tcells[i]].max()*0.2, 0, 'k'
#     axes.plot([x1, x1, x2, x2], [y, y+h, y+h, y], color=col, clip_on=False, lw=1.0)
#     axes.text((x1+x2)*.5, y+h, stars(p1), ha='center', va='bottom', color=col)

    i = i+1   
    sns.despine()
#fig.savefig('NK_func_'+timepoint+organ, dpi=400)       
plt.show()