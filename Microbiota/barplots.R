library(phyloseq)
library(ggplot2)
library(reshape)
library(qiime2R)
library(microbiome)
library(dplyr)
library(ggrepel)
library(clipr)
library(plyr)
library(svglite)

setwd('/Users/sophiecurio/Dropbox/APC_project/Microbiota/Sophie')
phy<-qza_to_phyloseq("table.qza", "rooted-tree.qza", "taxonomy.qza","metadata_phyloseq2.tsv")

Genotypes = c("WT_ctrl", "KO_ctrl")
Timepoints = c("18")
name <- paste(Genotypes, Timepoints, collapse = '_')

# only keep samples with > 2500 feature IDs
phy = prune_samples(sample_sums(phy) > 2500, phy)

#Remove taxa not seen more than 10 times in at least 20% of the samples
phy = filter_taxa(phy, function(x) sum(x > 10) > (0.2*length(x)), TRUE)

# select subset
phy = subset_samples(phy, Genotype %in% Genotypes)
phy = subset_samples(phy, Timepoint %in% Timepoints)

##save otu table as csv
#table = write_phyloseq(phy, type = "all")


phy.glom = tax_glom(phy, taxrank="Phylum", NArm=FALSE)

#merge all mice into one plot
phy_new = merge_samples(phy.glom, "Phylum")

#plot percentages rather than reads
phy_new = phy.glom
sample_data(phy_new)$Genotype <- levels(sample_data(phy.glom)$Genotype)
phy_new = transform_sample_counts(phy_new, function(x) 100 * x/sum(x))

#Run next few lines if certain taxa should be excluded
phy_new <- tax_glom(phy_new, taxrank = 'Phylum')
phy_new <- psmelt(phy_new)
phy_new$Phylum <- as.character(phy_new$Phylum)
medians <- ddply(phy_new, ~Phylum, function(x) c(median=median(x$Abundance)))
remainder <- medians[medians$median <= 0.05,]$Phylum
phy_new[phy_new$Phylum %in% remainder,]$Phylum <- 'Remainder'

order <- c('a59h', 'a74h', 'a68h', 'wk170', 'a53h', 'a65h', 'a58h', 'a62h')

ggplot(data = phy_new, aes(x=factor(Sample, level =order), y=Abundance, fill=Phylum)) + geom_bar(color = "black", position="stack", stat="identity") +  theme_bw() + labs(y='Abundance (%)') + theme(axis.title.x=element_blank(),
        axis.text.x=element_blank(),
        axis.ticks.x=element_blank(),
        panel.grid.major = element_blank(),
        strip.text.x = element_blank(),
        panel.border = element_blank())

ggsave("R/Barplots/Phylum_controls_18.svg")
last_plot()
plot(p)

##Normal barplots
# p <- plot_bar(phy_new, fill = "Phylum") + facet_grid(~Genotype, scales="free", space = "free") + theme_bw() + labs(y='Abundance (%)') + theme(axis.title.x=element_blank(),
#         axis.text.x=element_blank(),
#         axis.ticks.x=element_blank(),
#         panel.grid.major = element_blank(),
#         strip.text.x = element_blank(),
#         panel.border = element_blank())
        
# plot(p)

# png(file = paste("R/Barplots/", paste('phylum_WTctrl_18.png'), sep = ''), units="in", width=5, height=4, res=700)
pdf(file = paste("R/Barplots/", paste('KO_ctrl_18_Phylum.pdf'), sep = ''),width=8, height=4)
plot(p)
dev.off()
