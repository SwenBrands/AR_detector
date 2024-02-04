import xarray as xr
import numpy as np
import os
import numpy.matlib
import csv

## USER OPTIONS ########################################################
homedir = os.getenv("HOME")
lustre = os.getenv("LUSTRE")
version = 1
srcdir = lustre+'/swen/datos/tareas_meteogalicia/ar/my_catalogues/merra2/nhemis/v'+str(version)

#define the grid box
tarlat = 38.5
tarlon = -123.125

#load the global lat lon mask
inputfile = srcdir+'/MERRA2.ar_tag.Brands_v1.3hourly.*.nc4'
nc = xr.open_mfdataset(inputfile)
lat = nc.lat.values
lon = nc.lon.values

#find indices for this specfic grid box
latind = np.where(lat == tarlat)
lonind = np.where(lon == tarlon)

#get the data for this longitude and latitude and format
gridbox = nc.ar_binary_tag.sel(lat=tarlat,lon=tarlon,method='nearest')
data = np.int8(gridbox.values)
lat = np.float16(gridbox.lat.values)
lon = np.float16(gridbox.lon.values)
dates = gridbox.time.values

#output = xr.DataArray(data, coords=[dates, lat, lon], dims=['time', 'lat', 'lon'], name = 'ar_binary_tag')
output = xr.DataArray(data, coords=[dates], dims=['time'], name = 'ar_binary_tag')

#save to netcdf
outputfile=srcdir+'/Brands_v'+str(version)+'_lat'+str(tarlat)+'_lon'+str(tarlon)+'_1980_2017.nc'
output.to_netcdf(outputfile)
nc.close()

#with open(outputfile,'wb') as resultFile:
    #wr = csv.writer(resultFile, dialect='excel-tab')
    #for outrow in output:
        #wr.writerows([[outrow]])
        
    

     
 
        
    
