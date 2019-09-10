import pandas as pd
import matplotlib.pyplot as plt

data = [10,30,50,10]
s = pd.DataFrame(data,columns=['the chart'],index=['apples','pears','charries','banans'])

print(s)
s.plot()
plt.show()
