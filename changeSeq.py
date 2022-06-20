import glob

def changeSeq(filetobechanged, newFile):
    counter = 0
    badline = '<seqXML xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://www.seqxml.org/0.4/seqxml.xsd" seqXMLversion="0.4"><entry id='
    replaceLine = '                <sequence id=' 
    badline2 = '><description>'
    badline2_1 = '</description><DNAseq>'
    replaceLine2_1 = 'totalcount="4" value="'
    badline3 = '</DNAseq></entry></seqXML><?xml version="1.0" encoding="utf-8"?>'
    replaceLine3 = '"/>'
    removeline = '<?xml version="1.0" encoding="utf-8"?>'
    emptyspace = ''

    with open(filetobechanged, 'r') as nr, open(newFile, 'w') as anf:
        for line in nr.readlines():
            if badline in line:
                counter += 1
                doitbetter = line.replace(badline, replaceLine)
                print(doitbetter)
                if badline2 in doitbetter:
                    doitbetter2 = doitbetter.replace(badline2, ' taxon="dog' + str(counter) + '" ')
                    print(doitbetter2)
                    if badline2_1 in doitbetter2:
                        doitbetter2_1 = doitbetter2.replace(badline2_1, replaceLine2_1)          
                        print(doitbetter2_1)
                        if badline3 in doitbetter2_1:
                            doitbetter3 = doitbetter2_1.replace(badline3, replaceLine3)
                            anf.write(doitbetter3)
                            print(doitbetter3)
                                    
            elif removeline in line:
                doitbetter4 = removeline.replace(removeline, emptyspace)
                anf.write(doitbetter4)
                      
                     
            else:
                anf.write(line)
                
                      
                

  
    
beautiFiles = glob.glob('Beauti*.xml')
print(beautiFiles)
print(len(beautiFiles))
count = 0
for a in beautiFiles:
    changeSeq(a, 'ReadyforBeast_' + str(count) + '.xml')
    count += 1