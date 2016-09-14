## For cluster A1
A1_proteinID = []
ortho_proteinID = []
#common = []
with open("/home/chicky/Downloads/Datasets/Working_files/bedFiles/A1") as clusterA1, open("Orthologous_sequences_from_Dmel.bed") as orthoSeq:
    for l in clusterA1:
        s = l.strip().split()
        A1_proteinID.append(s[3])

    for l2 in orthoSeq:
        s2 = l2.strip().split()
        ortho_proteinID.append(s2[3])

common = set(A1_proteinID).intersection(ortho_proteinID) ## These are the orthologs that are present in the cluster
#no_seq = open("no_of_elements_in_each_cluster.txt",'a')
#no_seq = open("no_of_elements_in_each_cluster_Dmel.txt",'a')
#no_seq.write(str(len(common))+'\n')

print(len(common))
    ## There are 169 common sequences in the cluster A1

#with open("Orthologous_sequences.bed") as cluster, open("cluster_match_orthologs_A2.bed",'w') as matchSeq:
#    for line in cluster:
#        record = line.strip().split()
#        if record[3] in common:
#            tmp = '\t'.join(record)
#            matchSeq.write(tmp+'\n')
#            print(tmp)
#print(no_seq)
##print(len(common))