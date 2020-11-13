library(phyloseq)
library(qiime2R)
library(ggplot2)
library(reshape)
library(DESeq2)
library(tidyverse)
library(ggrepel)


setwd('/Users/sophiecurio/16s/Sophie/')

Genotypes = c("APC_KO3", "KO_ctrl")
Timepoints = "18"
name <- paste(Genotypes, Timepoints, collapse = '_')

phy<-qza_to_phyloseq("table.qza", "rooted-tree.qza", "taxonomy.qza","metadata_phyloseq2.tsv")

# only keep samples with > 2500 feature IDs
# phy = prune_samples(sample_sums(phy) > 2500, phy)
phy = tax_glom(phy, taxrank="Family", bad_empty=c(NA, "", " ", "\t"))
phy

#Remove taxa not seen more than 10 times in at least 20% of the samples
#phy = filter_taxa(phy, function(x) sum(x > 10) > (0.2*length(x)), TRUE)

# select subset
phy = subset_samples(phy, Timepoint %in% Timepoints)
phy = subset_samples(phy, Genotype %in% Genotypes)

phy_deseq = phyloseq_to_deseq2(phy, ~ Genotype)
phy_deseq = DESeq(phy_deseq, test="Wald", fitType="parametric")

res = results(phy_deseq, cooksCutoff = FALSE)
alpha = 0.05
sigtab = res[which(res$padj < alpha), ]
sigtab = cbind(as(sigtab, "data.frame"), as(tax_table(phy)[rownames(sigtab), ], "matrix"))

sigtab

#plot by differentially expressed genus
library("ggplot2")
theme_set(theme_bw())
scale_fill_discrete <- function(palname = "Set1", ...) {
  scale_fill_brewer(palette = palname, ...)
}
# Phylum order
x = tapply(sigtab$log2FoldChange, sigtab$Phylum, function(x) max(x))
x = sort(x, TRUE)
sigtab$Phylum = factor(as.character(sigtab$Phylum), levels=names(x))
# Genus order
x = tapply(sigtab$log2FoldChange, sigtab$Genus, function(x) max(x))
x = sort(x, TRUE)
sigtab$Genus = factor(as.character(sigtab$Genus), levels=names(x))

#plot significant genus
png(file = paste("R/DESeq2/test", paste(name, '_sig.png'), sep = ''), units="in", width=5, height=5, res=300)
ggplot(sigtab, aes(x=Family, y=log2FoldChange, color=Phylum)) + geom_point(size=6) + 
  theme(axis.text.x = element_text(angle = -90, hjust = 0, vjust=0.5))
dev.off()

#sig features into list
sig_features <- as.vector(rownames(sigtab))
head(sigtab)

#make csv with sig diff OTUs
file = paste("R/DESeq2/test", paste(name, '.csv'), sep ='')
write.csv(sigtab, file)

#volcao plot
png(file = paste("R/DESeq2/test", paste(name, '_volcano.png'), sep = ''), units="in", width=5, height=5, res=300)
plotMA(res)
dev.off()

#plot normalised counts
for (i in sig_features) {
  print(i)
  png(file = paste("R/DESeq2/", paste(name, i, 'counts.png'), sep = '_'), units="in", width=5, height=5, res=300)
  d  <- plotCounts(phy_deseq, gene=i, intgroup="Genotype")
  dev.off()
}


# plot individual genes with sample names
d  <- plotCounts(phy_deseq, gene='5c1e8168883cd2f3674c03502010ebec', intgroup="Genotype", returnData=TRUE)
ggplot(d, aes(x = Genotype, y = count)) + 
  geom_point(position=position_jitter(w = 0.1,h = 0)) +
  geom_text_repel(aes(label = rownames(d))) + 
  theme_bw() +
  ggtitle('5c1e8168883cd2f3674c03502010ebec') +
  theme(plot.title = element_text(hjust = 0.5))
