# Title     : PCA_notes_college
# Objective : test PCA
# Created by: F.DUNAN
# Created on: 25/10/17
library(FactoMineR)
notes <- read.table("notes college.txt",header=TRUE, sep="\t",dec=".",row.names=1)
summary(notes)
res.pca <- PCA(notes,quanti.sup=4,quali.sup=5:6)
summary(res.pca)