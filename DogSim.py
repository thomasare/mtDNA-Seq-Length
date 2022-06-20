import glob
from Bio import SeqIO

allFiles = glob.glob('*.pau') #find all the .pau files and save to variable allFiles, list
simFiles = glob.glob('*.xml')
dogFiles = glob.glob('dogSim*.xml')


def inputData(dataFile, tFile, newName):
'''writes template and sequences to file from two lists and name of file; data block must be empty'''
    seqData = []
	with open(dataFile, 'r') as sd:
	    for record in SeqIO.parse(sd, 'seqxml'):
		    seqData.append(record)
	
	dataBlock = "    <data id"
	oldName = "Dog_Mito_Round_2"
	#pull template stuff
	file = open(newName + '.xml', 'w')
	with open(tFile, 'r') as fs:
	    for line in fs.readlines():
		    if oldName in line:
			    oldnew = line.replace(oldName, newName)
				file.write(oldnew)
		        if line.startswith(dataBlock) == True:
				    for record in seqData:
				        SeqIO.write(record, file, 'seqxml')					
		    else:
			    file.write(line)
		
#get dem files
for s in dogFiles:
    fileName = s.split('.')
    inputData(s, 'Template3.xml', 'Beauti_' + str(fileName[1]))