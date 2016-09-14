## To find out the gene ID of the orthologos genes in D.pseudoobscura

OrthoDB6_Drosophila_tabtext <- read.delim("~/Downloads/Datasets/Working_files/OrthoDB6_Drosophila_tabtext")
Dpse_data <- subset(OrthoDB6_Drosophila_tabtext, OrthoDB6_Drosophila_tabtext[,'UniProt_Species']=='DROPS')
orthologs_in_thirty_clusters_Dpse <- read.delim("~/Downloads/Datasets/Working_files/orthologs_in_thirty_clusters_Dpse.bed", header=FALSE)
colnames(orthologs_in_thirty_clusters_Dpse)<- c('Group','start','end','ODB6_OG_ID','value','Strand','value2')

## The intersection of the OrthoDB IDs gives 2958 IDs common to the D.pseudoobscura file and the ortholog files.
## Which means, manually search for the missing ones! -_-
temp<- intersect(orthologs_in_thirty_clusters_Dpse$ODB6_OG_ID,Dpse_data$ODB6_OG_ID)

## Now find out all those orthoIDs which are present in orthologs_in_thirty_clusters_Dpse, but not in Dpse_data
#onlyOrtho <- setdiff(orthologs_in_thirty_clusters_Dpse$ODB6_OG_ID, Dpse_data$ODB6_OG_ID)

## Select the Gene_ID of those records where orthologs_thirty_clusters_Dpse$ODB6_OG_ID are in 
## Dpse_data$ODB6_OG_ID
#test_var <- merge(orthologs_in_thirty_clusters_Dpse, Dpse_data, by="ODB6_OG_ID") ## Created a table by merging
test_var <- merge(Dpse_data, orthologs_in_thirty_clusters_Dpse, by="ODB6_OG_ID")
list_df <- as.data.frame(test_var$Gene_ID)
write.csv(list_df,"list_of_genes", row.names = FALSE, quote = FALSE)



## Gene ID according to the Architecture:
architectureData <- read.delim("~/Downloads/Datasets/Working_files/architectureDetails_Dpse_PromoterLearn2.txt", header=FALSE)
colnames(architectureData) <- c("architecture_number","Details","Sequence","ODB6_OG_ID")
library(plyr)
arranged_data <- arrange(architectureData, architecture_number)
arch1 <- arranged_data[arranged_data$architecture_number==1,]
#write.table(arch1,"architecture1_values", sep = '\t',quote = FALSE, append = TRUE )
orthoDB_list <- list(arch1$OrthoDB6_ID)
#list_of_genes <- test_var[test_var$ODB6_OG_ID %in% orthoDB_list]

common_list_to_find_genes <- merge(arch1,test_var, by = "ODB6_OG_ID")
#################### Separating the files:
list_architecture_1 <- arranged_data[,[]]

## GO term analysis of Architecture 1
chart_F4DF3D0FFA2B1464344045370 <- read.delim("~/Downloads/Datasets/Working_files/cluster_annotation_DAVID/chart_F4DF3D0FFA2B1464344045370.txt")
write.table(chart_F4DF3D0FFA2B1464344045370,"architecture1.csv",sep = '\t', quote = FALSE, row.names = FALSE)

## Plotting the 