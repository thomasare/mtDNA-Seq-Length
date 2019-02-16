import glob
from Bio import SeqIO

allFiles = glob.glob('*.pau') #find all the .pau files and save to variable allFiles, list
simFiles = glob.glob('*.xml')
dogFiles = glob.glob('dogSim*.xml')

#1. Change pau files to xml; DONE - Need this
def convertPau(pauFile):
    SeqIO.convert((pauFile), 'nexus', 'Test.' + str(pauFile.split('.')[0]) + '.xml', 'seqxml')

for x in allFiles:
    convertPau(x)