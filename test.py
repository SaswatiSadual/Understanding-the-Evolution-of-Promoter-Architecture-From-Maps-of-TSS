

for line in replace_lines:
    record = line.strip().split()
    record = record[3]

    for strand in record:
        if strand.__contains__("-"):
            fasta_file_read.readline()
            for i in range(3):
                L = fasta_file_read.readline()
                L = fasta_file_read.append(L)
                L = L.replace('\n','')
            print(L)




replace_lines = open("newfile.bed")

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

f_file = open("dm3_output.fa")
out_file = open("outfile.fa","w")
elements = f_file.readlines()
for index in range(0,len(elements),4):
    tmp = elements[index+1]+elements[index+2]+elements[index+3]
    sequence = tmp.replace('\n','')
    if elements[index].__contains__(">-"):
        sequence = reverseCompliment(sequence)
    #elements[1] = sequence
    #out_file.write(">"+replace_lines.readline()+'\n')

    #out_file.write(sequence+'\n')
    #print(">"+replace_lines.readline()+'\n')
    #print(sequence)
    out_file.write(">"+replace_lines.readline())
    out_file.write(sequence+'\n')
    #elements.pop(0)
    #elements.pop(0)
    #index = index+4



with open("file") as infile, open("output") as outfile:
    for j in range(len(orthologous_sequence)):
        for line in infile:
            l = line.strip().split()
            if orthologous_sequence[j]==l[3]:
                temp = '\t'.join(l)
                print(temp)
                outfile.write(temp+'\n')