import xarray as xr
import dask
import numpy as np
import pandas as pd
import os
import numpy.matlib
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt
import scipy.stats
from mpl_toolkits.basemap import Basemap
from mpl_toolkits.basemap import addcyclic
from math import radians, cos, sin, asin, sqrt
import sys

## USER OPTIONS ########################################################
region = 'nhemis'
dataset = 'ccsm1_2'
experiment = 'preindust'
runspec = 'paleorun'
cmip = 'cmip5'
filelabel = 'CCSM4_historical_r6i1p1'
version = 'v1.1'
homedir = os.getenv("HOME")
lustre = os.getenv("LUSTRE")
srcdir = lustre+'/swen/datos/GCMData/'+dataset+'/'+experiment+'/'+runspec #used to load the original grid for this gcm
prctdir = lustre+'/swen/datos/tareas_meteogalicia/ar/my_catalogues/'+dataset+'/'+experiment+'/'+runspec+'/'+region #used to load the percentiles file 

#geographical domain for the tracking algorithm, longitudes must be in Greenwich format (-180 to 180 degrees)
minlat2 = 29
maxlat2 = 63
minlon2 = -151
maxlon2 = 31

## EXECUTE #############################################################
#get lons and lats for this dataset
gridfile = srcdir+'/uhusavi/uhusavi_6hrLev_CCSM4_historical_r6i1p1_1950010106-1950033118.nc'
nc = xr.open_dataset(gridfile)
lat = nc.lat.values
lon = nc.lon.values
nc.close()
#shift to -180-180 degrees format
mask = np.where(lon > 180)[0]
lon[mask] = lon[mask]-float(360)
lon.sort()

## EXECUTE #############################################################
if region == 'nhemis':
    ##construct domain for AR tracking
    minlat2_ind = np.argmin(np.abs(lat-minlat2))
    maxlat2_ind = np.argmin(np.abs(lat-maxlat2))
    minlon2_ind = np.argmin(np.abs(lon-minlon2))
    maxlon2_ind = np.argmin(np.abs(lon-maxlon2))
    detect_lat = lat[minlat2_ind:maxlat2_ind]
    detect_lon = lon[minlon2_ind:maxlon2_ind]    
    detect_lon, detect_lat = np.meshgrid(detect_lon,detect_lat)
    detect_lon = np.ndarray.flatten(detect_lon)
    detect_lat = np.ndarray.flatten(detect_lat)
else:
    raise Exception('check entry for <region>!')
    
#create an xarray DataArray and fill in values
outdata = np.zeros((len(lat),len(lon)), dtype='int8')

for ff in xrange(len(detect_lat)):
    latind = np.where(lat == detect_lat[ff])
    lonind = np.where(lon == detect_lon[ff])
    outdata[latind,lonind] = 1
    #del latind; del lonind

#re-convert to float64 so that the data can be saved
lat = np.float64(lat)
lon = np.float64(lon)

output = xr.DataArray(outdata, coords=[lat, lon], dims=['lat', 'lon'], name = 'ar_binary_mask')

savefile = prctdir+'/'+cmip+'_'+filelabel+'.ar_mask.Brands_'+version+'.nc4'
print(savefile)
output.to_netcdf(savefile, format='NETCDF4')
output.close()
      

        
    
     
     
 
        
    
