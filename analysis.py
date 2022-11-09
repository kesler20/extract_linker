import pandas as pd

df = pd.read_csv("result.csv")
print(df)

rows_to_drop = []
for index, row in enumerate(df[df.columns[0]]):
    if str not in [type(linker) for linker in df.loc[index]]:
        rows_to_drop.append(index)

df.drop(rows_to_drop, axis=0, inplace=True)
print(df)
