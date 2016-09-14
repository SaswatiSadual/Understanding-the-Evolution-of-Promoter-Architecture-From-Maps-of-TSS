Sequences_10000 <- read.delim("architectureDetails.txt", header=FALSE)
Sequences_TSS <- read.delim("~/PromoterClassify_for_whole_genome/architecture_TSS.txt", header=FALSE)

pdf("Histogram_for_10000_TSS_comparison.pdf", paper="USr")
##hist(Sequences_10000$V4, col=rgb(0,0,1,0.25), breaks=100)
hist(Sequences_TSS$V4, col=rgb(1,0,0,0.25), breaks=100)
hist(Sequences_10000$V4, col=rgb(0,0,1,0.25), breaks=100, add=T)
dev.off() 
