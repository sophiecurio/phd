import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import scipy as scipy
from scipy import stats
from scipy.stats.stats import pearsonr
from scipy.stats import linregress
from sklearn.metrics import r2_score

data = pd.read_csv('merged_phylum.csv')
#data containing microbiota analysis, flow cytometry analysis and macroscopic parameters

#fig, ax = plt.subplots()
#ax = sns.swarmplot (x='genotype', y='age', data = myData, color='0.25')
#ax = sns.boxplot (x='genotype', y='age', data = myData, palette='Set1', showfliers=False)
#ax.set_xlabel('Genotype')
#ax.set_ylabel('Age (wks)')
#plt.show()

data = data[(data['Timepoint_faeces'].isin(['18']))]
#only select data relating to ileum (SB3)
data = data[(data['Organ'].isin(['SB3']))]
data.dropna()


# data = data[data.Organ == 'SB3']
# data = data[data.Who == 'SCC']
# data = data[data.Genotype == 'APC/WT']

x_par = 'D_0__Bacteria;D_1__Actinobacteria'
y_par = 'CD4/PD-1'

x = data[x_par].tolist()
y = data[y_par].tolist()

#ax = sns.jointplot(x='age', y='CD8/IFNg', data = data, size=5, kind='reg')


ax = sns.lmplot(x=x_par, y=y_par, data = data, size=5, aspect=1, palette='Set1')
ax.set_xlabels(x_par)
ax.set_ylabels(y_par)

print(x)
print(y)

print(linregress(x, y))

plt.show()