# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 07:38:56 2017

@author: maheshp
"""

from pandas_datareader import DataReader
from datetime import datetime
import pandas as pd

ibm = DataReader('C',  'yahoo', datetime(2010, 1, 1), datetime(2012, 1, 1))
#print(ibm['Adj Close'])
excel1 = pd.ExcelWriter('C.xlsx', engine='xlsxwriter')
ibm.to_excel(excel1,sheet_name='Sheet1')
excel1.save()




