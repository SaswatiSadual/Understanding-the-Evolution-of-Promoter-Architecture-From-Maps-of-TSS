fas_file = open("output_cluster_file.fa")

content = fas_file.readlines()
seq_list = []
for index in range(1,len(content),2):
    #content[index] = content[index].replace('\n','').replace('>','')

    seq_list.append(content[index])


pixel_value = {'A':1, 'a':1, 'T':2, 't':2, 'G':3, 'g':3, 'C':4, 'c':4} ## each nucleotide is coded
list_of_seq = []
for i in range(len(seq_list)):
    seq_list[index] = seq_list[index].replace('\n','')
    p = list(seq_list[i])
    pixValue = [pixel_value[x] for x in p]
    #print(pixValue)
    list_of_seq.append(pixValue)
    #print(list_of_seq)

### The sequences that were stored in the nested list were converted into a CSV record file.
### Each row has the corresponding sequence of the Supp_File_S5_CAGE_Dpse_F_carcass.bed file.
import csv

with open("image_code_matrix_total_ortholog_fasta.csv",'w') as matrix_file:
    #matrix_file.writelines(','.join(i)+'\n' for i in list_of_seq)
    w = csv.writer(matrix_file, dialect='excel')
    w.writerows(list_of_seq)
########### The CSV File is Created###########################################
