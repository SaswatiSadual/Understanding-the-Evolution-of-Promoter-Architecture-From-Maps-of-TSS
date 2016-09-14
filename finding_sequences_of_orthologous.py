# Find the orthologous sequences between the D.melanogaster and D.pseudoobscura
from subprocess import call


proteinList_Dmel = []
with open("Supp_File_S1_CAGE_Dmel_FM_carcass.bed") as Dmel:
        for rec in Dmel:
            values = rec.strip().split()
            proteinList_Dmel.append(values[3])

#print(proteinList_Dmel)

proteinList_Dpse = []
with open("Supp_File_S5_CAGE_Dpse_F_carcass.bed") as Dpse:
    for r in Dpse:
        val = r.strip().split()
        proteinList_Dpse.append(val[3])

#print(proteinList_Dpse)

## The orthologous sequences are the common sequences between both the species:
ortho_sequences = set(proteinList_Dpse).intersection(proteinList_Dmel)
#print(ortho_sequences)

## These orthologous sequences will be used to find the respective protein ID from the D.pseudoobscura .bed file
## A new .bed file is created with the entire data of the orthologs
with open("Supp_File_S5_CAGE_Dpse_F_carcass.bed") as fileDpse, open("Dpse_out.bed","w") as Dpse_outfile:
    for line in fileDpse:
        record = line.strip().split()
        #for index in range(len(ortho_sequences)):
        if record[3] in ortho_sequences:
            write_rec = '\t'.join(record)
            Dpse_outfile.write(write_rec+'\n')
            #print(record)


## Creating the FASTA file from the orthologous sequences in the .bed file.


## Modifying the bed file to be used with twoBitToFa:
with open("Dpse_out.bed") as orig_file, open("ortholog_sequences.bed",'w') as new_fi:
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
call("./twoBitToFa dp4.2bit dp4_output.fa -bed=ortholog_sequences.bed", shell=True)


##### Editing the FASTA file. The reverse complement of the negative strand is taken. #################
replace_lines = open("ortholog_sequences.bed")  ## The used .bed file. The strand information is taken from this file

########### Reverse Complement ############################
alt_map = {'ins':'0'}
complement = {'A':'T', 'T':'A', 'G':'C', 'C':'G', 'a':'t','t':'a','g':'c','c':'g'}
def reverseComplement(seq):
    for k,v in alt_map.items():
        seq = seq.replace(k,v)
    bases = list(seq)
    bases = reversed([complement.get(base,base) for base in bases])
    bases =''.join(bases)
    for k,v in alt_map.items():
        bases = bases.replace(v,k)
    return bases
#############################################################


f_file = open("dp4_output.fa")  ## The input FASTA file. This does not contain strand information and reverse complement hasn't been done
out_file = open("ortholog_fasta.fa","w")  ## The required output FASTA file. This will be used in NPLB
elements = f_file.readlines()
seq_list = []
for index in range(0,len(elements),4):  ## Combining the three lines of sequences
    tmp = elements[index+1]+elements[index+2]+elements[index+3]
    sequence = tmp.replace('\n','')
    if elements[index].__contains__(">-"):
        sequence = reverseComplement(sequence)
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

with open("image_code_matrix.csv",'w') as matrix_file:
    #matrix_file.writelines(','.join(i)+'\n' for i in list_of_seq)
    w = csv.writer(matrix_file, dialect='excel')
    w.writerows(list_of_seq)
########### The CSV File is Created###########################################

## This CSV file is now used in R to create the imag pixel matrix
#call("convert_image_code_matrix_to_image.R")