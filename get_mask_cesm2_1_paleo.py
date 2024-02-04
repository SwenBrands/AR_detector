#gets regional coverage of my AR detection and tracking algorihm
#ON FT3, prior to calling this script, please load:
#module purge
#module load meteogalicia/2021
#module load python/2.7.18

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
region = 'na2eu'
dataset = 'cesm1_2'
experiment = 'preindust'
runspec = 'r1'
filelabel = 'paleoartmip_experiments'
version = 'v1.1'
homedir = os.getenv("HOME")
lustre = os.getenv("LUSTRE")
srcdir = lustre+'/swen/datos/tareas_meteogalicia/ar/my_catalogues/'+dataset+'/'+experiment+'/'+runspec+'/results/'+region+'/'+version #used to load the original grid for this gcm
#prctdir = lustre+'/swen/datos/tareas_meteogalicia/ar/my_catalogues/'+dataset+'/'+experiment+'/'+runspec+'/'+region #used to load the percentiles file 

#geographical domain for the tracking algorithm, longitudes must be in Greenwich format (-180 to 180 degrees)
##ARs are tracked for this domain
if region == 'na2eu':
    minlat2 = 29
    maxlat2 = 63
    minlon2 = -151
    maxlon2 = 31
    
    ##smaller domain for short tests
    #minlat2 = 29
    #maxlat2 = 63
    #minlon2 = -151
    #maxlon2 = -148
else:
    raise Exception('check entry for <region>!')

## EXECUTE #############################################################
#get lons and lats for this dataset
gridfile = srcdir+'/cesm1_2_PreIndust.ar_tag.Brands_v1.1.6hr.0121.nc4'
nc = xr.open_dataset(gridfile)
lat = nc.lat.values
lon = nc.lon.values
nc.close()
#shift to -180-180 degrees format
mask = np.where(lon > 180)[0]
lon[mask] = lon[mask]-float(360)
lon.sort()

## EXECUTE #############################################################
if region == 'na2eu':
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
output.lat.attrs['units'] = 'degrees north'
output.lat.attrs['long_name'] = 'latitude'
#output.lat.attrs['axis'] = 'Y'
output.lon.attrs['units'] = 'degrees east'
output.lon.attrs['long_name'] = 'longitude'
#output.lon.attrs['axis'] = 'X'
output.attrs['description'] = "atmospheric river regional coverage mask"
output.attrs['scheme'] = "Brands"
output.attrs['version'] = "valid for all Brands versions used in PaleoARTMIP"

#ds = xr.Dataset(data_vars=dict(ar_binary_mask=(["y","x"], outdata),),coords=dict(lat=(["y"], lat),lon=(["x"], lon),))

savefile = srcdir+'/'+filelabel+'.ar_mask.Brands_universal.nc4'
print(savefile)
output.to_netcdf(savefile, format='NETCDF4')
output.close()
      

        
    
     
     
 
        
    
