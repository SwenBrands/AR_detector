#!/bin/bash -l
#recall: the .1 methods all use the (full) preindust experiment as references for cacluating the relative IVT thresholds, while the .2 methods use the experiment
#the are executed for, i.e. either 10ka_orbital or pi_21ka_co2. The .2 methods have not been applied to the preindust experiment because, in this case, they
#are indentical to the respective .1 method

dataset="cesm1_2"
experiment="pi_21ka_co2" #preindust, 10ka_orbital or pi_21ka_co2
runspec="r1"
version="v3.2"
region="na2eu"
src=${LUSTRE}/swen/datos/tareas_meteogalicia/ar/my_catalogues/${dataset}/${experiment}/${runspec}/results/${region}/${version}

#load modules
module purge
module load meteogalicia/2021

## EXECUTE #############################################################
if [ ${experiment} == 'preindust' ]
then
    experiment_out='PreIndust'
    years=(0121 0122 0123 0124 0125 0126 0127 0128 0129 0130 0131 0132 0133 0134 0135 0136 0137 0138 0139 0140 0141 0142 0143 0144 0145 0146 0147 0148 0149 0150) #v1.1, preindust, done, 10 minutes runtime per year is sufficient
elif [ ${experiment} == '10ka_orbital' ]
then
    experiment_out='10ka-Orbital'
    years=(0271 0272 0273 0274 0275 0276 0277 0278 0279 0280 0281 0282 0283 0284 0285 0286 0287 0288 0289 0290 0291 0292 0293 0294 0295 0296 0297 0298 0299 0300) #v1.1, 10ka_orbital, done, 9 minutes runtime per year is sufficient
elif [ ${experiment} == 'pi_21ka_co2' ]
then
    experiment_out='PI_21ka-CO2'
    years=(0061 0062 0063 0064 0065 0066 0067 0068 0069 0070 0071 0072 0073 0074 0075 0076 0077 0078 0079 0080 0081 0082 0083 0084 0085 0086 0087 0088 0089 0090) #v1.1, pi_21ka_co2, 6 minutes is sufficient
else
    echo "ERROR: check entry for <experiment>, exiting now!"
    exit 1
fi

filelabel=${dataset}_${experiment}_${runspec}
echo "The basic file name is ${filelabel}"
echo "The output label for ${experiment} is ${experiment_out}"

cd ${src}
for taryear in ${years[*]}
    do
    echo "processing year ${taryear}"
    ##compress
    #endyear=$((taryear+1))
    ncks -O -4 -L 1 ${dataset}_${experiment}_${runspec}_Brands_${version}_${taryear}.nc4 ${dataset}_${experiment_out}.ar_tag.Brands_${version}.6hr.${taryear}.nc4
    sleep 1
done
echo "the output data is in ${src}"
exit 0
