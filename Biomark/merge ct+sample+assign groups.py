import pandas as pd
import csv
import glob, os

df = pd.read_csv('ct.csv')
df1 = pd.read_csv('samples.csv')

data = pd.merge(df, df1, how='outer')

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

#Define the groups we want to compare and save them all as individual csv
WT_T = data[(data.Tissue == 'T') & (data.Genotype == 'APC/WT')]
WT_T['Group'] = 'WT_T'
WT_T.to_csv('By group/WT_T.csv')
WT_ST = data[(data.Tissue == 'ST') & (data.Genotype == 'APC/WT')]
WT_ST['Group'] = 'WT_ST'
WT_ST.to_csv('By group/WT_ST.csv')
KO_T = data[(data.Tissue == 'T') & (data.Genotype == 'APC/KO')]
KO_T['Group'] = 'KO_T'
KO_T.to_csv('By group/KO_T.csv')
KO_ST = data[(data.Tissue == 'ST') & (data.Genotype == 'APC/KO')]
KO_ST['Group'] = 'KO_ST'
KO_ST.to_csv('By group/KO_ST.csv')
WT_ctrl = data[(data.Tissue == 'ST') & (data.Genotype == 'WT ctrl')]
WT_ctrl['Group'] = 'WT_ctrl'
WT_ctrl.to_csv('By group/WT_ctrl.csv')
KO_ctrl = data[(data.Tissue == 'ST') & (data.Genotype == 'KO ctrl')]
KO_ctrl['Group'] = 'KO_ctrl'
KO_ctrl.to_csv('By group/KO_ctrl.csv')

#merge the individual csv
path ='By group'
allFiles = glob.glob(path + "/*.csv")
list_ = []

for file_ in allFiles:
    df = pd.read_csv(file_,index_col=None,)
    list_.append(df)
    data = pd.concat(list_)
    print(file_ + " has been imported.")

data.to_csv('ct+sample_info+group.csv')
    