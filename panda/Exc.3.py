import pandas as pd
import matplotlib.pyplot as plt

data={"country":["Brazil","Russia","India","china","South Africa"],
      "capital":["Brasilien","Moscow","New Dehli","Beijing","Pretoria"],
      "area":[8.516,17.10,3.286,9.597,1.221],"population":[200.4,143.5,1252,1357,52.98]}
print(data)
my_data=pd.DataFrame(data) #it is not array one dimension this is frame
print(my_data.mean())
print(my_data.describe())
my_data.index=["BR","RU","IN","CH","SA"] #to change the index
print(my_data)
