##with open("/home/chicky/Downloads/Datasets/Working_files/Misc/modEncode_2625/interpreted_data_files/2625_A-Female_7T_peaks_modified.bed") as proteinBindSite, open("/home/chicky/Downloads/Datasets/Working_files/Protein_binding_site_comparison/Orthologous_sequences_from_Dmel.bed") as dmel_data:

proteinBindSite = open("/home/chicky/Downloads/Datasets/Working_files/Misc/modEncode_2625/interpreted_data_files/2625_A-Female_7T_peaks_modified.bed")
dmel_orthologs = open("/home/chicky/Downloads/Datasets/Working_files/Protein_binding_site_comparison/Orthologous_sequences_from_Dmel.bed")

proteinBind_start_site = []
proteinBind_end_site = []

TSS_start_site_1 = []
TSS_start_site_2 = []

for line in proteinBindSite:
    l = line.strip().split()
    proteinBind_start_site.append(int(l[]))



