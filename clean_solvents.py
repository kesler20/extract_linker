import pandas as pd
from utils import *

df = pd.read_excel("3ddigimofs.tab.xlsx")
df_sample = []
solvents = convert_file_content_into_list("csd_solvent_list.txt")
for solvent in solvents:
    for name in df["[_chemical_name_systematic]"]:
        name = name.replace(solvent, "")
        df_sample.append(name)

df = pd.DataFrame(df_sample)
df.to_excel("cleaned_3ddigimofs.tab.xlsx")
