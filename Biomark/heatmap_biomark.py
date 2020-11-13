import pandas as pd
import math
import seaborn as sns
import matplotlib.pyplot as plt
import scipy.stats as stats
import csv
import matplotlib
from matplotlib.colors import LogNorm

matplotlib.rcParams['pdf.fonttype'] = 42

data = pd.read_csv('means.csv')

gene_mean = pd.DataFrame(columns = ['Gene', 'Mean fold change'])

#creates a list with all the gene names, removes duplicates (each gene name only once)
genes = data['Gene'].tolist()
genes = list(dict.fromkeys(genes))

i = 0
for gene in genes:
        data_gene = data.loc[data['Gene'] == gene]
        mean = data_gene['Mean fold change'].mean()
        gene_mean.loc[i] = [gene, mean]
        i += 1


#sorts the gene names by mean fold change from highest expressed to lowest expressed        
gene_mean = gene_mean.sort_values(by='Mean fold change', ascending=False)

#puts the gene names in a list in descending otder
gene_mean = gene_mean['Gene'].tolist()

#puts the dataframe in the right shape
data = data.pivot(index='Gene', columns='Group', values='Mean fold change')

#sets the order of groups
#groups = ['WT_ctrl', 'KO_ctrl', 'WT_ST', 'KO_ST', 'WT_T', 'KO_T']
groups = ['WT_ctrl', 'WT_T', 'KO_T']


#select certain subgroups
TF = ['STAT1', 'STAT3', 'STAT6', 'TBX21', 'RORC', 'NFKB']
chemo = ['CXCL9', 'CXCL10', 'CCL17', 'CCL22', 'CXCR3']
infl = ['TNFA', 'COX2']
myeloid = ['INOS2', 'IL-6', 'MIF']
cytotoxic = ['GzB', 'TRAIL', 'Perforin']
inhibitory = ['PD1', 'CTLA4', 'BTLA', 'Lag3']
antiinfl = ['TGFb', 'IL-10']
IL = ['IL-33', 'IL-15', 'IL-21', 'IL-12', 'IL-23', 'IL-22', 'IL-10']
misc = ['MMP9', 'LIGHT', 'IL-1RB', 'IL-22RA2', 'IL-23R']

to_include = ['GzB', 'TGFb', 'IL-15', 'TNFA', 'CTLA4', 'PD-L1', 'Lag3', 'PD1', 'IL-6', 'Perforin', 'IL-33', 'COX-2', 'FOXP3', 'TRAIL']

delete = [x for x in gene_mean if x not in to_include]
print(delete)
data = data.drop(delete)

data = data.reindex(columns=groups, index=gene_mean)
data = data.dropna()
# data = data.drop(['GAPDH'])
# data = data.drop(['TNFA'])
# data = data.drop(['MIF'])
# data = data.drop(['CCL17'])


print(data)

#displays the data as log
log_norm = LogNorm(vmin=data.min().min(), vmax=data.max().max())
cbar_ticks = [math.pow(10, i) for i in range(math.floor(math.log10(data.min().min())), 1+math.ceil(math.log10(data.max().max())))]

fig, ax = plt.subplots(figsize=(6,5)) 
sns.heatmap(data, norm = log_norm, cbar_kws={"ticks": cbar_ticks}, xticklabels=True, yticklabels=True, cmap="coolwarm", ax = ax)
plt.savefig('WT vs KO T selected genes.png', transparent = True)
plt.show()
