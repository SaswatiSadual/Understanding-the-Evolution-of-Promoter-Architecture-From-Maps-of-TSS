## Python script to extract the sequences from the .2bit files onto FASTA files to be used in NPLB

######### Creating the required .bed file to use it with twoBitToFa ##################################
from subprocess import call


with open("Supp_File_S1_CAGE_Dmel_FM_carcass.bed") as orig_file, open("newfile.bed",'w') as new_fi:
    for line in orig_file:
        L = line.strip().split()
        if(L[5]=='+'):
            L[1] = str(int(L[1]) - 50)
            L[2] = str(int(L[2]) + 51)
        else:
            L[1] = str(int(L[1]) - 51)
            L[2] = str(int(L[2]) + 50)

        L.pop(6)
        L.pop(4)
        L.pop(3)
        val = '\t'.join(L)
        new_fi.write(val+'\n')
        #print(val+'\n')
       # new_fi.write('\n')

##### Creating the FASTA file using the .bed file created above. ######################################
call("./twoBitToFa dm3.2bit dm3_output.fa -bed=newfile.bed", shell=True)


##### Editing the FASTA file. The reverse complement of the negative strand is taken. #################
replace_lines = open("newfile.bed")  ## The used .bed file. The strand information is taken from this file

########### Reverse Compliment ############################
alt_map = {'ins':'0'}
complement = {'A':'T', 'T':'A', 'G':'C', 'C':'G'}
def reverseCompliment(seq):
    for k,v in alt_map.items():
        seq = seq.replace(k,v)
    bases = list(seq)
    bases = reversed([complement.get(base,base) for base in bases])
    bases =''.join(bases)
    for k,v in alt_map.items():
        bases = bases.replace(v,k)
    return bases
#############################################################


f_file = open("dm3_output.fa")  ## The input FASTA file. This does not contain strand information and reverse complement hasn't been done
out_file = open("outfile.fa","w")  ## The required output FASTA file. This will be used in NPLB
elements = f_file.readlines()
for index in range(0,len(elements),4):  ## Combining the three lines of sequences
    tmp = elements[index+1]+elements[index+2]+elements[index+3]
    sequence = tmp.replace('\n','')
    if elements[index].__contains__(">-"):
        sequence = reverseCompliment(sequence)
    #print(">"+replace_lines.readline()+'\n')
    #print(sequence)
    out_file.write(">"+replace_lines.readline()) ## Writing the strand information
    out_file.write(sequence+'\n')                ## Writing the sequence into the file.

