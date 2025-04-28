## Displaying the species in my plant collection on a phylogeny
## April 2025

library(U.PhyloMaker)
library(dplyr)
library(tidyr)
library(ggtree)

# Load the whole phylogeny
megatree <- read.tree("plant_20221117-main/plant_megatree.tre")
# load the lookup file indicating what family genera belong to
genus_list <- read.csv("plant_20221117-main/plant_genus_list.csv", sep=",")

## TODO automatically extract the species list from the Obsidian md file
species <- c("Capsicum annuum",
             "Punica granatum",
             "Cannabis sativa",
             "Tropaeolum majus",
             "Cycas revoluta",
             "Persea americana",
             "Clianthus maximus",
             "Crassula ovata",
             "Strelitzia reginae",
             "Ficus elastica",
             "Sphaeropteris medullaris",
             "Citrus sinensis",
             "Pyrrosia serpens",
             "Malva sylvestris",
             "Matricaria chamomilla",
             "Papaver somniferum",
             "Passiflora edulis")

result <- phylo.maker(species, megatree, genus_list, nodes.type = 1, scenario = 3)

plot(result$phylo)
