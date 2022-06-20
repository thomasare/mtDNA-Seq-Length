def change_job_file(newName, tFile):
    oldName = "Dog_3500_to_11500"
    with open(newName + ".sh", "w") as file:
        with open(tFile, "r") as fs:
            for line in fs.readlines():
                if oldName in line:
                    oldnew = line.replace(oldName, newName)
                    file.write(oldnew)
                else:
                    file.write(line)
                        
                        

change_job_file("Dog8000_8000_to_16000", "Dog_3500_to_11500.sh")

