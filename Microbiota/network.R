library(phyloseq)
library(ggplot2)
library(reshape)
library(qiime2R)
library(vegan)

setwd('/Users/sophiecurio/16s/Sophie/')

phy<-qza_to_phyloseq("table.qza", "rooted-tree.qza", "taxonomy.qza","metadata_phyloseq.tsv")
phy


# only keep samples with > 2500 feature IDs
phy = prune_samples(sample_sums(phy) > 2500, phy)

#network
ig <- make_network(phy, max.dist=0.5, dist.fun="bray")

png(file = paste("R/", paste('network.png'), sep = ''), units="in", width=7, height=5, res=300)
plot_network(ig, phy, color="Genotype", shape="Timepoint", line_weight=0.4, label="Mouse_ID")
dev.off()

#heatmap (doesn't currently work)
# plot_dist_as_heatmap <- function(dist, title = NULL) {
#   data <- melt(as(dist, "matrix"))
#   colnames(data) <- c("x", "y", "distance")
#   if (!is.null(order)) {
#     data$x <- factor(data$x, levels = order)
#     data$y <- factor(data$y, levels = order)
#   }
#   p <- ggplot(data, aes(x = x, y = y, fill = distance)) + geom_tile() 
#   p <- p + theme(axis.title.x = element_blank(), 
#                  axis.title.y = element_blank(), 
#                  axis.text.x = element_blank(), 
#                  axis.text.y = element_blank()
#   )
#   p <- p + scale_fill_continuous(limits = c(0, 1))
#   if (!is.null(title)) {
#     p <- p + ggtitle(title)
#   }
#   return(p)
# }
# 
# dist.bc <- distance(phy, method = "bray")
# p <- plot_dist_as_heatmap(dist.bc, title = "Bray-Curtis")
# plot(p)