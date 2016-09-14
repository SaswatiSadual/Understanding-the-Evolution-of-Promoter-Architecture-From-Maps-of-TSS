
with open("/home/chicky/Downloads/Datasets/Working_files/bedFiles/A2") as clusterFile, open("/home/chicky/Downloads/Datasets/Working_files/bedFiles/modified_A2",'w') as modifiedClusterA1:

    for line in clusterFile:
        l = line.strip().split()
        tmp = l+['2']
        print(tmp)
        t = '\t'.join(tmp)
        modifiedClusterA1.write(t+'\n')