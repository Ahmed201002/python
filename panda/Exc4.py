import pandas as pd

names=['Bob','Jassica','Mary','John','Mel']
births=[968,155,77,578,973]
BabyDataSet=list(zip(names,births))
print(BabyDataSet)
df=pd.DataFrame(BabyDataSet,columns=["Names","Births"]
                ,index=["B","J","M","J","M"])
print(df.head(1))
print("Max Birth:",df['Births'].max()) # i determine which colums und what i want
print("Sum Births",df["Births"].sum())

df=df.sort_values(['Births']) #we have ony option ascending
print(df)
print("************************")
df=df.sort_values(['Births'],ascending=False) #we have ony option ascending
print(df)