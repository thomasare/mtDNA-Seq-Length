def createxml(newName, tFile, oldName, start, seq_len):
    '''creates an xml (newName) from template (tFile) and replaces newName with oldName)'''
    input_file = "Dog_Mito_Round_2.fasta"
    input_file_type = "fasta"
    full_seq_len = 16434

    from Bio import SeqIO
    from Bio.Seq import Seq
    from Bio.SeqRecord import SeqRecord
      
    temp = {}
    for record in SeqIO.parse(input_file, input_file_type):
      end = start + seq_len
      new = str(record.seq)
      if end > full_seq_len:
          add = end - full_seq_len 
          frag = new[start:full_seq_len]
          start2 = 0
          end2 = start2 + add
          anew = new_seq[start2:end2]
          final = frag + anew
          temp.update([(record.id, final)])
      else:
          frag = new[start:end]
          temp.update([(record.id, frag)])
      
    search = "<sequence id="
    with open(newName + ".xml", "w") as file:
        with open(tFile, 'r') as fs:
            for line in fs.readlines():
                if oldName in line:
                    oldnew = line.replace(oldName, newName)
                    file.write(oldnew)
                elif search in line:
                    remove = line.split("value=")
                    for key, val in temp.items():
                        if str(key) in remove[0]:
                            wline = remove[0] + "value=" + (f'"{temp[key]}"') + "/>" + "\n"
                            file.write(wline)
                        else:
                            continue
                else:
                    file.write(line)
                    
createxml("Dog_3500_to_11500", "temp.xml", "Dog_Mito_Round_2", 3500, 8000)