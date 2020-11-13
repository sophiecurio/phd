import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import scipy.stats as stats

import csv

population_list = []
with open('populations_stim.csv') as csvfile:
        for row in csv.reader(csvfile):
                population_list.append(row[0])

del population_list[0]
#print(population_list)


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

organ = 'SB3'
data = pd.read_csv('unstim.csv')
data = data[data.Organ == organ]
data = data[data.Mix == 'unstim']

cells = ['NK/CD107a']

c = ['Mouse']

i = 0
x = 0

fig, axes_group = plt.subplots(3, 1, sharex=True, sharey=False, figsize=(5, 10))
for axes in axes_group.flatten():
        palette = sns.color_palette("hls", n_colors=len(c[x]))
        sns.swarmplot (x='Genotype', y=cells[i], order = ['APC/WT', 'APC/KO'], data = data, color='0.25', ax = axes, palette = palette, hue=c[x])
        sns.boxplot (x='Genotype', width=0.8, y=cells[i], data = data, order=['APC/WT', 'APC/KO'], palette='Set1', showfliers=False, ax = axes)
        axes.legend(loc='right', bbox_to_anchor=(1.75, 0.5), ncol=1)
        
        t1 = data[data.Genotype=='APC/WT'][cells[i]].dropna()
        t2 = data[data.Genotype=='APC/KO'][cells[i]].dropna()
        p1 = stats.ttest_ind(t1, t2, equal_var=True).pvalue
        print(p1)
    #    print('WT vs. KO', p1, stars(p1))
        
        x1, x2 = 0, 1
        y, h, col = data[cells[i]].max() + data[cells[i]].max()*0.2, 0, 'k'
        axes.plot([x1, x1, x2, x2], [y, y+h, y+h, y], color=col, clip_on=False, lw=1.0)
        axes.text((x1+x2)*.5, y+h, stars(p1), ha='center', va='bottom', color=col)
    
        i = i+1   
        sns.despine()
#        fig.savefig(organ+'unstim', dpi=400)
        
plt.show()


#i = 0
#fig, axes_group = plt.subplots(10, 13, sharex=True, sharey=False, figsize=(30, 40))
#for axes in axes_group.flatten():
#        sns.swarmplot (x='Genotype', y=population_list[i], order = ['APC/WT', 'APC/KO'], data = data, color='0.25', ax = axes)
#        sns.boxplot (x='Genotype', width=0.8, y=population_list[i], data = data, order=['APC/WT', 'APC/KO'], palette='Set1', showfliers=False, ax = axes)
#        
#        t1 = data[data.Genotype=='APC/WT'][population_list[i]].dropna()
#        t2 = data[data.Genotype=='APC/KO'][population_list[i]].dropna()
#        p1 = stats.ttest_ind(t1, t2, equal_var=False).pvalue
#    #    print('WT vs. KO', p1, stars(p1))
#        
#        x1, x2 = 0, 1
#        y, h, col = data[population_list[i]].max() + data[population_list[i]].max()*0.2, 0, 'k'
#        axes.plot([x1, x1, x2, x2], [y, y+h, y+h, y], color=col, clip_on=False, lw=1.0)
#        axes.text((x1+x2)*.5, y+h, stars(p1), ha='center', va='bottom', color=col)
#    
#        i = i+1   
#        sns.despine()
#        fig.savefig(organ+'scaled', dpi=400)
#        
#plt.show()
       
