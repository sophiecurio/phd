import pandas as pd
import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt
import scipy.stats as stats
import csv

#organ = 'SB3'
data = pd.read_csv('JM&CT&SCC.csv')
#data = data[data.Organ == organ]
data = data[data.Mix == 'stim']
data = data[data.Timepoint == '18-20']
data = data[data.Genotype == 'APC/WT']

ax = data.groupby("Organ")['CD4/TNFa', 'CD8/TNFa', 'gdT/TNFa', 'NK/TNFa'].mean().plot(kind='bar',  colormap='Accent')
ax.set_facecolor('white')

print(data.groupby("Organ")['CD4/NKG2D', 'CD8/NKG2D', 'gdT/NKG2D', 'NK/NKG2D'].mean())

plt.legend(loc='center left', bbox_to_anchor=(1,0.5))
plt.show()
