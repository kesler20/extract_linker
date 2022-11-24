import pandas as pd
import os

raw_dataset = pd.read_excel("3D_MOF_subset.tab.xlsx")
linkers = pd.read_csv("result.csv")
metals = pd.read_csv("metals.csv")
solvents = pd.read_csv("solvents.csv")
code = raw_dataset["[REFCODE]"]
original = raw_dataset["[_chemical_name_systematic]"]
schema = {"code": [], "linkers": [],  "metals": [],  "solvent": []}

linkers["raw linkers"] = original
linkers["code"] = code
linkers["metals"] = metals
linkers["solvents"] = solvents

linkers.to_csv("final_result.csv", index=False)

# rows_to_drop = []
# for index, row in enumerate(linkers[linkers.columns[0]]):
#     if str not in [type(linker) for linker in linkers.loc[index]]:
#         rows_to_drop.append(index)

# linkers.drop(rows_to_drop, axis=0, inplace=True)
# print(linkers)
