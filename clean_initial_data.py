from utils import *
import time
import pandas as pd
df = pd.read_excel("3D_MOF_subset.tab.xlsx")

clean_chemical_name_systematic = []

for name in df["[_chemical_name_systematic]"]:
    space_index = find_substring(name, " ")
    if space_index != -1:
        if space_index < len(name)/2:
            name = name.replace(" ", "", 1)

    clean_chemical_name_systematic.append(name)

data = pd.DataFrame(clean_chemical_name_systematic)
data.to_csv("clean_chemical_name_systematic.csv")
