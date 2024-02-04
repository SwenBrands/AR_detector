#!/bin/bash -l

#define input variables
years=(1980 1981 1982 1983 1984 1985 1986 1987 1988 1989 1990 1991 1992 1993 1994 1995 1996 1997 1998 1999 2000 2001 2002 2003 2004 2005 2006 2007 2008 2009 2010 2011 2012 2013 2014 2015 2016 2017)
savedir=${LUSTRE}/swen/datos/tareas_meteogalicia/ar/my_catalogues/merra2/nhemis
tarregion=nhemis
version=2

#load packages
module purge
module load ibi/2018
module load gcc/5.5.0
module load openmpi/1.10.7
module load nco/4.4.9

for taryear in ${years[*]}
    do
    #attributes for ar_binary_tag
    ncatted -a version,ar_binary_tag,m,string,${version}.0 ${savedir}/output_v${version}_${taryear}.nc4
    sleep 1
done
exit
