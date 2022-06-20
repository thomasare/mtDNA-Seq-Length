def filesforfunction(seqlen, intervalnumb):
    '''generates code for createxml function and changejobfiles function'''
    full_seq_len = 16434
    #A. create xml function
    firstpartA = "createxml("
    secondpartA = '"Dog" + str(seqlen) + "_"'
    thirdpartA = '"_to_"'
    comma = ", "
    finalpartA = ', "org_temp.xml", "Dog_Mito_Round_2", '
   
    interval = 0
    counter = 0
    
    #B. create changejobfiles function
    firstpartB = "change_job_file("
    secondpartB = "Dog" + str(seqlen) + "_"
    finalpartB = '"Dog_3500_to_11500.sh")'
    counter2 = 0
    interval2 = 0 
   
    with open("filesfor" + str(seqlen) + ".txt", "w") as file:
        while counter < 33:
            fourthpartA = interval + seqlen
            file.write(firstpartA + secondpartA + str(interval) + thirdpartA + str(fourthpartA) + finalpartA + str(interval) + comma + str(seqlen) + ")\n")
            counter += 1
            interval += intervalnumb
        while counter2 < 33:
            fourthpartB = interval2 + seqlen
            file.write(str(firstpartB + secondpartB + str(interval2) + thirdpartA + str(fourthpartB)) + comma + finalpartB + "\n")
            counter2 += 1
            interval2 += intervalnumb 
    
    
filesforfunction(1000, 500)
