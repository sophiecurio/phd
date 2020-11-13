import pandas as pd
import glob, os

path ='./'
allFiles = glob.glob(path + "macro/*"+".csv")
list_ = []

for file_ in allFiles:
    df = pd.read_csv(file_,index_col=None,)
    list_.append(df)
    data = pd.concat(list_)
    print(file_ + " has been imported.")
    
data.to_csv('macro.csv', index=False)
