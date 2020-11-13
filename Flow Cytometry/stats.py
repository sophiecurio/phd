import pandas as pd
import scipy.stats as stats
import numpy as np

df = pd.read_csv('citro_nkg2d.csv')

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
 
celltype1 = 'NK d7'
celltype2 = 'NK d25'

t1 = df[celltype1].dropna()
t2 = df[celltype2].dropna()

shapiro1 = stats.shapiro(df[celltype1].dropna())
shapiro2 = stats.shapiro(df[celltype2].dropna())

if shapiro1[0] and shapiro2[0] < 0.05: 
    p1 = stats.ttest_ind(t1, t2, equal_var=False).pvalue
    print('normal')
    print(p1, stars(p1))

else:
    p2 = stats.mannwhitneyu(t1, t2).pvalue
    print('not normal')
    print(p2, stars (p2))
        