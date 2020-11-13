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
gene1 = 'KLRK1'
gene2 = 'IFNG'

df = pd.read_csv('combined_1.csv')
#csv file containing one column for each gene and pathological feature/ overall survival time and individual patients as rows
df = df[[gene1, gene2]]

df = df.replace(0, np.nan)
df = df.dropna()


x = df[gene1].tolist()
y = df[gene2].tolist()

print(linregress(x, y))
slope, intercept, r_value, p_value, std_err = stats.linregress(x,y)
p = ('p = ' + str(p_value))

fig, ax = plt.subplots()
sns.scatterplot(x=gene1, y=gene2, data=df, palette='Set1')
plt.xlabel(gene1)
plt.ylabel(gene2)
plt.title(p)
plt.show()
fig.savefig(gene1 + "_"+ gene2 + ".png", dpi=400)