##print(data)
#subsets2 = ['CD11b', 'B cells', 'B220high', 'B220int', 'CD11bhigh', 'CD11bint', 'CD3', 'NK', 'gdT']
#Tcells = ['CD3', 'CD4', 'CD8', 'gdT', 'Treg']
#Myeloid = ['DCs', 'Eosinophils', 'M-MDSC', 'PMN-MDSC', 'M2']
#NK_func = ['NK_DNAM', 'NK_NKG2D', 'NK_NKp46', 'NKT_DNAM', 'NKT_NKG2D', 'NKT_NKp46']
#Tcell_func = ['CD4_DNAM', 'CD4_NKG2D', 'CD4_NKp46', 'CD8_DNAM', 'CD8_NKG2D', 'CD8_NKp46']
#B220 = ['B220high/CD11b+/F4_80high', 'B220high/CD11b+/F4_80int', 'B220high/CD11b+/Gr-1high', 'B220high/CD11b+/Gr-1int', 'B220high/CD11b+/Gr-1+F4_80+', 'B220int/CD11b+/F4_80+', 'B220int/CD11b+/Gr-1+']
#CD11b = ['B220-CD11b+/F4_80high', 'B220-CD11b+/F4_80int', 'B220-CD11b+/Gr-1high', 'B220-CD11b+/Gr-1int', 'B220-CD11b+/Gr-1+F4_80+', 'CD11bhigh/F4_80high', 'CD11bhigh/F4_80int', 'CD11bhigh/Gr-1+', 'CD11bint/F4_80+', 'CD11b int/Gr-1+']
#Tumor = ['MULT_T', 'MULT_MFI_T']
#
#
#i = 0
#fig, axes_group = plt.subplots(3, 3, sharex=True, sharey=True, figsize=(7,7))
#for axes in axes_group.flatten():
#    sns.swarmplot (x='Genotype', y=subsets2[i], order=['APC/WT', 'APC/KO'], data = data, color='0.25', ax = axes)
#    sns.boxplot (x='Genotype', width=0.8, y=subsets2[i], data = data, order=['APC/WT', 'APC/KO'], palette='Set1', showfliers=False, ax = axes)
#    
#    t1 = data[data.Genotype=='APC/WT'][subsets2[i]].dropna()
#    t2 = data[data.Genotype=='APC/KO'][subsets2[i]].dropna()
#    p1 = stats.ttest_ind(t1, t2, equal_var=False).pvalue
##    print('WT vs. KO', p1, stars(p1))
#    
#    x1, x2 = 0, 1
#    y, h, col = data[subsets2[i]].max() + data[subsets2[i]].max()*0.2, 0, 'k'
#    axes.plot([x1, x1, x2, x2], [y, y+h, y+h, y], color=col, clip_on=False, lw=1.0)
#    axes.text((x1+x2)*.5, y+h, stars(p1), ha='center', va='bottom', color=col)
#
#    i = i+1   
#    sns.despine()
#    fig.savefig(organ+' subsets2.png', dpi=400)
#
#i = 0
#fig, axes_group = plt.subplots(1, 5, sharex=True, sharey=True, figsize=(7,4))
#for axes in axes_group.flatten():
#    sns.swarmplot (x='Genotype', y=Tcells[i], order=['APC/WT', 'APC/KO'], data = data, color='0.25', ax = axes)
#    sns.boxplot (x='Genotype', width=0.8, y=Tcells[i], data = data, order=['APC/WT', 'APC/KO'], palette='Set1', showfliers=False, ax = axes)
#    
#    t1 = data[data.Genotype=='APC/WT'][Tcells[i]].dropna()
#    t2 = data[data.Genotype=='APC/KO'][Tcells[i]].dropna()
#    p1 = stats.ttest_ind(t1, t2, equal_var=False).pvalue
##    print('WT vs. KO', p1, stars(p1))
#    
#    x1, x2 = 0, 1
#    y, h, col = data[Tcells[i]].max() + data[Tcells[i]].max()*0.2, 0, 'k'
#    axes.plot([x1, x1, x2, x2], [y, y+h, y+h, y], color=col, clip_on=False, lw=1.0)
#    axes.text((x1+x2)*.5, y+h, stars(p1), ha='center', va='bottom', color=col)
#
#    i = i+1   
#    sns.despine()
#    fig.savefig(organ+' Tcells.png', dpi=400)
#    
#    
#i = 0
#fig, axes_group = plt.subplots(1, 5, sharex=True, sharey=True, figsize=(7,5))
#for axes in axes_group.flatten():
#    sns.swarmplot (x='Genotype', y=Myeloid[i], order=['APC/WT', 'APC/KO'], data = data, color='0.25', ax = axes)
#    sns.boxplot (x='Genotype', width=0.8, y=Myeloid[i], data = data, order=['APC/WT', 'APC/KO'], palette='Set1', showfliers=False, ax = axes)
#    
#    t1 = data[data.Genotype=='APC/WT'][Myeloid[i]].dropna()
#    t2 = data[data.Genotype=='APC/KO'][Myeloid[i]].dropna()
#    p1 = stats.ttest_ind(t1, t2, equal_var=False).pvalue
##    print('WT vs. KO', p1, stars(p1))
#    
#    x1, x2 = 0, 1
#    y, h, col = data[Myeloid[i]].max() + data[Myeloid[i]].max()*0.2, 0, 'k'
#    axes.plot([x1, x1, x2, x2], [y, y+h, y+h, y], color=col, clip_on=False, lw=1.0)
#    axes.text((x1+x2)*.5, y+h, stars(p1), ha='center', va='bottom', color=col)
#
#    i = i+1   
#    sns.despine()
#    fig.savefig(organ+' Myeloid.png', dpi=400)
#    
#i = 0
#fig, axes_group = plt.subplots(2, 3, sharex=True, sharey=True, figsize=(5,7))
#for axes in axes_group.flatten():
#    sns.swarmplot (x='Genotype', y=NK_func[i], order=['APC/WT', 'APC/KO'], data = data, color='0.25', ax = axes)
#    sns.boxplot (x='Genotype', width=0.8, y=NK_func[i], data = data, order=['APC/WT', 'APC/KO'], palette='Set1', showfliers=False, ax = axes)
#    
#    t1 = data[data.Genotype=='APC/WT'][NK_func[i]].dropna()
#    t2 = data[data.Genotype=='APC/KO'][NK_func[i]].dropna()
#    p1 = stats.ttest_ind(t1, t2, equal_var=False).pvalue
##    print('WT vs. KO', p1, stars(p1))
#    
#    x1, x2 = 0, 1
#    y, h, col = data[NK_func[i]].max() + data[NK_func[i]].max()*0.2, 0, 'k'
#    axes.plot([x1, x1, x2, x2], [y, y+h, y+h, y], color=col, clip_on=False, lw=1.0)
#    axes.text((x1+x2)*.5, y+h, stars(p1), ha='center', va='bottom', color=col)
#
#    i = i+1 
#    sns.despine()
#    fig.savefig(organ+' NK func.png', dpi=400)
#    
#    
#i = 0
#fig, axes_group = plt.subplots(2, 3, sharex=True, sharey=True, figsize=(5,7))
#for axes in axes_group.flatten():
#    sns.swarmplot (x='Genotype', y=Tcell_func[i], order=['APC/WT', 'APC/KO'], data = data, color='0.25', ax = axes)
#    sns.boxplot (x='Genotype', width=0.8, y=Tcell_func[i], data = data, order=['APC/WT', 'APC/KO'], palette='Set1', showfliers=False, ax = axes)
#    
#    t1 = data[data.Genotype=='APC/WT'][Tcell_func[i]].dropna()
#    t2 = data[data.Genotype=='APC/KO'][Tcell_func[i]].dropna()
#    p1 = stats.ttest_ind(t1, t2, equal_var=False).pvalue
##    print('WT vs. KO', p1, stars(p1))
#    
#    x1, x2 = 0, 1
#    y, h, col = data[Tcell_func[i]].max() + data[Tcell_func[i]].max()*0.2, 0, 'k'
#    axes.plot([x1, x1, x2, x2], [y, y+h, y+h, y], color=col, clip_on=False, lw=1.0)
#    axes.text((x1+x2)*.5, y+h, stars(p1), ha='center', va='bottom', color=col)
#
#    i = i+1 
#    sns.despine()
#    fig.savefig(organ+' T cell func.png', dpi=400)
#
#    
#i = 0
#fig, axes_group = plt.subplots(2, 3, sharex=True, sharey=True, figsize=(5,7))
#for axes in axes_group.flatten():
#    sns.swarmplot (x='Genotype', y=B220[i], order=['APC/WT', 'APC/KO'], data = data, color='0.25', ax = axes)
#    sns.boxplot (x='Genotype', width=0.8, y=B220[i], data = data, order=['APC/WT', 'APC/KO'], palette='Set1', showfliers=False, ax = axes)
#    
#    t1 = data[data.Genotype=='APC/WT'][B220[i]].dropna()
#    t2 = data[data.Genotype=='APC/KO'][B220[i]].dropna()
#    p1 = stats.ttest_ind(t1, t2, equal_var=False).pvalue
##    print('WT vs. KO', p1, stars(p1))
#    
#    x1, x2 = 0, 1
#    y, h, col = data[B220[i]].max() + data[B220[i]].max()*0.2, 0, 'k'
#    axes.plot([x1, x1, x2, x2], [y, y+h, y+h, y], color=col, clip_on=False, lw=1.0)
#    axes.text((x1+x2)*.5, y+h, stars(p1), ha='center', va='bottom', color=col)
#
#    i = i+1 
#    sns.despine()
#    fig.savefig(organ+' B220.png', dpi=400)
#    
#
#i = 0
#fig, axes_group = plt.subplots(2, 5, sharex=True, sharey=True, figsize=(10,7))
#for axes in axes_group.flatten():
#    sns.swarmplot (x='Genotype', y=CD11b[i], order=['APC/WT', 'APC/KO'], data = data, color='0.25', ax = axes)
#    sns.boxplot (x='Genotype', width=0.8, y=CD11b[i], data = data, order=['APC/WT', 'APC/KO'], palette='Set1', showfliers=False, ax = axes)
#    
#    t1 = data[data.Genotype=='APC/WT'][CD11b[i]].dropna()
#    t2 = data[data.Genotype=='APC/KO'][CD11b[i]].dropna()
#    p1 = stats.ttest_ind(t1, t2, equal_var=False).pvalue
##    print('WT vs. KO', p1, stars(p1))
#    
#    x1, x2 = 0, 1
#    y, h, col = data[CD11b[i]].max() + data[CD11b[i]].max()*0.2, 0, 'k'
#    axes.plot([x1, x1, x2, x2], [y, y+h, y+h, y], color=col, clip_on=False, lw=1.0)
#    axes.text((x1+x2)*.5, y+h, stars(p1), ha='center', va='bottom', color=col)
#
#    i = i+1 
#    sns.despine()
#    fig.savefig(organ+' CD11b.png', dpi=400)
#    
#    
#i = 0
#fig, axes_group = plt.subplots(1, 2, sharex=True, sharey=True, figsize=(5,4))
#for axes in axes_group.flatten():
#    sns.swarmplot (x='Genotype', y=Tumor[i], order=['APC/WT', 'APC/KO'], data = data, color='0.25', ax = axes)
#    sns.boxplot (x='Genotype', width=0.8, y=Tumor[i], data = data, order=['APC/WT', 'APC/KO'], palette='Set1', showfliers=False, ax = axes)
#    
#    t1 = data[data.Genotype=='APC/WT'][Tumor[i]].dropna()
#    t2 = data[data.Genotype=='APC/KO'][Tumor[i]].dropna()
#    p1 = stats.ttest_ind(t1, t2, equal_var=False).pvalue
##    print('WT vs. KO', p1, stars(p1))
#    
#    x1, x2 = 0, 1
#    y, h, col = data[Tumor[i]].max() + data[Tumor[i]].max()*0.2, 0, 'k'
#    axes.plot([x1, x1, x2, x2], [y, y+h, y+h, y], color=col, clip_on=False, lw=1.0)
#    axes.text((x1+x2)*.5, y+h, stars(p1), ha='center', va='bottom', color=col)
#
#    i = i+1 
#    sns.despine()
#    fig.savefig(organ+' tumor.png', dpi=400)
#    
#plt.show()