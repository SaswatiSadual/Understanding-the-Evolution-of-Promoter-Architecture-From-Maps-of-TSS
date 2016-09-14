setwd("~/Downloads/Datasets/Working_files/image_files");
files <- list.files(path=".", pattern="*.png", all.files=T, full.names=T)
filelist <- lapply(files, readPNG)
names(filelist) <- paste0(basename((files)))
list2env(filelist, envir=.GlobalEnv)


par(mar=rep(0,4))
layout(matrix(1:length(names(filelist)), bycol =TRUE))

for(i in 1:length(names(filelist))) {
  img <- readPNG(names(filelist[i]))
  plot(NA,xlim=0:1,ylim=0:1,xaxt="n",yaxt="n")
  rasterImage(img,0,0,1,1)
}


dev.print(pdf, "output.pdf") 