library(phyloseq)
library(tidyverse)
library(qiime2R)

setwd('/Users/sophiecurio/16s/Sophie/core-metrics-results')

metadata<-read_tsv("metadata_phyloseq2.tsv")
shannon<-read_qza("shannon_vector.qza")
shannon$uuid
head(shannon$data)

png(file = paste("/Users/sophiecurio/Dropbox/APC_project/16s/Sophie/R/", paste('shannon_overtime2.png'), sep = ''), units="in", width=10, height=18, res=300)
shannon$data %>%
  as.data.frame() %>%
  rownames_to_column("#SampleID") %>%
  left_join(metadata) %>%
  mutate(Timepoint=as.numeric(Timepoint)) %>% #coerce this to be stored as number
  ggplot(aes(x=Timepoint, y=shannon, group=Mouse_ID, color=Genotype)) +
  geom_point(size=4) +
  geom_line() +
  facet_grid(Mouse_ID~Genotype) + #plot body sites across rows and subjects across columns
  theme_bw() +
  xlab("Time (weeks)") +
  ylab("Shannon Diversity") +
  ggtitle("Shannon diversity across time")

dev.off()


df <- (shannon$data %>%
  as.data.frame() %>%
  rownames_to_column("#SampleID") %>%
  left_join(metadata) %>%
  mutate(Timepoint=as.numeric(Timepoint)))

write.csv(df, '/Users/sophiecurio/Dropbox/APC_project/16s/Sophie/R//shannon_over_time.csv')