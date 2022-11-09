import pandas as pd
import os

raw_dataset = pd.read_excel("3ddigimofs_raw.tab.xlsx")
linkers = pd.read_csv("result.csv")
metals = pd.read_csv("metals.csv")
solvents = pd.read_csv("solvents.csv")
code = raw_dataset["[REFCODE]"]
original = raw_dataset["[_chemical_name_systematic]"]
schema = {"code": [], "linkers": [],  "metals": [],  "solvent": []}

rows_to_drop = []
for index, row in enumerate(linkers[linkers.columns[0]]):
    if str not in [type(linker) for linker in linkers.loc[index]]:
        rows_to_drop.append(index)

linkers.drop(rows_to_drop, axis=0, inplace=True)
print(linkers)

# for file in os.listdir(os.getcwd()):
#     if file.endswith(".csv") or file.endswith(".xlsx"):
#         os.system(f"echo start excel {file}")
