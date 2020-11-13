library(phyloseq)
library(ggplot2)
library(reshape)
library(qiime2R)

setwd('/Users/sophiecurio/Dropbox/APC_project/16s/Sophie/')
phy<-qza_to_phyloseq("table.qza", "rooted-tree.qza", "taxonomy.qza","metadata_phyloseq2.tsv")

Genotypes = c("APC_WT3", "WT_ctrl")
Timepoints = c("18")
name <- paste(Genotypes, Timepoints, collapse = '_')


# only keep samples with > 2500 feature IDs
phy = prune_samples(sample_sums(phy) > 2500, phy)

# select subset
phy = subset_samples(phy, Genotype %in% Genotypes)
phy = subset_samples(phy, Timepoint %in% Timepoints)



# plot all alpha diversity parameters by timepoint/genotype
png(file = paste("R/", paste('richness1.png'), sep = ''), units="in", width=18, height=10, res=300)
plot_richness(phy, x = 'Timepoint', color = 'Genotype')
dev.off()


# plot only specific parameteres with boxplot with p value
rich = estimate_richness(phy)
p_value <- wilcox.test(rich$Shannon, sample_data(phy)$Genotype)$p.value
rich$Shannon

shannon <- estimate_richness(phy, measure=c("Shannon"))
shannon

png(file = paste("R/Alpha_plots/", paste(name, '_alpha_observed.png'), sep = ''), units="in", width=5, height=5, res=300)
p <- plot_richness(phy, x="Genotype", measures=c("Shannon"))
plot(p)
#  + geom_text(aes(label=Mouse_ID)) + ggtitle(paste(name, '\np =', p_value))
dev.off()

