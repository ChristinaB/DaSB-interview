# -*- coding: utf-8 -*-
"""
Created on Thu Jul 25 21:00:30 2024

@author: Diner
"""

#restart computer 

import os 
import glob 
import pandas as pd 
from datetime import datetime

os.chdir("C:\\Users\\a_colleague\\Desktop\\basin_prcp_scripts\\data")

# get files from 1979-2021 
# renaming pfile to files

filesALL = glob.glob('basin*')
#Option 2: use files only to 2022
files=filesALL[0:43]
# Define daily data dictionary 
daily_P={}
# Define annual dictionary
data = {'year': [],
        'prcp': []} 
#Set index to length of years
index = pd.RangeIndex(len(files))
# Convert the dictionary into DataFrame
df = pd.DataFrame(data, columns=['year', 'prcp'])

for ind in index:
    current = pd.read_csv(files[ind])
    
    daily_P['date']=pd.to_datetime(current['day'])
    daily_P['prcp'] = round(current['prcp'], 2)
    df.loc[ind,'year'] =daily_P['date'].dt.year[0]
    df.loc[ind,'prcp'] = round(current['prcp'].sum(),2)

# fix year column by converting to integer
df = df.astype({'year':'int'})
"""
for i in range(1, 42):
    # i = 2
    year = 1978 + i 

    current = pd.read_csv(pfiles[i])
    current['prcp'] = round(current['prcp'], 2) 
    current['day'] = pd.to_datetime(current['day'])

    pdata = pdata.append(current)


pdata['year'] = pdata['day'].dt.year

# plot annual total 
pdata_annual = pdata.groupby(['year']).sum()
"""
import matplotlib.pyplot as plt
#I recommend plotting with Year instead of index. 
#plt.plot(df.index, df['prcp'], 'o', color = 'black ##plt.plot(pdata_annual.index, pdata_annual['prcp'], 'o', color = 'black')
plt.plot(df['year'], df['prcp'], 'o', color = 'black')
plt.xlabel('Year')
plt.ylabel('Annual precipitation, mm')