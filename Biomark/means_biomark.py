import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import scipy.stats as stats
import csv
import glob, os
from scipy.stats import shapiro

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

data = pd.read_csv('ct+sample_info+group.csv')

assays = pd.read_csv('assays.csv')
genes = assays['Gene'].tolist()
genes.remove('NKG2D')
genes.remove('HPRT')
genes.remove('IL-17F')
genes.remove('IL-18')
#genes.remove('IL1R8')
genes.remove('IL-18')


groups = ['WT_ctrl', 'KO_ctrl', 'WT_T', 'WT_ST', 'KO_T', 'KO_ST']

df_mean = pd.DataFrame(columns = ['Gene', 'Mean fold change', 'Group'])

if data[data['Manual Call'] == 'Fail']:
    print('failed')

#only select data that passed the manual call
#data = data.loc[data['Manual Call'] == 'Pass']
#
#i = 0
#for group in groups:
#    for gene in genes:
#        data_gene = data.loc[data['Gene'] == gene]
#        data_gene = data_gene.loc[data_gene['Group'] == group]
#        mean = data_gene['Fold change'].mean()
#        df_mean.loc[i] = [gene, mean, group]
#        i += 1
#
#df_mean.to_csv('means.csv')

    