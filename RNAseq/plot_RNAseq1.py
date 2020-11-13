import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import scipy.stats as stats
import math

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

#set gene name
gene = 'ENSG00000213809'
name = 'KLRK1'

#read csv & select only CMS and gene column
data = pd.read_csv('expression.csv')
data_gene = data[(data['GeneID'].isin(['CMS' , gene]))]


#transpose & drop index column so that CMS & gene are the index
data_gene = data_gene.transpose()
df = data_gene.reset_index()
df.columns = df.iloc[0]
df = df.reindex(df.index.drop(0)).reset_index(drop=True)
df.columns.name = None
df = df.iloc[1:]
print(df)


#stats
#tests whether it is normally distributed or not; p > 0.05 means it is normally distributed
print(stats.shapiro(df.CMS=='CMS1'))

#T test
t1 = df[df.CMS=='CMS1'][gene]
t2 = df[df.CMS=='CMS2'][gene]
p1 = stats.ttest_ind(t1, t2, equal_var=False).pvalue
print('CMS1 vs. 2', p1, stars(p1))

t1 = df[df.CMS=='CMS1'][gene]
t2 = df[df.CMS=='CMS3'][gene]
p2 = stats.ttest_ind(t1, t2, equal_var=False).pvalue
print('CMS1 vs. 3', p2, stars(p2))

t1 = df[df.CMS=='CMS1'][gene]
t2 = df[df.CMS=='CMS4'][gene]
p3 = stats.ttest_ind(t1, t2, equal_var=False).pvalue
print('CMS1 vs. 4', p3, stars(p3))

t1 = df[df.CMS=='CMS2'][gene]
t2 = df[df.CMS=='CMS3'][gene]
p4 = stats.ttest_ind(t1, t2, equal_var=False).pvalue
print('CMS2 vs. 3', p4, stars(p4))

t1 = df[df.CMS=='CMS3'][gene]
t2 = df[df.CMS=='CMS4'][gene]
p5 = stats.ttest_ind(t1, t2, equal_var=False).pvalue
print('CMS3 vs. 4', p4, stars(p4))

fig, ax = plt.subplots()
sns.swarmplot (x='CMS', y=gene, order = ['CMS1', 'CMS2', 'CMS3', 'CMS4'], data = df, color='0.25', ax = ax)
sns.boxplot (x='CMS', width=0.8, y=gene, order = ['CMS1', 'CMS2', 'CMS3', 'CMS4'], data = df, palette='Set1', showfliers=False, ax = ax)
ax.set(ylabel=name)
#ax.set(ylim=(0,1))
sns.despine()
#plt.show()

#SIGNIFICANCE BARS
x1, x2 = 0, 1 
y, h, col = df[gene].max() + df[gene].max()*0.3, 0, 'k'
plt.text((x1+x2)*.5, y+h, stars(p1), ha='center', va='bottom', color=col)
ax.plot([x1, x1, x2, x2], [y, y+h, y+h, y], color=col, clip_on=False, lw=1.0)

x1, x2 = 0, 2 
y, h, col = df[gene].max() + df[gene].max()*0.2, 0, 'k'
plt.text((x1+x2)*.5, y+h, stars(p2), ha='center', va='bottom', color=col)
ax.plot([x1, x1, x2, x2], [y, y+h, y+h, y], color=col, clip_on=False, lw=1.0)

x1, x2 = 0, 3 
y, h, col = df[gene].max() + df[gene].max()*0.1, 0, 'k'
plt.text((x1+x2)*.5, y+h, stars(p3), ha='center', va='bottom', color=col)
ax.plot([x1, x1, x2, x2], [y, y+h, y+h, y], color=col, clip_on=False, lw=1.0)

x1, x2 = 1, 2 
y, h, col = df[gene].max() + df[gene].max()*0.4, 0, 'k'
plt.text((x1+x2)*.5, y+h, stars(p4), ha='center', va='bottom', color=col)
ax.plot([x1, x1, x2, x2], [y, y+h, y+h, y], color=col, clip_on=False, lw=1.0)

x1, x2 = 2, 3 
y, h, col = df[gene].max() + df[gene].max()*0.3, 0, 'k'
plt.text((x1+x2)*.5, y+h, stars(p5), ha='center', va='bottom', color=col)
ax.plot([x1, x1, x2, x2], [y, y+h, y+h, y], color=col, clip_on=False, lw=1.0)

fig.savefig(name+".png", dpi=400)

