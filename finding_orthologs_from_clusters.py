from subprocess import call
proteinList_Dmel = []
#with open("Supp_File_S1_CAGE_Dmel_FM_carcass.bed") as Dmel:
with open("/home/chicky/Downloads/Datasets/Working_files/bedFiles/A2") as Dmel:
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
ortho_sequences = list(set(proteinList_Dpse).intersection(proteinList_Dmel))
## There are 5660 orthologs
#################### Found the orthologous proteins ####################################

## Compare these orthologs with the D.melanogaster cluster .bed files.

#with open("Supp_File_S5_CAGE_Dpse_F_carcass.bed") as infile, open("orthologs_in_thirty_clusters_Dpse_test.bed",'a') as outfile:
#    for line in infile:
#        l = line.strip().split()
#        for j in range(len(ortho_sequences)):

#            if ortho_sequences[j]==l[3]:
#                temp = '\t'.join(l)
#                #print(temp)
#                outfile.write(temp+'\n')


records_list = []
#file_rec = []
with open("Supp_File_S5_CAGE_Dpse_F_carcass.bed") as dpse:
    for line in dpse:
        record = line.split()
        records_list.append(record)

with open("/home/chicky/Downloads/Datasets/Working_files/bedFiles/cluster_total_Dmel.bed") as Dmel, open("orthologs_in_thirty_clusters_Dpse.bed",'w') as outfile:
    for line1 in Dmel:
        lDmel = line1.strip().split()
        for index in range(len(records_list)):
            if lDmel[3]==records_list[index][3]:
                temp = '\t'.join(records_list[index])
                #print(len(temp))
                #file_rec.append(temp)
                outfile.write(temp+'\n')

with open("orthologs_in_thirty_clusters_Dpse.bed") as orig_file, open("cleaned_bed_file_of_orthologs_in_Dpse_clusters.bed",'w') as new_fi:
    for line in orig_file:
        L = line.strip().split()
        if (L[5] == '+'):
            # L[1] = str(int(L[1]) - 46)
            # L[2] = str(int(L[2]) + 47)
            L[1] = str(int(L[1]) - 46)
            L[2] = str(int(L[2]) + 44)
        else:
            L[1] = str(int(L[1]) - 44)
            L[2] = str(int(L[2]) + 46)

        L.pop(6)
        L.pop(4)
        L.pop(3)
        val = '\t'.join(L)
        new_fi.write(val + '\n')


call("./twoBitToFa dp4.2bit dpse_output_ortho.fa -bed=cleaned_bed_file_of_orthologs_in_Dpse_clusters.bed", shell=True)

replace_lines = open("orthologs_in_thirty_clusters_Dpse.bed")
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


f_file = open("dpse_output_ortho.fa")  ## The input FASTA file. This does not contain strand information and reverse complement hasn't been done
out_file = open("All_orthologs_fasta_Dpse.fa","w")  ## The required output FASTA file. This will be used in NPLB
elements = f_file.readlines()
seq_list = []
for index in range(0,len(elements),3):  ## Combining the three lines of sequences
    #tmp = elements[index+1]+elements[index+2]+elements[index+3]
    tmp = elements[index + 1] + elements[index + 2]
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

with open("image_code_matrix_Dpse_Orthologs.csv",'w') as matrix_file:
    #matrix_file.writelines(','.join(i)+'\n' for i in list_of_seq)
    w = csv.writer(matrix_file, dialect='excel')
    w.writerows(list_of_seq)
########### The CSV File is Created###########################################



############# To join two or more images:
## convert Dmel_orthologs_NPLB.png Dpse_orthologs_NPLB.png +append finalimage.png