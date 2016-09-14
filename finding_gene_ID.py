records_list = []
#file_rec = []
#with open("OrthoDB6_Drosophila_tabtext") as dpse:
#    for line in dpse:
#        record = line.split()
#        records_list.append(record)
with open("OrthoDB6_Drosophila_tabtext") as drosophila, open("D_pseudoobscura_data",'w') as outfile:
    for line in drosophila:
        l = line.strip().split(sep='\t')
        if l[6]=='DROPS':
            print('\t'.join(l)+'\n')
            temp = '\t'.join(l)
            outfile.write(temp+'\n')


with open("orthologs_in_thirty_clusters_Dpse.bed") as Dpse, open("geneIDFiles",'w') as outfile:
    for line1 in Dpse:
        lDmel = line1.strip().split()
        for index in range(len(records_list)):
            if lDmel[3]==records_list[index][1] and records_list[index][5]=='DROPS':

                #temp = '\t'.join(records_list[index])
                temp = records_list[index][3]
                #print(len(temp))
                #file_rec.append(temp)
                #print(temp)
                outfile.write(temp+'\n')
