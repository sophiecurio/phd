library(phyloseq)
library(ggplot2)
library(reshape)
library(qiime2R)
library(psadd)

#to install KronaTools, navigate to KronaTools folder in terminal ./install.pl

setwd('/Users/sophiecurio/Dropbox/APC_project/16s/Sophie/')
phy<-qza_to_phyloseq("table.qza", "rooted-tree.qza", "taxonomy.qza","metadata_phyloseq2.tsv")

Genotypes = c("APC_WT3")
Timepoints = c("3", "10", "18", "50")
name <- paste(Genotypes, Timepoints, collapse = '_')

phy = subset_samples(phy, Genotype %in% Genotypes)
phy = subset_samples(phy, Timepoint %in% Timepoints)

plot_krona(phy, output='krona', variable='Timepoint', trim = F, color = TRUE)