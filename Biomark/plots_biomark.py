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

print(genes)


#only select data that passed the manual call
data = data.loc[data['Manual Call'] == 'Pass']

for x in genes:
    fig, ax = plt.subplots()
    data_gene = data.loc[data['Gene'] == x]    
    sns.boxplot (x='Group', width=0.8, y='Fold change', order = ['WT_ctrl', 'KO_ctrl', 'WT_ST', 'KO_ST', 'WT_T', 'KO_T'], data = data_gene, palette='Set1', showfliers=False, ax = ax)
    sns.swarmplot (x='Group', y='Fold change', order = ['WT_ctrl', 'KO_ctrl', 'WT_ST', 'KO_ST', 'WT_T', 'KO_T'], data = data_gene, color='0.25', ax = ax)
    fig.suptitle(x)
        
    t1 = data_gene[data_gene.Group=='WT_T']['Fold change'].dropna()
    t2 = data_gene[data_gene.Group=='KO_T']['Fold change'].dropna()
    
    if len(t1) > 2 and len(t2) > 2:
        t1_norm, p1 = shapiro(t1)
        t2_norm, p2 = shapiro(t2)
        
        if t1_norm > 0.05 and t2_norm > 0.05:
            p1 = stats.ttest_ind(t1, t2).pvalue
        else:
            p1 = stats.mannwhitneyu(t1, t2).pvalue
            
        x1, x2 = 4, 5
        y, h, col = data_gene['Fold change'].max() + data_gene['Fold change'].max()*0.02, 0, 'k'
        ax.plot([x1, x1, x2, x2], [y, y+h, y+h, y], color=col, clip_on=False, lw=1.0)
        ax.text((x1+x2)*.5, y+h, stars(p1), ha='center', va='bottom', color=col)
    else:
        print('not enough datapoints') 
        
        
        
    t3 = data_gene[data_gene.Group=='WT_ST']['Fold change'].dropna()
    t4 = data_gene[data_gene.Group=='KO_ST']['Fold change'].dropna()
    
    if len(t3) > 2 and len(t4) > 2:        
        
        t3_norm, p3 = shapiro(t3)
        t4_norm, p4 = shapiro(t4)
    
        
        if t3_norm > 0.05 and t4_norm > 0.05:
            p2 = stats.ttest_ind(t3, t4).pvalue
        else:
            p2 = stats.mannwhitneyu(t3, t4).pvalue
        
        x1, x2 = 2, 3
        y, h, col = data_gene['Fold change'].max() + data_gene['Fold change'].max()*0.02, 0, 'k'
        ax.plot([x1, x1, x2, x2], [y, y+h, y+h, y], color=col, clip_on=False, lw=1.0)
        ax.text((x1+x2)*.5, y+h, stars(p2), ha='center', va='bottom', color=col)
    else:
        print('not enough datapoints')
        
        
        
        
    t5 = data_gene[data_gene.Group=='WT_ctrl']['Fold change'].dropna()
    t6 = data_gene[data_gene.Group=='KO_ctrl']['Fold change'].dropna()    
        
    if len(t5) > 2 and len(t6) > 2:     
        t5_norm, p5 = shapiro(t5)
        t6_norm, p6 = shapiro(t6)
        
        if t5_norm > 0.05 and t6_norm > 0.05:
            p3 = stats.ttest_ind(t5, t6).pvalue
        else:
            p3 = stats.mannwhitneyu(t5, t6).pvalue
        
        x1, x2 = 0, 1
        y, h, col = data_gene['Fold change'].max() + data_gene['Fold change'].max()*0.02, 0, 'k'
        ax.plot([x1, x1, x2, x2], [y, y+h, y+h, y], color=col, clip_on=False, lw=1.0)
        ax.text((x1+x2)*.5, y+h, stars(p3), ha='center', va='bottom', color=col)
    
    else:
        print('not enough datapoints')
    plt.savefig(x+'_plot.png')
    
plt.show()