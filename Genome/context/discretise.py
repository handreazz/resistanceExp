# input: pivot table
in_path = '/home/hermuba/data0118/mutual_info/'
table_name = 'blastp_out_max_evalue'

in_file = in_path + table_name + '_pivot'
quantile = in_path + table_name + '_quantile'
ordinary = in_path + table_name + '_ordinary'

import pandas as pd
from  multiprocessing import Pool


# fillna, discretise using two methods:
def discrete(df):
    df.fillna(0, inplace = True)
    c_table = pd.DataFrame(index = df.index, columns = df.columns)
    for index, rows in df.iterrows():
        c_table.loc[rows.name] = pd.cut(rows, 415, labels = False)
    return(c_table)


def discrete_equal_bulk(df):
    import numpy as np
    bin_path = '/home/hermuba/data0118/discretize/'
    if 'eskape' in table_name:
        npy = 'eskape_bins.npy'
    else:
        npy = 'refseq_bins.npy'

    npy = bin_path + npy

    precalculated_bin = np.load(npy)

    q_table = pd.DataFrame(index = df.index, columns = df.columns, labels = list(range(1, len(npy)+ 2)))

    for index, rows in df.iterrows():
        q_table.loc[rows.name] = pd.cut(rows, precalculated_bin)

    return(q_table.fillna(0))



def run_chunkwise(in_file, discrete_method):
    #chunks = pd.read_csv(in_file, header = 0, index_col = 0, nrows = 50)
    chunks = pd.read_csv(in_file, header = 0, index_col = 0, chunksize = 100, iterator = True)
    no_chunk = 0
    for chunk in chunks:
        c = discrete_method(chunk)

        outfile = in_path + table_name + str(discrete_method)
        if no_chunk == 0:

            #with open(quantile, 'w') as f:
                #q.to_csv(f, header = True)
            with open(outfile, 'w') as f:
                c.to_csv(f, header = True)
        else:
            #with open(quantile, 'a') as f:
                #q.to_csv(f, header = False)
            with open(outfile, 'a') as f:
                c.to_csv(f, header = False)
        no_chunk += 1

##### remember to rerun 'discrete'
