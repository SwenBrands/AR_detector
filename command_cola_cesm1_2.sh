#!/bin/bash -l

#define input variables
tarregion=$1
taryear=$2
version=$3
dataset=$4
experiment=$5
runspec=$6
savedir=$7 #is currently not used because it is set in ar_tracker_cesm1_2.py

#track ARs
module purge
module load meteogalicia/2021
module load python/2.7.18

echo "the target region is:" ${tarregion}
echo "the target year is:" ${taryear}
echo "the algorithm version is:" ${version}
echo "the dataset is:" ${dataset}
echo "the experiment is:" ${experiment}
echo "the run is:" ${runspec}
echo "launching ar_tracker_cesm1_2.py..."
echo "the savedir for the catalogue files is set in ar_tracker_cesm1_2.py"
python ar_tracker_cesm1_2.py ${tarregion} ${taryear} ${version} ${dataset} ${experiment} ${runspec}
sleep 2
exit 0
