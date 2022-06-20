#!/bin/sh
#$ -N Dog_13500_to_5066_job
#$ -e /Users/athomas14/workspace/dna/dissertation/Dog_13500_to_5066_job.err
#$ -o /Users/athomas14/workspace/dna/dissertation/Dog_13500_to_5066_job.log 
#$ -M ariane-thomas@uiowa.edu
#$ -m abe
#$ -pe smp 4
#$ -cwd
#$ -q ANTH

date start = 'date +%s'
CMD="
module load BEAST

java -jar /Users/athomas14/workspace/dna/tools/beast.jar -beagle -beagle_CPU -beagle_SSE /Users/athomas14/workspace/dna/dissertation/Dog_13500_to_5066.xml

"
echo "***************************"
echo "commands=$CMD"
echo"****************************"


module load BEAST
java -jar /Users/athomas14/workspace/dna/tools/beast.jar -beagle -beagle_CPU -beagle_SSE /Users/athomas14/workspace/dna/dissertation/Dog_13500_to_5066.xml
