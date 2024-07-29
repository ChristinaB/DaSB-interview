# -*- coding: utf-8 -*-
"""
Created on Thu Jul 25 21:00:51 2024

@author: a_colleage + Diner
"""
#Download pr_*.nc data files
#Manual: Go to this website and download the pr_ files first: https://www.northwestknowledge.net/metdata/data/
#Automated: Use https://github.com/ChristinaB/DaSB-interview/blob/main/download_USGS_precip.ipynb

# console code to run this file
#runfile('C:/Users/Diner/GithubRepos/DaSB-interview/subset_precip.py', wdir='C:/Users/Diner/USGSdata')

# subset nc files to our area of interest 
import os
import xarray as xr 
import numpy as np 
import pandas as pd 
import glob
#set I/O directory
path_to_save_directory = os.getcwd()
#read file
files=glob.glob('pr_*')
# Extract numbers from position 4 to 8
# for first year in file name list
start_numbers_str = files[0][3:7] # Positions are 0-indexed
start = int(start_numbers_str)
# for last year in file name list
end_numbers_str = files[len(files)-1][3:7] # Positions are 0-indexed
#Option 1: use latest year file available
#end = int(end_numbers_str) 
#Option 2: use 2021
end = 2021

# Set boundaries for area of interest
lats, lons = [30, 31], [-88, -87] 

# Do you specifically want to end the time series analysis at 2022? The latest files are available for 2024. Because this data catalogue is dynamic and updated annually, I updated this code so it gets the last precipitation file available and uses all available data. You can reset it to whatever start and end year data interval you want to plot.  

# See code changes to line 21 and 25; yours follow commented

for year in range(start, end + 1): ##for year in range(1979, 2021):
    file = 'pr_%s.nc' % year
    file_out = 'basin_prcp_%s.csv' % year 

    nc = xr.open_dataset(path_to_save_directory + '\\' + file) ##  nc = xr.open_dataset(local_dir + file) 
    if year == 2021:
        nc2021=nc
        
    data = nc['precipitation_amount']

    data = data.loc[dict(lon = slice(lons[0], lons[1]))]
    data = data.loc[dict(lat = slice(lats[1], lats[0]))]

    mean_precip = np.mean(data, axis = (1,2))

    out = pd.DataFrame({'day': mean_precip['day'].values, 'prcp': mean_precip.values})
    # np.savetxt(file_out, out, delimiter=',')
    out.to_csv(file_out, index = False) 
    
