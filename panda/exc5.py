import pandas as pd
import numpy as np
d={"one":[1,2,3,4,5],"two":[2,2,2,2,2],"letter":["a","a","b","b","c"]}
df=pd.DataFrame(d)
print(df)
print(df["one"].apply(np.sqrt)) #.apply to make any mathmatical operations with help of numpy library

print(df["letter"].map(lambda t:"map_"+t)) # to manipulate the values in the all value