import glob
def changeMCMC(inputfile, outputfile):
    originalMCMC = '<run id="mcmc" spec="MCMC" chainLength="100000000">'
    newMCMC = '<run id="mcmc" spec="MCMC" chainLength="10000000">'
    
    with open(inputfile, 'r') as inf, open(outputfile, 'w') as opf:
        for line in inf.readlines():
            if originalMCMC in line:
                now = line.replace(originalMCMC, newMCMC)
                opf.write(now)
            else:
                opf.write(line)
    

	
beastfiles = glob.glob('Beast*.xml')
print(len(beastfiles))
for i in beastfiles:
    outputname = i.split('_')
    changeMCMC(i, 'Dog_' + str(outputname[0]) + '_' + str(outputname[2]))
	
allthefiles = glob.glob('Dog_*.xml')
print(len(allthefiles))
