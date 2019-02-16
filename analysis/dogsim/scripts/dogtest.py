import glob
import os#changes directories and file names
from Bio import SeqIO

os.chdir('/Users/Ariane Thomas/Downloads/Test') #change to the appropriate dir
allFiles = glob.glob('*.pau') #find all the .pau files and save to variable allFiles, list
simFiles = glob.glob('*.xml')
dogFiles = glob.glob('dogSim*.xml')

#1. Change pau files to xml; DONE - Need this
def convertPau(pauFile):
'''converts pau/nexus files to xml.  Input must be a string'''
    SeqIO.convert((pauFile), 'nexus', 'dogSim.' + str(pauFile.split('.')[0]) + '.xml', 'seqxml')

for x in allFiles:
    convertPau(x)
	
#2. Get sequences from xml file; DONE - extra
def xmlSeq(xmlFile): #any xml or file
'''pulls the sequence record and saves them as a list'''
    sequences = []
	pf = open(xmlFile, 'r')#open file and pull records from pau file save to a list
    for record in SeqIO.parse(pf, 'seqxml'):
        sequences.append(record)
	pf.close()

#3. Get template file into a list; DONE - extra
def pullTemp(tempFile): #any Beauti file
'''pulls data from a template file into a list'''		
	allLines = []
	with open(tempFile) as pt:
	for line in pt.readlines():
	    allLines.append(line)
	
#4. Get Beauti files from xml files; Done
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
for s in simFiles:
    fileName = s.split('.')
    inputData(s, 'Template3.xml', 'Beauti_' + str(fileName[1]))

#5. Pull out the incorrect data in data block
def changeSeq(filetobechanged, newFile):
    counter = 0
    badline = '<seqXML xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://www.seqxml.org/0.4/seqxml.xsd" seqXMLversion="0.4"><entry id='
    replaceLine = '                <sequence id=' 
    badline2 = '><description>'
    badline2_1 = '</description><DNAseq>'
    replaceLine2_1 = 'totalcount="4" value="'
    badline3 = '</DNAseq></entry></seqXML><?xml version="1.0" encoding="utf-8"?>'
    replaceLine3 = '"/>'
    addline = '<map name="Uniform" >beast.math.distributions.Uniform</map>'
    addline2 = '</data>'
    addline3 = '<map name="Uniform" >beast.math.distributions.Uniform</map>'
    removeline = '<?xml version="1.0" encoding="utf-8"?>'
    emptyspace = ''

    with open(filetobechanged, 'r') as nr, open(newFile, 'w') as anf:
        for line in nr.readlines():
            if badline in line:
                counter += 1
                doitbetter = line.replace(badline, replaceLine)
                if badline2 in doitbetter:
                    doitbetter2 = doitbetter.replace(badline2, ' taxon="dog' + str(counter) + '" ')
                    if badline2_1 in doitbetter2:
                        doitbetter2_1 = doitbetter2.replace(badline2_1, replaceLine2_1)          
                        if badline3 in doitbetter2_1:
                            doitbetter3 = doitbetter2_1.replace(badline3, replaceLine3)
                            anf.write(doitbetter3)
                                    
            elif removeline in line:
                doitbetter4 = removeline.replace(removeline, emptyspace)
                anf.write(doitbetter4)
                      
            elif addline in line:
                doitbetter5 = addline.replace(addline, addline2)
                anf.write(doitbetter5)
                anf.write(addline3)
                      
            else:
                anf.write(line)
                
                      
                

  
    
beautiFiles = glob.glob('BEAUti_*.xml')
count = 0
for a in beautiFiles:
    changeSeq(a, 'ReadyforBeast_' + count + .xml')
    count += 1
    