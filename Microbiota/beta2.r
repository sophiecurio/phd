library(phyloseq)
library(ggplot2)
library(reshape)
library(qiime2R)
library(vegan)

setwd('/Users/sophiecurio/Dropbox/APC_project/Microbiota/Sophie')
phy<-qza_to_phyloseq("table.qza", "rooted-tree.qza", "taxonomy.qza","metadata_phyloseq.tsv")

Genotypes = c("KO_ctrl", 'WT_ctrl')
Timepoints = c("3", "10", "18")
name <- paste(Genotypes, Timepoints, collapse = '_')


# only keep samples with > 2500 feature IDs
phy = prune_samples(sample_sums(phy) > 2500, phy)

# select subset
phy = subset_samples(phy, Genotype %in% Genotypes)
phy = subset_samples(phy, Timepoint %in% Timepoints)


wunifrac_dist = phyloseq::distance(phy, method="unifrac", weighted=F)
ordination = ordinate(phy, method="PCoA", distance=wunifrac_dist)
p<-plot_ordination(phy, ordination, color="Timepoint", shape="Genotype") + theme(aspect.ratio=1) + theme_bw() 
#+ stat_ellipse(type = "t") 



png(file = paste("R/Beta_plots/", paste(Genotypes, '_ctrl_all_beta.png'), sep = ''), units="in", width=5, height=5, res=300)
pdf(file = paste("R/Beta_plots/", paste('3_10_18_ctrl_beta.pdf'), sep = ''), width=5, height=4, useDingbats=FALSE)
plot(p)
dev.off()

adonis(wunifrac_dist ~ sample_data(phy)$Genotype)
