# to find out how many E.coli genomes are incomplete

patric_file = '/home/hermuba/data/patric_original/PATRIC_genome_ecoli.csv'

genomes_included = '/home/hermuba/data0118/annotated_RIS/anno_df'
pangenome_included = '/home/hermuba/data0118/cdhit/clstr/pangenome_df/Escherichia0.70.clstr.csv'

quast_file = '/home/hermuba/data/genome/all_genome_stat.tsv'

# select the genome ID of ecoli

import pandas as pd

# use genome with resistant annotation only
df = pd.read_pickle(genomes_included)
genome_id = df.loc[df['Species'] == 'Escherichia']['Genome ID'].unique()

# use all genome from patric
#with open(pangenome_included) as f:
#    genome_id = f.readline().split(',')
#    genome_id.remove("")


# select the stats from patric file

patric = pd.read_csv(patric_file, header = 0, sep = ',', dtype = str)
patric = patric.set_index('Genome ID')
selected_patric = patric.loc[genome_id]

# join quast
with open(quast_file) as f:
    names = f.readline().split('\t')

quast = pd.read_csv(quast_file, skiprows = 1, sep=r"\s+", names = names)
quast = quast.set_index('Assembly')
selected_quast = quast.loc[genome_id]


# merge
merged = pd.merge(selected_quast, selected_patric, left_index = True, right_index = True)

# select genome that are WGS or Complete, remove plasmid
selected_genome_id = merged.loc[merged['Genome Status'] != 'Plasmid'].index


selected_genome_id.to_series().to_csv('/home/hermuba/data/genome_list/ecoli_rm_plasmid_1582', index = False, header = False)
