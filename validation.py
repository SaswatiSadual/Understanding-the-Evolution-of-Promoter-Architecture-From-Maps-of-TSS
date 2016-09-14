## Python script to extract the sequences from the .2bit files onto FASTA files to be used in NPLB

######### Creating the required .bed file to use it with twoBitToFa ##################################
from subprocess import call


with open("Supp_File_S1_CAGE_Dmel_FM_carcass.bed") as orig_file, open("Dmel_all_sequence.bed",'w') as new_fi:
    for line in orig_file:
        L = line.strip().split()
        if(L[5]=='+'):
            L[1] = str(int(L[1]) - 46)
            L[2] = str(int(L[2]) + 44)
        else:
            L[1] = str(int(L[1]) - 44)
            L[2] = str(int(L[2]) + 46)

        L.pop(6)
        L.pop(4)
        L.pop(3)
        val = '\t'.join(L)
        new_fi.write(val+'\n')
        #print(val+'\n')
       # new_fi.write('\n')

##### Creating the FASTA file using the .bed file created above. ######################################
call("./twoBitToFa dm3.2bit dm3_all_seq_output.fa -bed=Dmel_all_sequence.bed", shell=True)


##### Editing the FASTA file. The reverse complement of the negative strand is taken. #################
##replace_lines = open("newfile.bed")  ## The used .bed file. The strand information is taken from this file
replace_lines = open("Supp_File_S1_CAGE_Dmel_FM_carcass.bed")
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


f_file = open("dm3_all_seq_output.fa")  ## The input FASTA file. This does not contain strand information and reverse complement hasn't been done
out_file = open("Dmel_outfile_all.fa","w")  ## The required output FASTA file. This will be used in NPLB
elements = f_file.readlines()
seq_list = []
for index in range(0,len(elements),3):  ## Combining the three lines of sequences
    #tmp = elements[index+1]+elements[index+2]+elements[index+3]
    tmp = elements[index + 1] + elements[index + 2]
    sequence = tmp.replace('\n','')
    if elements[index].__contains__(">-"):
        sequence = reverseCompliment(sequence)
    #print(">"+replace_lines.readline()+'\n')
    #print(sequence)
    seq_list.append(sequence)
    out_file.write(">"+replace_lines.readline()) ## Writing the strand information
    out_file.write(sequence+'\n')                ## Writing the sequence into the file.

## Here seq_list contains all the sequences that are in the fasta file:
pixel_value = {'A':1, 'a':1, 'T':2, 't':2, 'G':3, 'g':3, 'C':4, 'c':4} ## each nucleotide is coded
list_of_seq = []
for i in range(len(seq_list)):

    p = list(seq_list[i])
    pixValue = [pixel_value[x] for x in p]
    #print(pixValue)
    list_of_seq.append(pixValue)
    #print(list_of_seq)

### The sequences that were stored in the nested list were converted into a CSV record file.
### Each row has the corresponding sequence of the Supp_File_S5_CAGE_Dpse_F_carcass.bed file.
import csv

with open("image_code_matrix_Dmel_All.csv",'w') as matrix_file:
    #matrix_file.writelines(','.join(i)+'\n' for i in list_of_seq)
    w = csv.writer(matrix_file, dialect='excel')
    w.writerows(list_of_seq)
########### The CSV File is Created###########################################
