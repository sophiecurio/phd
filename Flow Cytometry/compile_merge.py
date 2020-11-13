import pandas as pd

#path ='New'
#allFiles = glob.glob(path + "/*.csv")
#list_ = []

#df = pd.DataFrame()

df = pd.read_csv('macro.csv')
df1 = pd.read_csv('JM&CT&SCC.csv')
#df2 = pd.read_csv('Mix1_LB_2.csv')

merged = pd.merge(df, df1, how='outer')

#merged = pd.merge(merged, df2, how='outer')
##print(merged)
#
#for file_ in allFiles:
#    df3 = pd.read_csv(file_)
#    merged = pd.merge(df3, merged, how='inner')
##    data = pd.concat(list_)
#    print(file_ + " has been imported.")
    
merged.to_csv('JM&CT&SCC+macro.csv', index=False)