from subprocess import call

with open("/home/chicky/Downloads/Datasets/Working_files/Test_folder_bedFiles_Dmel/A27") as orig_file, open("/home/chicky/Downloads/Datasets/Working_files/Test_folder_bedFiles_Dmel/A27_modified.bed","w") as new_fi:
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

call("./twoBitToFa dm3.2bit /home/chicky/Downloads/Datasets/Working_files/Test_folder_bedFiles_Dmel/Dmel_A27.fa -bed=/home/chicky/Downloads/Datasets/Working_files/Test_folder_bedFiles_Dmel/A27_modified.bed", shell=True)


##### Editing the FASTA file. The reverse complement of the negative strand is taken. #################
#replace_lines = open("ortholog_sequences.bed")  ## The used .bed file. The strand information is taken from this file
replace_lines = open("/home/chicky/Downloads/Datasets/Working_files/Test_folder_bedFiles_Dmel/A27")
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


f_file = open("/home/chicky/Downloads/Datasets/Working_files/Test_folder_bedFiles_Dmel/Dmel_A27.fa")  ## The input FASTA file. This does not contain strand information and reverse complement hasn't been done
out_file = open("/home/chicky/Downloads/Datasets/Working_files/Test_folder_bedFiles_Dmel/Dmel_A27_final.fa","w")  ## The required output FASTA file. This will be used in NPLB
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
    out_file.write(">"+replace_lines.readline().replace('\t',',')) ## Writing the strand information
    out_file.write(sequence+'\n')                ## Writing the sequence into the file.