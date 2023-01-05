'''
The objective of this assignment is to clean the csv file of the attendance.
The path to the csv file is "attendance_to_clean.csv"
You can find it in the instruction folder.
List of installed and authorized packages :
    - csv
    - pandas
    - datetime
    - numpy
You cannot use other packages than the listed ones (except built-in default package in python).
You can write you code after this comment :
'''

#Your code here:
import pandas as pd
import csv
import datetime
import numpy as np
na_value=['error','two','na','_'] 
df = pd.read_csv("attendance_to_clean.csv", na_values = na_value)
for index, line in df.iterrows():
    try:
        datetime.datetime.strptime(line['DATE'],'%Y-%m-%d')
    except:
        df.loc[index, 'DATE'] = np.nan
        pass
    try:
        int(line['NAME_STUDENT'])
        df.loc[index, 'NAME_STUDENT'] = np.nan
    except:
        pass
    if line['DATE']== '1968-09-27' or line['DATE']=='2020-10-07' or line['DATE'] == '2022-01-13':
        df.loc[index,'KBTU_ID']=np.nan
    if line['BEGIN_HOUR']==23 or line['COUNT'] == 10:
        df.loc[index,'KBTU_ID']=np.nan
df.dropna(subset = ['BEGIN_HOUR','COUNT','DATE','WEEK', 'KBTU_ID','TYPE','NAME_STUDENT'], inplace = True)
df = df.drop_duplicates() 
df["DATE"] = pd.to_datetime(df['DATE'])
df = df.sort_values(by=['NAME_STUDENT'])
df.reset_index(drop=True, inplace=True)
print(df)