#!/bin/bash -l

#define input variables
#years=(1980 1981 1982 1983 1984 1985 1986 1987 1988 1989 1990 1991 1992 1993 1994 1995 1996 1997 1998 1999 2000 2001 2002 2003 2004 2005 2006 2007 2008 2009 2010 2011 2012 2013 2014 2015 2016 2017)
#years=(1950 1951 1952 1953 1954 1955 1956 1957 1958 1959 1960 1961 1962 1963 1964 1965 1966 1967 1968 1969 1970 1971 1972 1973 1974 1975 1976 1977 1978 1979 1980 1981 1982 1983 1984 1985 1986 1987 1988 1989 1990 1991 1992 1993 1994 1995 1996 1997 1998 1999 2000 2001 2002 2003 2004 2005)
years=(2006 2007 2008 2009 2010 2011 2012 2013 2014 2015 2016 2017 2018 2019 2020 2021 2022 2023 2024 2025 2026 2027 2028 2029 2030 2031 2032 2033 2034 2035 2036 2037 2038 2039 2040 2041 2042 2043 2044 2045 2046 2047 2048 2049 2050 2051 2052 2053 2054 2055 2056 2057 2058 2059 2060 2061 2062 2063 2064 2065 2066 2067 2068 2069 2070 2071 2072 2073 2074 2075 2076 2077 2078 2079 2080 2081 2082 2083 2084 2085 2086 2087 2088 2089 2090 2091 2092 2093 2094 2095 2096 2097 2098 2099 2100)

dataset="ccsm4"
experiment="rcp85"
runspec="r6i1p1"
version="v3.1"
region="nhemis"

##execute
filestring="CCSM4_"${experiment}_${runspec}
savedir=${LUSTRE}/swen/datos/tareas_meteogalicia/ar/my_catalogues/${dataset}/${experiment}/${runspec}/${region}
rm -r ${savedir}/${version} #delete previously generated directory
mkdir ${savedir}/${version} #newly generate this directory

#load modules
module purge
module load meteogalicia/2018
module load nco/4.7.7

for taryear in ${years[*]}
    do
    
    #first check consitency of the entries
    if [ ${taryear} -gt 2005 ] && [ ${experiment} != "rcp85" ] 
    then
        echo "target year ${taryear} and experiment ${experiment} are inconsistent, exiting now!"
        exit 1
    elif  [ ${taryear} -le 2005 ] && [ ${experiment} != "historical" ]
    then
        echo "target year ${taryear} and experiment ${experiment} are inconsistent, exiting now!"
        exit 1
    else
        echo "target year ${taryear} and experiment ${experiment} are consistent, start setting the attributes..."
    fi
    
    filename=${dataset}_${experiment}_${runspec}_Brands_${version}_${taryear}.nc4
    #copy file to the version folder
    echo "copying ${savedir}/${dataset}_${experiment}_${runspec}_Brands_${version}_${taryear}.nc4...."
    cp ${savedir}/${filename} ${savedir}/${version}/
    
    echo "processing ${savedir}/${filename}...."
    #attributes for variable time
    ncatted -a standard_name,time,c,string,time ${savedir}/${version}/${filename}
    ncatted -a long_name,time,c,string,time ${savedir}/${version}/${filename}
    
    #attributes for variable lon
    ncatted -a standard_name,lon,c,string,longitude ${savedir}/${version}/${filename}
    ncatted -a long_name,lon,c,string,longitude ${savedir}/${version}/${filename}
    ncatted -a units,lon,c,string,degrees_east ${savedir}/${version}/${filename}
    ncatted -a axis,lon,c,string,X ${savedir}/${version}/${filename}

    #attributes for variable lat
    ncatted -a standard_name,lat,c,string,latitude ${savedir}/${version}/${filename}
    ncatted -a long_name,lat,c,string,latitude ${savedir}/${version}/${filename}
    ncatted -a units,lat,c,string,degrees_north ${savedir}/${version}/${filename}
    ncatted -a axis,lat,c,string,Y ${savedir}/${version}/${filename}

    #attributes for ar_binary_tag
    ncatted -a version,ar_binary_tag,c,string,${version} ${savedir}/${version}/${filename}
    ncatted -a scheme,ar_binary_tag,c,string,"Brands based on doi:10.1007/s00382-016-3095-6" ${savedir}/${version}/${filename}
    ncatted -a description,ar_binary_tag,c,string,"binary indicator of atmospheric river occurrence" ${savedir}/${version}/${filename}

    ##set global attributes
    #ncatted -a input,global,c,string,"ARTMIP file format" ${savedir}/MERRA2.ar_tag.Brands_v1.0hourly.${taryear}.nc4
    ncatted -a casename,global,c,string,${filestring} ${savedir}/${version}/${filename}
   
    sleep 1
done
exit
