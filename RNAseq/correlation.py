import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import os
from scipy import stats
from scipy.stats.stats import pearsonr
from scipy.stats import linregress
from sklearn.metrics import r2_score
from sklearn.linear_model import LinearRegression

#set gene name
gene1 = 'ENSG00000111537'
name1 = 'IFNg'
gene2 = 'ENSG00000213809'
name2 = 'KLRK1'

#read csv & select only CMS and gene column
data = pd.read_csv('expression.csv')
data_gene = data[(data['GeneID'].isin(['CMS', gene1, gene2]))]

#transpose & drop index column so that CMS & gene are the index
data_gene = data_gene.transpose()
df = data_gene.reset_index()
df.columns = df.iloc[0]
df = df.reindex(df.index.drop(0)).reset_index(drop=True)
df.columns.name = None
df = df.iloc[1:]
df = df.drop(['GeneID'], axis = 1)
#df = df.astype(float)
df = df[df.CMS == 'CMS1']


x = df[gene1].tolist()
y = df[gene2].tolist()

print(linregress(x, y))

fig, ax = plt.subplots()
sns.scatterplot(x=gene1, y=gene2, hue='CMS', data=df, palette='Set1')
plt.xlabel(name1)
plt.ylabel(name2)
plt.show()
# fig.savefig(name1 + "_"+ name2 + ".png", dpi=400)

#stats for CMS1 only
cms1 = df[df['CMS'] == 'CMS1']
x = cms1[gene1].tolist()
y = cms1[gene2].tolist()
print(linregress(x, y))

cms1.to_csv('cms1.csv')