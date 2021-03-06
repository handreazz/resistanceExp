
import pandas as pd
import numpy as np
cluster_detail = pd.read_pickle("/home/hermuba/data/genePredicted/cdhit/cluster_detail_df")

#add cog_category
with open("/home/hermuba/data/cog/ecoli.cog.list") as f:
    for line in f:
        line = line.replace('\n', '')
        genome_id = line.split('\t')[0]
        protein_id = line.split('\t')[1]
        head = protein_id+'|'+genome_id
        if head in list(cluster_detail['representing gene header']):
            index = cluster_detail.loc[cluster_detail['representing gene header'] == head].index
            cluster_detail.loc[index, 'cog'] = line.split('\t')[2]

# add on card annotation (each member)
def card_in_cluster(cluster_name):
    print('doing card', cluster_name)
    count = 0
    repre = cluster_detail.loc[cluster_name, 'representing gene header']
    rep_id = repre.split('|')[1]
    rep_protein = repre.split('|')[0]
    df = pd.read_pickle("/home/hermuba/data/genePredicted/card_detail_df/"+rep_id)

    if rep_protein in df.index:

       rep_best = df.loc[rep_protein, 'best_ARO']
       rep_aro = df.loc[rep_protein, 'ARO']
       rep_aro_id = df.loc[rep_protein, 'ARO_name']
    else:
        rep_aro = np.nan
        rep_aro_id = np.nan
        rep_best = np.nan
    members = cluster_detail.loc[cluster_name, 'member'].split(',')[1:] # the first element is ''
    for mem in members:
        genome_id = mem.split('|')[1]
        protein_id = mem.split('|')[0]

        df = pd.read_pickle("/home/hermuba/data/genePredicted/card_detail_df/"+genome_id)
        aro = []
        identity = []
        if protein_id in df.index:
            count = count + 1
            aro.append(df.loc[protein_id, 'ARO'])
            identity.append(df.loc[protein_id, 'ARO_name'])
        return(count, count/len(members), set(aro), set(identity), rep_aro, rep_aro_id, rep_best)

for clu in cluster_detail.index:
    count, portion, aro, identity, rep_aro, rep_aro_id, rep_best = card_in_cluster(clu)

    cluster_detail.loc[clu, "card_portion"] = portion
    cluster_detail.loc[clu, "card_count"] = count
    cluster_detail.loc[clu, "aro_member"] = str(aro)
    cluster_detail.loc[clu, "aro_member_identity"] =str(identity)
    cluster_detail.loc[clu, "representing_aro"] = rep_aro
    cluster_detail.loc[clu, "representing_aro_identity"] = rep_aro_id
    cluster_detail.loc[clu, "best_aro_identity"] = rep_best
# add card ARO for representing gene

# add "prevalance" to cluster_detail
df = pd.read_pickle("/home/hermuba/data/genePredicted/cdhit/ec0102_df")
prevalance = df.mean(axis = 0)
cluster_detail['prevalance'] = prevalance
# cluster_detail['prevalance'] = df.mean() # __% genome has that gene
cluster_detail.to_pickle("/home/hermuba/data/genePredicted/cdhit/cluster_detail_df")
cluster_detail.to_excle("/home/hermuba/data/genePredicted/cdhit/cluster_detail.xlsx")
