## Displaying the species in my plant collection on a phylogeny
## April 2025

library(U.PhyloMaker)
library(dplyr)
library(tidyr)
library(ggtree)
library(readMDTable)

## Load the whole phylogeny
megatree <- read.tree("plant_20221117-main/plant_megatree.tre")
## load the lookup file indicating what family genera belong to
genus_list <- read.csv("plant_20221117-main/plant_genus_list.csv", sep=",")

## Extract the species list from the Obsidian md file
collection <- read_md_table("~/projects/obsidian/Botany/Species in collection.md")

result <- collection |>
  select("Latin name") |>
  phylo.maker(megatree, genus_list, nodes.type = 1, scenario = 3)

ggtree(result$phylo) +
  geom_tiplab() +
  xlim(0, 500)
