#while (arranged_data$V1==1) {
#  if(grepl(arranged_data$V2,test_var$ODB6_OG_ID)==TRUE){
#    write.table(test_var$Gene_ID, file = "architecture1", append = TRUE, sep = '\n')
#  }
#}


test_var$new <- gsub('_.*', '', test_var$start)
arch1$new <- ifelse(grepl('_', arch1$Details), gsub('_.*', '', arch1$Details),substring(arch1$Details, 1, 4))

arch1$Gene_ID <- sapply(arch1$new, function(i) test_var$Gene_ID[match(i, test_var$new)])


arch1 <- arranged_data[arranged_data$architecture_number==11,]
orthoDB_list <- list(arch1$OrthoDB6_ID)
common_list_to_find_genes <- merge(arch1,test_var, by = "ODB6_OG_ID")
list_of_genes <- list(common_list_to_find_genes$Gene_ID)
write.table(list_of_genes,"genes_in_architecture11.txt",quote = FALSE, row.names = FALSE)

architecture6_functional_annotation_chart <- read.delim("~/Downloads/Datasets/Working_files/cluster_annotation_DAVID/architecture5_functional_annotation_chart")

write.table(architecture11_functional_annotation_chart,"architecture11.csv", sep = '\t', quote = FALSE, row.names = FALSE)





####### Finding sequences in architectures to create the FASTA file
list1 <- subset(arranged_data$Sequence, arranged_data$architecture_number==1)
write.table(list1,"sequences_in_architecture1", quote = FALSE, sep = '\n', row.names = FALSE, col.names = FALSE)



## Writing FASTA file:
library("seqinr", lib.loc="~/R/x86_64-pc-linux-gnu-library/3.3")
for(i in 1:312){
  write.fasta(sequences = arch3_of_arch9$V3[i], file.out = "Architecture_fasta.fa", names = arch3_of_arch9$V2[i], open = 'a', nbchar = 100)
}


## Creating FASTA File (FINAL) for NPLB promoterLearn input
## Running NPLB on the 18 architectures
orthoID_in_arch2 <- subset(arranged_data$ODB6_OG_ID, arranged_data$architecture_number==2)
write.table(orthoID_in_arch2, "/home/chicky/Downloads/Datasets/Working_files/architectureDetails/orthoIDs_in_architecture2", quote = FALSE, row.names = FALSE, col.names = FALSE)





## Comparing two columns in two files
Orthologous_sequences_from_Dmel <- read.delim("~/Downloads/Datasets/Working_files/Protein_binding_site_comparison/Orthologous_sequences_from_Dmel.bed", header=FALSE)
View(Orthologous_sequences_from_Dmel)
Female_peaks_modified <- read.delim("~/Downloads/Datasets/Working_files/Protein_binding_site_comparison/Drosophila_melanogaster/3231_7T_3dFemale_peaks_modified.bed", header=FALSE)
View(Female_peaks_modified)

Details_of_TSS_with_TF_binding <- data.frame()
Ortholog_TSS_TF_Binding <- data.frame()
if((Orthologous_sequences_from_Dmel$Start[i] > Female_peaks_modified$Start[i]) && (Orthologous_sequences_from_Dmel$End[i] < Female_peaks_modified$End[i]))
{
  Ortholog_TSS_TF_Binding <- rbind(Ortholog_TSS_TF_Binding, Orthologous_sequences_from_Dmel[,i])
}


## To concatenate strings in R
foo[] <- lapply(foo, function(x) {paste("chr", x, sep = '')})


## Modifying the bed files
dmel.all.r6.11 <- read.delim("~/Downloads/Datasets/Working_files/melanogaster_whole_genome/dmel-all-r6.11.gtf", header=FALSE)
View(dmel.all.r6.11)



## Creating FASTA file from the suspected promoter architectures:
sequences_from_file <- as.list(greater_than_4150$V3)
names_of_sequences <- as.character(greater_than_4150$V2)
write.fasta(sequences = sequences_from_file, names = names_of_sequences, file.out = "Testfile.fa", open = 'w', nbchar = 91)



## Read FASTA File without masking!
library(CHNOSZ)
file <- system.file("all_sequences_from_dmel_10000.fa", package="CHNOSZ")

# Function
ReadFasta<-function(file) {
  # Read the file line by line
  fasta<-readLines(file)
  # Identify header lines
  ind<-grep(">", fasta)
  # Identify the sequence lines
  s<-data.frame(ind=ind, from=ind+1, to=c((ind-1)[-1], length(fasta)))
  # Process sequence lines
  seqs<-rep(NA, length(ind))
  for(i in 1:length(ind)) {
    seqs[i]<-paste(fasta[s$from[i]:s$to[i]], collapse="")
  }
  # Create a data frame 
  DF<-data.frame(name=gsub(">", "", fasta[ind]), sequence=seqs)
  # Return the data frame as a result object from the function
  return(DF)
}

# Usage example
seqs<-ReadFasta(file)




### Elements in data frame A not in data frame B:
findDifference <- function(df1, df2, ...){
  df1p <- do.call("paste",df1)
  df2p <- do.call("paste", df2)
  df1[! df1p %in% df2p, ]
}

## If the rows of newPredProm match with promotersFound, assign 1, else 0

## count_promoters_found has another column with the count of the promoters.
## Import this file into R and set the last column as: if greater than 0, set it 1
count_promoters_found2[count_promoters_found$V4>0,] <- 1

## Plot the precision Recall curve:
pred <- prediction(count_promoters_found2$Score, count_promoters_found2$Label)
perf <- performance(pred, "prec", "rec")
plot(perf)