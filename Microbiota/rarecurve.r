library(phyloseq)
library(ggplot2)
library(reshape)
library(qiime2R)
library(vegan)

setwd('/Users/sophiecurio/16s/Sophie/')

phy<-qza_to_phyloseq("table.qza", "rooted-tree.qza", "taxonomy.qza","metadata_phyloseq2.tsv")
phy

png(file = paste("R/DESeq2/", paste('rarecurve.png'), sep = ''), units="in", width=12, height=8, res=300)
rarecurve(t(otu_table(phy)), step=50, cex=0.5)
dev.off()

# only keep samples with > 2500 feature IDs
phy = prune_samples(sample_sums(phy) > 2500, phy)

png(file = paste("R/DESeq2/", paste('rarecurve_afterexclusion.png'), sep = ''), units="in", width=12, height=8, res=300)
rarecurve(t(otu_table(phy)), step=50, cex=0.5)
dev.off()
