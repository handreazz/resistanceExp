# download all 307 E.coli from genebank for panX analysis
import pandas as pd
pan_X_acc = pd.read_csv("/home/hermuba/data/metainfo.tsv", sep = '\t')

from Bio import Entrez
Entrez.email = "b101102109@tmu.edu.tw"     # Always tell NCBI who you are

download_path = "/home/hermuba/bin/pan-genome-analysis/data/ec_all/"
# search with accession number
def get_gi(accession):
    handle = Entrez.esearch(term=accession, db = 'nucleotide')
    record = Entrez.read(handle)
    handle.close()
    genome_id = record['IdList'][0]
    d_handle = Entrez.efetch(db="nucleotide", id=genome_id, rettype="gbwithparts", retmode="text")
    gb = d_handle.read()
    d_handle.close()

    filename = open(download_path+accession+'.gbk', 'w')
    filename.write(gb)
    filename.close()

# filelist
from os import listdir
from os.path import isfile, join
onlyfiles = [f for f in listdir(download_path) if isfile(join(download_path, f))]
done = [f.replace('.gbk', '') for f in onlyfiles]
for acc in pan_X_acc['accession']:
    if acc not in done:
        get_gi(acc)
