import os
from numpy import nan
from utils import *
import pandas as pd
metals = convert_file_content_into_list(
    f"chars_to_remove/list_of_metals.txt")
df = pd.read_excel("3ddigimofs_raw.tab.xlsx")

df: list[str] = [row for row in df["[_chemical_name_systematic]"]]
results = []
max_len = 0
for name in df:
    # replace $ and numbers before them
    index_of_dollar_signs = find_symbol_in_string(name, "$")
    cnt = 0
    for index in index_of_dollar_signs:
        index += cnt
        name = name.replace(name[index - 1] + name[index], "", 1)
        cnt -= 2

    # remove solvents
    name = name.split(" ")[0]

    # replace all the metals
    name = replace_with_string(convert_chars_to_string(name), metals, "")

    # replace exclamation marks
    name = name.replace("!", "")

    # replace ato with ate
    name = name.replace("ato", "ate")

    # split the name by (m to separate linkers
    name = name.split("(m")

    # replace everything which does not start with the u- this will return a list of linkers
    name = [name.replace(
        "u-", "") for name in list(filter(lambda sub_string: sub_string.startswith("u"), name))]

    # initialise the final list of linkers
    linkers = []
    for linker in name:
        # remove the last dash in the name of the linker
        index_of_dash_1 = find_symbol_in_string(linker, ")-")
        if len(index_of_dash_1) == 0:
            linkers.append(linker)
        else:
            linkers.append(linker[:index_of_dash_1[-1]])
    
    # data processing
    results.append(linkers)
    if len(linkers) > max_len:
      max_len = len(linkers)
    
    if len(linkers) < max_len:
      for i in range(max_len - len(linkers)):
        linkers.append(None)
      
    if os.path.isfile("result.csv"):
        old_rows = pd.read_csv("result.csv")
        new_row = pd.DataFrame({ f'Linker {index}' : [linker] for index, linker in enumerate(linkers,1) })
        new_df = pd.concat([old_rows, new_row])
        new_df.to_csv("result.csv", index=False)
    else:
        new_df = pd.DataFrame({ f'Linker {index}' : [linker] for index, linker in enumerate(linkers,1) })
        new_df.to_csv("result.csv", index=False)


os.system("start excel result.csv")
