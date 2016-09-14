'''
with open("all_dmel") as infile, open("final_fasta_file_without_repeats.fa") as outfile:
    count = 0
    for line in infile:
        count = count + 1
        if count%2 == 0:

            l = line.strip().split()

from Bio import SeqIO
with open('/home/chicky/Downloads/Datasets/Working_files/melanogaster_whole_genome/all_sequences_from_dmel_10000.fa') as fasta_file:
    identifiers = []
    sequences_in_file = []
    for seq_record in SeqIO.parse(fasta_file, 'fasta'):  # (generator)
        identifiers.append(seq_record.id)
        sequences_in_file.append(seq_record.seq)

## Converting it to Data Frame:
import pandas as pd
table_of_details = pd.DataFrame({'Identifier':identifiers, 'Sequence':sequences_in_file})
'''

# from subprocess import call
with open('/home/chicky/Downloads/Datasets/Working_files/melanogaster_whole_genome/all_sequences_from_dmel.fa') as f, open('/home/chicky/Downloads/Datasets/Working_files/melanogaster_whole_genome/final_fasta_file_without_repeats.fa','w') as outfile:
    lists = [[], []]
    i = 0
    for line in f:
        lists[i].append(line.strip())
        i ^= 1
    for index in range(len(lists[1])):
        ## if lists[1][index] contains lowercase, pop it
        identifier = str(lists[0][index])
        sequence = str(lists[1][index])
        if sequence.isupper() and not sequence.__contains__('N'):
            outfile.write(identifier + '\n')
            outfile.write(sequence + '\n')

# call("mv final_fasta_file_without_repeats.fa final_fasta_file_without_repeats_.fa", shell=True)

# table_of_details = pd.DataFrame({'Identifier':lists[0], 'Sequence':lists[1]})
