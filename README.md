# AR_detector
Python 2.7 scripts and functions to detect Atmospheric Rivers in reanalysis and climate model data, implemented for use on the Finisterrae 3 High Performance Cluster of the Galician Center for Supercomputing (CESGA).

This software package was developed from the Matlab scripts used in https://doi.org/10.1007/s00382-016-3095-6 and, after being brought to Python, was applied in https://doi.org/10.1029/2019JD030936. Atmospheric rivers are detected at each grid-box of a spatial domain the user can define. A detailed algorithm description can be found in my PhD thesis available from:
https://www.researchgate.net/publication/320015096_Oceanic_and_atmospheric_precursors_of_atmospheric_river_activity_along_the_west_coasts_of_Europe_and_western_North_America

Description of the individual scripts

#Python scripts

1 get_percentiles_cesm1_2.py
calculates IVT percentile thresholds used in ar_tracker_cesm1_2.py to detect and track ARs.

2 ar_tracker_cesm1_2.py
principal script to detect and track AR for each timestep and grid-box in the input gridded GCM or reanalysis data

3 shiftlons.py
shifts longitudes of the gridded IVT data array to -180 to 180 degrees format

4 haversine.py
calculates Haversine Distance between the centres of two grid-boxes

5 get_wind_sector.py
returns the cardinal direction the IVT comes from

6 get_gridpoint.py
once the AR tracks are found and stored by ar_tracker_cesm1_2.py, this scripts gets the AR time series at a specific grid-box defined by the user.

7 get_mask.py
retrieves the binary AR coverage mask for the MERRA 2 dataset used in the TIER 1 method comparision paper (Rutz et al. 2019)

8 get_mask_cesm2_1_paleo.py
as 7, but for the CESM1 datasets generated in PaleoARTMIP


#Shell scripts

1 runme_cesm1.sh
This is the principal script to launch my AR detection and tracking algorithm to queue on CESGA's FINISTERRAE 3 HPC for use in ARTMIP (the script is currently set up for PaleoARTMIP).

2 command_cola_cesm1_2.sh
is sent to queue by runme_cesm1.sh in order to launch the Python scripts mentioned below on the working node.

3 set_attributes_ccsm4.sh
sets file attributes as requested by TIER 2 paper on AR scenarios

4 rename_and_compress_cesm1_2.sh
compresses and renames the netcdf output files as requested by TIER 2 paper on AR scenarios, is no longer in use

5 set_local_attributes_aux.sh
sets <version> attribute in the netCDF files, is no longer used

6 mask.sh
sets attributes of the netCDF file containing the binary AR coverage mask used in the TIER1 intercomparison paper (Rutz et al. 2019), is no longer in use

