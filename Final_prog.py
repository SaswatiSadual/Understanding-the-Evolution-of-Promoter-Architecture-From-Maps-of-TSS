from subprocess import call

with open("Supp_File_S1_CAGE_Dmel_FM_carcass.bed") as orig_file, open("newfile.bed",'w') as new_fi:
    for line in orig_file:
        L = line.strip().split()
	if 
        L[1] = str(int(L[1]) - 50)
        L[2] = str(int(L[2]) + 51)
	L.pop(6)        
	L.pop(4)
	L.pop(3)
        val = '\t'.join(L)
        new_fi.write(val+'\n')
        #print(val+'\n')
       # new_fi.write('\n')
call(["/home/leelavati/bin/i686/twoBitToFa dm3.2bit dm3_output.fa -bed=newfile.bed"], shell=True)

