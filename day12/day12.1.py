import pandas as pd
data=pd.read_csv('example_csv.csv',index_col=0)
print(data)
print(data.drop(随便一行))
data['3']=data['1']+data['2']
print(data)
