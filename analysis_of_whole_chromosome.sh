#!/bin/bash


for((index=1040000;index<23011544;index=$(($index+10000))));  
do
	echo "A new directory is being created. If the directory exists, then a new directory will be created, with the name PromoterArchitectureAnalysis_1: "
	p=0
	while ! mkdir PromoterArchitectureAnalysis_chr2L_$p
	do
		p=$((p+1))
	done

	cd PromoterArchitectureAnalysis_chr2L_$p


	echo "FASTA File creation Starts. Check!"
	## Start Site
	##start_site=250000
	start_site=$index
	
	## Total number of sequences considered
	total_sequences=10000 
	
	## Ending Site
	end_site=$(($start_site+$total_sequences)) 

	echo "Start site: " $start_site > DetailsFile_to_$end_site.txt
	echo "Start site: " $start_site
	echo "Ending site: " $end_site >> DetailsFile_to_$end_site.txt
	echo "Ending site: " $end_site

	static=91 ## Window size = 91

	## Creating the temporary file:
	touch temporaryFile.fa
	## Take nucleotides 91 at a time till you complete the chromosome:
	for((i=$start_site;i<$end_site;i++));  
		do  
			## Create the fasta file of the 91 nucleotides:		
			/export/apps/kent/twoBitToFa ~/PromoterClassify_for_whole_genome/dm3.2bit dmel_sequences.fa -seq=chr2L -start=$i -end=$(($i+$static))
			#./twoBitToFa ~/PromoterClassify_for_whole_genome/dm3.2bit dmel_sequences.fa -seq=chr2L -start=$i -end=$(($i+$static))
		
			## Append the contents of dmel_sequences.fa into the file all_sequences_from_dmel.fa
			cat dmel_sequences.fa >> temporaryFile.fa
		done	
	
	## Remove the unnecessary newlines from the FASTA File:
	awk '!/^>/ { printf "%s", $0; n = "\n" } /^>/ { print n $0; n = "" } END { printf "%s", n }' temporaryFile.fa > all_sequences_from_dmel.fa 
	
	## Removing the temporary and unneccessary files:
	rm temporaryFile.fa
	## rm chromosomedata.fa
	rm dmel_sequences.fa
	
	## Removing the repeats for the FASTA file:
	echo "The repeat sequences are removed from the FASTA file: "
	/state/partition/data1/opt/python/bin/python3 ~/PromoterClassify_for_whole_genome/removing_repeats.py
	

	mv final_fasta_file_without_repeats.fa final_fasta_file_without_repeats_$end_site.fa
	## rm all_sequences_from_dmel.fa  ## Removing the FASTA file with the repeats
	echo "Process completed. Required fasta file is final_fasta_file_without_repeats_$end_site.fa"
	
	##  Running promoterClassify on the created FASTA file:
	echo "Now running promoterClassify on the formed fasta file"

	~/NPLB_modified/promoterClassify -f final_fasta_file_without_repeats_$end_site.fa -m ~/Lambda0/arch_30/bestModel.p -o testPromoterClassify_new_$end_site -i 0
	
	
	#cd testPromoterClassify_new_$end_site
	
	## Deleting the html_files folder:
	#rm -r html_files
	
	## Creating Histogram of the architectureDetails data and overlapping it with the TSS data:
	#echo "TSS Start site: RED" > ColorCode.txt
	#echo "10000 Sequences: Blue" >> ColorCode.txt
	#Rscript ~/PromoterClassify_for_whole_genome/creatingHistogram.R
	#echo "The overlapping histogram is created"

	## Finding the sequences with score less than -4000 
	## Creating FASTA files for the sequences
	
	#Rscript ~/PromoterClassify_for_whole_genome/createFASTA.R 
	#echo "The FASTA file of the sequences with score greater than -4000 is created."
	
	## Running promoterClassify again on the sequences which have a score less than -4000
	#echo "The promoterClassify is being used on the FASTA file, to find the presence of promoters in the sequences"
	#~/NPLB_modified/promoterClassify -f Score_greater_than_minus_4000.fa -m ~/Lambda0/arch_30/bestModel.p -o classifyingPromotersWithScoreGreaterThan4000 -i 0
	#cd classifyingPromotersWithScoreGreaterThan4000
	
	## Removing unneccessary files
	#rm -r html_files
	
	cd ~/PromoterClassify_for_whole_genome
	
	## Appending all the data in the architectureDetails.txt of all 10000 sequences into a single file:
	echo "The architectureDetails.txt files of all the 10000 sequences is appended into ArchitectureDetails_all_files.txt file in DESCENDING order."
	cat PromoterArchitectureAnalysis_chr2L_$p/testPromoterClassify_new_$end_site/architectureDetails.txt >> ArchitectureDetails_all_files.txt
	Rscript arranging_the_data_according_to_score.R
	
	## Intersect the BED files
	echo "The BED file of the Transcription Start and End Sites from refSeq.txt is created: refGene_txStart_txEnd.bed"
	echo "The intersection of the BED files with counts and sequences is being done..."
	/state/partition/data/shubhada/bedtools-2.17.0/bin/intersectBed -a arch_details_all_bedFile.bed -b refGene_txStart_txEnd.bed -u > overlappingSequences_in_refGene_chr2L.bed
	#echo "The gene count file is overlappingSequences_in_refGene_chr2L.bed"
	echo "The process is completed."
	rm -r PromoterArchitectureAnalysis_chr2L_$p	
done

#rm -r PromoterArchitectureAnalysis_chr2L_$p
