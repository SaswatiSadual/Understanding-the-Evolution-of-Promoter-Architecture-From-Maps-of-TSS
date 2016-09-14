from subprocess import call


## To join all .bed files:
## for i in {1..30}; do cat cluster_match_orthologs_A$i.bed>> cluster_total_out.bed; done


with open("/home/chicky/Downloads/Datasets/Working_files/bedFiles/cluster_total_Dmel.bed") as orig_file, open("clustered_Dmel.bed",'w') as new_fi:
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

call("./twoBitToFa dm3.2bit dmel_clustered.fa -bed=clustered_Dmel.bed", shell=True)


replace_lines = open("clustered_Dmel.bed")  ## The used .bed file. The strand information is taken from this file

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


f_file = open("dmel_clustered.fa")  ## The input FASTA file. This does not contain strand information and reverse complement hasn't been done
out_file = open("all_clusters_from_Dmel.fa","w")  ## The required output FASTA file.
elements = f_file.readlines()
seq_list = []
for index in range(0,len(elements),3):  ## Combining the three lines of sequences
    tmp = elements[index+1]+elements[index+2]
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

with open("image_code_matrix_Dmel_all_clusters.csv",'w') as matrix_file:
    #matrix_file.writelines(','.join(i)+'\n' for i in list_of_seq)
    w = csv.writer(matrix_file, dialect='excel')
    w.writerows(list_of_seq)
########### The CSV File is Created###########################################
