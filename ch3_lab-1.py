# -*- coding: utf-8 -*-
"""ch3_lab-1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1CAEJVWWtG7u2lcn_oRCEwvKslTHSpUNP
"""

import pandas as pd
spending_df = pd.read_csv('spending_df.csv',index_col=0)
spending_df

# lab1-1
earning_df = pd.DataFrame({
        '110年薪資收入':[21000, 21000, 22000],
        '110年股票收入':[1000, 0 ,200]
        })
earning_df

# lab1-1
rename_index = {0:'一月',1:'二月',2:'三月'}
earning_df = earning_df.rename(rename_index, axis=0)
earning_df

# lab1-1
property_df = pd.concat([spending_df,earning_df],axis=1)
property_df

# lab1-2
spending_df[(spending_df['110年娛樂費']>=4000)|(spending_df['110年交通費']<1200)]

# lab1-3
spending_df['110年生活費']['二月']

# lab1-4
spending_df.loc['三月']

# lab1-5
spending_df['110年娛樂費'].max()