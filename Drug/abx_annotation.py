import pandas as pd
import numpy as np
clsi = pd.read_excel("/home/hermuba/res/data/anootated_RIS/CLSI_m100_breakpoint.xlsx")
category = clsi[['category', 'drug']]
category = category.drop_duplicates(subset = 'drug')
order = ['penicillins', 'b_lactam_inhibitor', 'cephems', 'monobactams', 'carbapenems', 'lipopeptides', 'phenicols', 'macrolides', 'aminoglycosides', 'tetracyclines', 'quinolones', 'folate_path','nitrofurans', 'fosfomycins', 'licosamide', 'pleuromutilin']

all_drug = ['ertapenem', 'cephalexin', 'clindamycin', 'polymyxin b', 'tilmicosin','tazobactam', 'imipenem', 'cefoperazone', 'sulbactam', 'doripenem','cefazolin', 'piperacillin', 'ceftazidime', 'timentin', 'trimethoprim','tigecycline', 'chloramphenicol', 'ceftriaxone', 'cefuroxime','amikacin', 'levofloxacin', 'sulfisoxazole', 'azithromycin','cefotaxime', 'danofloxacin', 'sulfamethoxazole', 'enrofloxacin','kanamycin', 'colistin', 'ticarcillin', 'doxycycline', 'gentamicin','cefotetan', 'fosfomycin', 'sulfadimethoxine', 'oxytetracycline','minocycline', 'cephalothin', 'ciprofloxacin', 'florfenicol','nalidixic acid', 'ceftiofur', 'clavulanic acid', 'tetracycline','tiamulin', 'neomycin', 'aztreonam', 'ampicillin', 'meropenem','tylosin', 'spectinomycin', 'nitrofurantoin', 'chlortetracycline','cefepime', 'streptomycin', 'cefoxitin', 'amoxicillin', 'tobramycin','norfloxacin', 'moxifloxacin']

# ADD MISSING:

missing = list(set(all_drug)-set(category['drug']))
cat = ['b_lactam_inhibitor', 'phenicols', 'folate_path', 'cephems', 'penicillins', 'quinolones', 'cephems', 'macrolides', 'macrolides', 'lipopeptides', 'aminoglycosides', 'penicillins', 'tetracyclines', 'aminoglycosides', 'tetracyclines', 'cephems', 'aminoglycosides', 'folate_path', 'b_lactam_inhibitor', 'tetracyclines', 'licosamide', 'quinolones', 'b_lactam_inhibitor', 'b_lactam_inhibitor', 'pleuromutilin', 'quinolones', 'folate_path']

df = pd.DataFrame({'drug' : missing, 'category' :cat})
category = category.append(df, ignore_index = True)
for i in order:
    category.loc[category['category'] == i,'order'] = order.index(i)