# a script to run CARD(comprehensive antibiotic resistance database) annotation

# path
gene_path = "/home/hermuba/resistanceExp/genePredicted"
txt_path = "/home/hermuba/resistanceExp/genePredicted/resGeneTxt"
json_path = "/home/hermuba/resistanceExp/genePredicted/resGeneJson"
# import
from package import rgi
import os
# to run card
def run(ID):
    print("running CARD annotation for "+ID)
    os.chdir(gene_path)
    os.system("rgi -t 'protein' -i "+ ID +".faa -o " + ID)
    os.system("mv "+ ID+".txt "+ txt_path)
    os.system("mv "+ ID+".json "+ json_path)

# update
def update(ID):
    onlyfiles = [f for f in os.listdir(txt_path) if os.path.isfile(os.path.join(txt_path, f))]
    if ID+'.txt' in onlyfiles:
        print("we already have CARD for ", ID)
    else:
        run(ID)



    
    
