#!/bin/bash -l

#This is the header script to launch my AR detection and tracking algorithm to queue on FT3 for use in PaleoARTMIP.
#Note: Please check whether the years are consistent to the experiments.

#exectime is 15 minutes for v1.1 and preindustrial, 10 minutes for v1.2 and 10ka_orbital, 9 minutes for v1.2 and pi_21ka_co2,
# 7 minutes for 2.1 and preindust, 7 minutes for 2.1 and 10ka_orbital, 6 minutes for 2.1 and pi_21ka_co2, 17 minutos for v3.1 and predindust,
# 16 minutes for v3.1 and 10ka_orbital, 10 minutes for v3.1 and pi_21ka_co2, 7 minutes for 2.2 and 10ka_orbital, 5 minutes for 2.2 and pi_21ka_co2,
# 16 minutes for 3.2 and 10ka_orbital and for pi_21ka_co2


#user options
regions=(na2eu)
#years=(0271 0272 0273 0274 0275 0276 0277 0278 0279 0280 0281 0282 0283 0284 0285 0286 0287 0288 0289 0290 0291 0292 0293 0294 0295 0296 0297 0298 0299 0300) #v1.1, 10ka_orbital
years=(0061 0062 0063 0064 0065 0066 0067 0068 0069 0070 0071 0072 0073 0074 0075 0076 0077 0078 0079 0080 0081 0082 0083 0084 0085 0086 0087 0088 0089 0090) #v1.1, pi_21ka_co2
#years=(0121 0122 0123 0124 0125 0126 0127 0128 0129 0130 0131 0132 0133 0134 0135 0136 0137 0138 0139 0140 0141 0142 0143 0144 0145 0146 0147 0148 0149 0150) #v1.1, preindust

rundir=${HOME}/swen/ar_ft3/python
version="v3.1" #v1.1  v1.2  v2.1  v2.2  v3.1  v3.2
dataset="cesm1_2"
experiment="pi_21ka_co2" #experiment to which the AR detection algorithm is applied to, preindust, 10ka_orbital or pi_21ka_co2
runspec="r1"
exectime=00:11:00 #15 minutes for v1.1 and preindustrial, 10 minutes for v1.2 and 10ka_orbital, 9 minutes for v1.2 and pi_21ka_co2, 7 minutes for 2.1 and preindust, 17 minutos for v3.1 and predindust, 7 minutes for 2.2 and 10ka_orbital, 5 minutes for 2.2 and pi_21ka_co2, 16 minutes for 3.2 and 10ka_orbital and for pi_21ka_co2
memory=16G

#--------------------------------------------------------------------------------------------------
# generate ar time series file for each year
#--------------------------------------------------------------------------------------------------
cd ${rundir}
for tarregion in ${regions[*]}
    do
    savedir=${LUSTRE}/swen/datos/tareas_meteogalicia/ar/my_catalogues/${dataset}/${experiment}/${runspec}/results/${tarregion}
    logdir=${LUSTRE}/swen/datos/tareas_meteogalicia/ar/my_catalogues/${dataset}/${experiment}/${runspec}/LOG
    for taryear in ${years[*]}
        do
        #then send the job to queue
        QSUB="sbatch \
        --ntasks=1 \
        --cpus-per-task=1 \
        --time=${exectime} \
        --mem ${memory} \
        --job-name ar_${taryear} \
        --export=ALL \
        --begin=now \
        --output=${logdir}/AR_${tarregion}_${taryear}.out \
        --mail-type=ALL \
        --mail-user="swen.brands@gmail.com" \
        ./command_cola_cesm1_2.sh ${tarregion} ${taryear} ${version} ${dataset} ${experiment} ${runspec} ${savedir}"
        echo ${QSUB}
        ${QSUB}
        sleep 10 #try this to see whehter many subseqeunt jobs do not load the same files
    done
done
echo "The logfiles of the AR detection and tracking algorithm are located in:"
echo "${logdir}/AR_${tarregion}_${taryear}.out"
exit 0

