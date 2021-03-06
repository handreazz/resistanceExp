# to find inside the structures.sdf downloaded from drugbank those we want

import pybel
drugbank_data = '../../data/structures.sdf'
with open('../../data/druglist') as f:
    druglist = f.readlines()
# count search item
count = [0]*len(druglist)

# search through the whole document
for molecule in pybel.readfile("sdf",drugbank_data):
    data = molecule.data

    search_term = []
    name = data['GENERIC_NAME'].lower()
    search_term.append(name)
    if data.has_key('JCHEM_TRADITIONAL_IUPAC'):
        iupac = data['JCHEM_TRADITIONAL_IUPAC']
        search_term.append(iupac)
    if data.has_key('SYNONYMS'):
        other_name = data['SYNONYMS'].lower().split('; ')
        search_term = search_term + other_name


    for s in druglist:
        new = s.replace('\n', '').lower()
        #print(s)
        if new in search_term:
            molecule.write("sdf", '../../data/drug/'+s+'.sdf')

            print(s, search_term)
            count[druglist.index(s)] += 1
