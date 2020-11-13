import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import scipy as scipy
from scipy import stats
from scipy.stats.stats import pearsonr
from scipy.stats import linregress
from sklearn.metrics import r2_score

data = pd.read_csv('JM&CT&SCC+macro.csv')

#fig, ax = plt.subplots()
#ax = sns.swarmplot (x='genotype', y='age', data = myData, color='0.25')
#ax = sns.boxplot (x='genotype', y='age', data = myData, palette='Set1', showfliers=False)
#ax.set_xlabel('Genotype')
#ax.set_ylabel('Age (wks)')
#plt.show()

data.dropna()

data = data[data.Organ == 'SB3']
data = data[data.Who == 'SCC']
data = data[data.Genotype == 'APC/WT']

x = data['CD8/NKG2D'].tolist()
y = data['CD8/TNFa'].tolist()

#ax = sns.jointplot(x='age', y='CD8/IFNg', data = data, size=5, kind='reg')


ax = sns.lmplot(x='CD8/NKG2D', y='CD8/TNFa', data = data, size=5, aspect=1, palette='Set1')
ax.set_xlabels('CD8/NKG2D')
ax.set_ylabels('CD8/TNFa')


print(linregress(x, y))

plt.show()