# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 13:20:23 2019

@author: Ahmed
"""

import pandas as pd
Sheet1=pd.read_excel(r'C:\Users\Ahmed\OneDrive\Desktop\J&M\panda\salary.xlsx',sheet_name='Tabelle1')
Sheet2=df=pd.read_excel(r'C:\Users\Ahmed\OneDrive\Desktop\J&M\panda\salary.xlsx',sheet_name='zozo')


print(Sheet1,"\n and the")

print(Sheet2['Age']) #we become all the columns
print(Sheet2['Age'][0]) #the first element

weights=Sheet1['weight'].values.tolist() #to make it in the list and work  with it 
names=Sheet2['name'].values.tolist()
print(names)