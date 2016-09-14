library("plyr")

## Import the details in the file to a data frame in R
architectureDetails_combined_greater_minus_4000 <- read.delim("ArchitectureDetails_all_files_without_sequences.txt", header=FALSE)

## Arrange the contents of the file according to the fourth column i.e. the score:
arranged_data <- arrange(architectureDetails_combined_greater_minus_4000, desc(architectureDetails_combined_greater_minus_4000$V2))

## Write the data into a file:
#write.table(arranged_data, file="arranged_architecture_details_all.txt", row.names=FALSE, col.names=FALSE, quote=FALSE, sep='\t')

## Create the BED File out of it:
#arranged_architecture_details <- read.delim("arranged_architecture_details_all.txt", header=FALSE, quote="")
#to_create_bedFiles <- arranged_architecture_details$V2
to_create_bedFiles <- arranged_data$V1
score_values <- arranged_data$V2
to_write_to_file <- gsub(":","\t",to_create_bedFiles)
to_final <- gsub("-", "\t", to_write_to_file)
dataFrame_of_all_fields <- data.frame(cbind(to_final, score_values))
## Write the chromosome name, startSite and endSite into the Score_less_than_minus_4000bedFile.bed: 
write.table(dataFrame_of_all_fields, file = "NEW_arch_details_all_bedFile.bed", quote = FALSE, sep = "\t", row.names = FALSE, col.names = FALSE)
