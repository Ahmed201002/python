import pandas as pd
import matplotlib.pyplot as plt # to show the plotting

#install it with commandline pip install pandas
data=[100,120,140,180,200,210,240]
s=pd.Series(data) # with counter
s_list=s.values.tolist() # to make it in lists to work with it
#print(s.describe()) # to make describe for all the values
s.plot(kind="bar")
plt.show()

