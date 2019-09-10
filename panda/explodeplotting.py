import pandas as pd
import matplotlib.pyplot as plt

data = [10,30,50,10]
fruits=['apples','pears','charries','banans']
s = pd.Series(data,index=fruits,name='the chart')

print(s)
explode=[0,.1,.4,.7]
s.plot.pie(figsize=(10,10),explode=explode)
plt.show()
