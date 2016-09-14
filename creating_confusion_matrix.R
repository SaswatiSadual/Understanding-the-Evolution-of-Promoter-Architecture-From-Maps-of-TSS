df1 <- read.table("/home/chicky/Downloads/Datasets/Working_files/architectureDetails/architectureDetails_Dmel.txt", header = FALSE)
Dmel_data <- data.frame(df1)
colnames(Dmel_data) <- c("Architecture","Details_and_orthoID","Sequences")

df2 <- read.table("/home/chicky/Downloads/Datasets/Working_files/architectureDetails/architectureDetails_Dpse.txt", header = FALSE)
Dpse_data <- data.frame(df2)
colnames(Dpse_data) <- c("Architecture","Details_and_orthoID","Sequences")

x <- Dmel_data$Architecture ## The D.melanogaster clusters
y <- Dpse_data$Architecture ## The D.pseudoobsura clusters
confusionMatrix <- matrix(,nrow = 12, ncol = 12)

for(i in 1:12){for(j in 1:12){confusionMatrix[i][j]=0}}
for(i in x){
  for(j in y){
    confusionMatrix[i][j] = confusionMatrix[i][j]+1
  }
}

