import pandas as pd
import matplotlib.pyplot as plt

data = [10,30,50,10]
fruits=['apples','pears','charries','banans']
s = pd.Series(data,index=fruits,name='the chart')

print(s)
s.plot.pie(figsize=(10,10))
plt.show()
