#!/bin/bash -l

savedir=${LUSTRE}/swen/datos/tareas_meteogalicia/ar/my_catalogues/merra2/nhemis

#track ARs
module load chimplot
python get_mask.py
sleep 2

#set variable parameters
module purge
module load ibi/2018
module load gcc/5.5.0
module load openmpi/1.10.7
module load nco/4.4.9

#attributes for variable lon
ncatted -a standard_name,lon,c,string,longitude ${savedir}/MERRA2.ar_mask.Brands.nc4
ncatted -a long_name,lon,c,string,longitude ${savedir}/MERRA2.ar_mask.Brands.nc4
ncatted -a units,lon,c,string,degrees_east ${savedir}/MERRA2.ar_mask.Brands.nc4
ncatted -a axis,lon,c,string,X ${savedir}/MERRA2.ar_mask.Brands.nc4

#attributes for variable lat
ncatted -a standard_name,lat,c,string,latitude ${savedir}/MERRA2.ar_mask.Brands.nc4
ncatted -a long_name,lat,c,string,latitude ${savedir}/MERRA2.ar_mask.Brands.nc4
ncatted -a units,lat,c,string,degrees_north ${savedir}/MERRA2.ar_mask.Brands.nc4
ncatted -a axis,lat,c,string,Y ${savedir}/MERRA2.ar_mask.Brands.nc4

#attributes for ar_binary_mask
ncatted -a version,ar_binary_mask,c,string,1.0 ${savedir}/MERRA2.ar_mask.Brands.nc4
ncatted -a scheme,ar_binary_mask,c,string,Brands ${savedir}/MERRA2.ar_mask.Brands.nc4
ncatted -a description,ar_binary_mask,c,string,"atmospheric river regional coverage mask" ${savedir}/MERRA2.ar_mask.Brands.nc4

sleep 2
exit
