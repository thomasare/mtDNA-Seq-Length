#!/bin/sh
#$ -N Dog_3500_to_11500_job
#$ -e /Users/athomas14/workspace/dna/dissertation/Dog_3500_to_11500_job.err
#$ -o /Users/athomas14/workspace/dna/dissertation/Dog_3500_to_11500_job.log 
#$ -M ariane-thomas@uiowa.edu
#$ -m abe
#$ -pe smp 4
#$ -cwd
#$ -q ANTH

date start = 'date +%s'
CMD="
module load BEAST

java -jar /Users/athomas14/workspace/dna/tools/beast.jar -beagle -beagle_CPU -beagle_SSE /Users/athomas14/workspace/dna/dissertation/Dog_3500_to_11500.xml

"
echo "***************************"
echo "commands=$CMD"
echo"****************************"


module load BEAST
java -jar /Users/athomas14/workspace/dna/tools/beast.jar -beagle -beagle_CPU -beagle_SSE /Users/athomas14/workspace/dna/dissertation/Dog_3500_to_11500.xml

