## Reading the architectureDetails.txt file into a dataframe
library(seqinr)

architectureDetailsFile <- read.delim("architectureDetails.txt", header=FALSE)

## Selecting the records where the score of the sequence is greater than -4000
greater_than_minus_4000 <- subset(architectureDetailsFile, architectureDetailsFile$V4>-4000)

## Creating the FASTA file of the sequences which have score greater than -4000
sequences_from_file <- as.list(greater_than_minus_4000$V3)
names_of_sequences <- as.character(greater_than_minus_4000$V2)
write.fasta(sequences = sequences_from_file, names = names_of_sequences, file.out = "Score_greater_than_minus_4000.fa", open = 'w', nbchar = 91)


