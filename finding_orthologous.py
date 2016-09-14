#Dmel = open("Supp_File_S1_CAGE_Dmel_FM_carcass.bed")
#Dpse = open("Supp_File_S5_CAGE_Dpse_F_carcass")


<<<<<<< HEAD

proteinList_Dmel = []
with open("Supp_File_S1_CAGE_Dmel_FM_carcass.bed") as Dmel:
        for rec in Dmel:
            values = rec.strip().split()
            proteinList_Dmel.append(values[3])

print(proteinList_Dmel)

proteinList_Dpse = []
with open("Supp_File_S5_CAGE_Dpse_F_carcass.bed") as Dpse:
    for r in Dpse:
        val = r.strip().split()
        proteinList_Dpse.append(val[3])

print(proteinList_Dpse)
    
ortho_sequences = set(proteinList_Dpse).intersection(proteinList_Dmel)
=======
def orthologs() -> object:
    proteinList_Dmel = []
    with open("Supp_File_S1_CAGE_Dmel_FM_carcass.bed") as Dmel:
            for rec in Dmel:
                values = rec.strip().split()
                proteinList_Dmel.append(values[3])

    print(proteinList_Dmel)

    proteinList_Dpse = []
    with open("Supp_File_S5_CAGE_Dpse_F_carcass.bed") as Dpse:
        for r in Dpse:
            val = r.strip().split()
            proteinList_Dpse.append(val[3])

    print(proteinList_Dpse)
    
    ortho_sequences = set(proteinList_Dpse).intersection(proteinList_Dmel)
    return ortho_sequences
>>>>>>> c8ab41bd9df7dd94ba3163cd61bd4329f5ea2402
