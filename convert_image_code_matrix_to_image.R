# Get the pixel matrix created from the program finding_sequences_from_orthologous.py

# This is the code matrix of the nucleotide sequences:
pixelMatrix <- t(as.matrix(read.csv("image_code_matrix_Dpse_Orthologs.csv", sep = ',',header = FALSE)))

#Dictionary in finding_sequences_from_orthologous.py
## Set the color code for each valie in the matrix
####### Use this to compare with Chen et al. 
# A = 1 (Red), T = 2 (Yellow), G =3 (Blue), C = 4 (Green) as set in the 
#color_code <- c('1'= "#FF0000", '2'="#FFFF00", '3'="#0000A0", '4'="#008000")

####### Use this to compare with Mitra and Narlikar.
# Color code: A (1) = Green, T(2) = Red, G(3) = Yellow, C(4) = Blue
#color_code <- c('1'= "#008000", '2'="#FF0000", '3'="#FFFF00", '4'="#0000A0")
##A = 008000 C = 0000FF G= FFA500 T= FF0000

color_code <- c('1'= "#008000", '2'="#FF0000", '3'="#FFA500", '4'="#0000FF")
## Image is created. 
row_val <- nrow(pixelMatrix)
v <- row_val/2
x <-(-v:v)
#image(1:nrow(pixelMatrix), 1:ncol(pixelMatrix), as.matrix(pixelMatrix), col=color_code)
image(x, 1:ncol(pixelMatrix), as.matrix(pixelMatrix), col=color_code)
foo <- read.table("coordinates.txt",header = FALSE)
for(index in 1:length(foo[[1]]))
  { 
    coordinate = foo[[1]][index]
    abline(h=coordinate)
}
pixelMatrix <- t(as.matrix(read.csv("image_code_matrix.csv", sep = ',',header = FALSE)))

## Set the color code for each valie in the matrix
# A = 1 (Red), T = 2 (Green), G =3 (Blue), C = 4 (Black) as set in the 
#Dictionary in finding_sequences_from_orthologous.py

color_code <- c('1'= "#FF0000", '2'="#00FF00", '3'="#0000FF", '4'="#000000")

## Image is created. 
image(1:nrow(pixelMatrix), 1:ncol(pixelMatrix), as.matrix(pixelMatrix), col=color_code)
