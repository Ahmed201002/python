import pandas as pd
d=[0,1,2,3,4,5,6,7,8,9]
df=pd.DataFrame(d,columns=['Rev'])
print(df)
df['NewCol']=5
print(df)
del df['NewCol']
df['test']=3
df['col']=df['Rev']
print(df)
i=['a','b','c','d','e','f','g','h','i','j']
df.index=i
print(df)
print(df.loc['a']) #to show us the value of the index in all columns
print("and the next Value...")
print(df.loc['i'])
print(df.loc['b':'f'])    #segment of the table
print(df.iloc[0:3])  #determin the Rows too
print(df[['Rev','col']])  # i choose columns
print(df.head())      # by default 5 Rows from Top
print(df.tail(3))  # by default 5 Rows from tail
df.to_csv('My_Data.csv')