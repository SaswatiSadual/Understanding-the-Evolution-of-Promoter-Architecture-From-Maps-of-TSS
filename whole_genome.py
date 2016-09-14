from subprocess import call

## Create windows of size 40



call("./twoBitToFa dm3.2bit dmel_all.fa -seq=chr2L -start=0 -end=91", shell=True)
with open("dmel_all.fa") as tempFile, open("all_sequences_Dmel.fa",'a') as outfile:
    f = tempFile.readlines()



chromosomes = ['chr2L', 'chrX', 'chr3L', 'chr2R', 'chr3R', 'chr4']

