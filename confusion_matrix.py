from sklearn.metrics import confusion_matrix
import numpy as np
dmel_value = []
with open("/home/chicky/Downloads/Datasets/Working_files/architectureDetails/architectureDetails_Dmel.txt") as dmel:
    for line in dmel:
        l = line.strip().split()
        dmel_value.append(int(l[0]))

dpse_value = []
with open("/home/chicky/Downloads/Datasets/Working_files/architectureDetails/architectureDetails_Dpse.txt") as dpse:
    for line in dpse:
        l = line.strip().split()
        dpse_value.append(int(l[0]))

confusionMatrix = confusion_matrix(dmel_value,dpse_value) ## x = obtained value, y = predicated value

np.savetxt("confusion_matrix.txt",confusionMatrix, fmt='%d', delimiter='\t')
np.savetxt("confusin_matrix.csv", confusionMatrix, fmt='%d',delimiter=',')
