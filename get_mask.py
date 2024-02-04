import xarray as xr
import numpy as np
import os
import numpy.matlib
from matplotlib import pyplot as plt
from mpl_toolkits.basemap import Basemap

## USER OPTIONS ########################################################
region = 'nhemis'
homedir = os.getenv("HOME")
lustre = os.getenv("LUSTRE")
prctdir = lustre+'/swen/datos/tareas_meteogalicia/ar/my_catalogues/merra2'

## EXECUTE #############################################################
if region == 'nhemis':
    print('target region is nhemis')    
    ##ARs are tracked for this domain
    minlat2 = 30
    maxlat2 = 62
    minlon2 = -150
    maxlon2 = 30
   
    detect_lat = list(np.arange(minlat2,maxlat2,0.5))
    detect_lon = list(np.arange(minlon2,maxlon2,0.625))
    detect_lon, detect_lat = np.meshgrid(detect_lon,detect_lat)
    detect_lon = np.ndarray.flatten(detect_lon)
    detect_lat = np.ndarray.flatten(detect_lat)
else:
    raise Exception('check entry for <region>!')

#load the global lat lon mask
maskfile = prctdir+'/mask/MERRA2.ar_mask.Shields_v1.nc4'
nc = xr.open_mfdataset(maskfile)
lat_mask = nc.lat.values
lon_mask = nc.lon.values
nc.close()

#correct longitude error
lat_mask = np.float16(lat_mask)
lon_mask = np.float16(lon_mask)
stepind = np.where(lon_mask==-0.)
lon_mask[stepind] = 0
del stepind

#create an xarray DataArray and fill in values
outdata = np.zeros((len(lat_mask),len(lon_mask)), dtype='int8')

for ff in xrange(len(detect_lat)):
    latind = np.where(lat_mask == detect_lat[ff])
    lonind = np.where(lon_mask == detect_lon[ff])
    outdata[latind,lonind] = 1
    #del latind; del lonind

#re-convert to float64 so that the data can be saved
lat_mask = np.float64(lat_mask)
lon_mask = np.float64(lon_mask)

output = xr.DataArray(outdata, coords=[lat_mask, lon_mask], dims=['lat', 'lon'], name = 'ar_binary_mask')

savefile = prctdir+'/'+region+'/MERRA2.ar_mask.Brands.nc4'
print(savefile)
output.to_netcdf(savefile, format='NETCDF4')
output.close()
      

        
    
     
     
 
        
    
