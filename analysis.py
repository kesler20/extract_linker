import pandas as pd

linkers = pd.read_csv("result.csv")
metals = pd.read_csv("metals.csv")
solvents = pd.read_csv("solvents.csv")
code = pd.read_csv("3ddigimofs_raw.tab.xlsx")["[REFCODE]"]
print(linkers)

schema = {"code": [], "linkers": [],  "metals": [],  "solvent": []}
print(pd.merge(code, linkers, metals, solvents).to_csv("merged_result.csv"))

rows_to_drop = []
for index, row in enumerate(linkers[linkers.columns[0]]):
    if str not in [type(linker) for linker in linkers.loc[index]]:
        rows_to_drop.append(index)

linkers.drop(rows_to_drop, axis=0, inplace=True)
print(linkers)
