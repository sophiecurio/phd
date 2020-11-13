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
gene = 'ULBP1'

df = pd.read_csv('combined_1.csv')
#csv file containing one column for each gene and pathological feature/ overall survival time and individual patients as rows


# # T test
# t1 = df[df.kras_mutation_found=='YES'][gene]
# t2 = df[df.kras_mutation_found=='NO'][gene]
# p1 = stats.ttest_ind(t1, t2, equal_var=False).pvalue
# print('YES vs NO', p1, stars(p1))


fig, ax = plt.subplots()
sns.swarmplot (x='pathologic_stage', y=gene, order = ['Stage I', 'Stage IIA', 'Stage II', 'Stage IIIA', 'Stage IIIB', 'Stage IIIC', 'Stage IVA', 'Stage IVB'], data = df, color='0.25', ax = ax)
sns.boxplot (x='pathologic_stage', width=0.8, y=gene, order = ['Stage I', 'Stage IIA', 'Stage II', 'Stage IIIA', 'Stage IIIB', 'Stage IIIC', 'Stage IVA', 'Stage IVB'], data = df, palette='Set1', showfliers=False, ax = ax)
ax.set(ylabel=gene)
#ax.set(ylim=(0,1))
sns.despine()

# #SIGNIFICANCE BARS
# x1, x2 = 0, 1 
# y, h, col = df[gene].max() + df[gene].max()*0.3, 0, 'k'
# plt.text((x1+x2)*.5, y+h, stars(p1), ha='center', va='bottom', color=col)
# ax.plot([x1, x1, x2, x2], [y, y+h, y+h, y], color=col, clip_on=False, lw=1.0)
plt.show()

# fig.savefig(gene+"_kras", dpi=400)

