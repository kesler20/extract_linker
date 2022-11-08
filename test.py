from utils import *
import pandas as pd

df = pd.DataFrame()
name = "catena-[(mu!2$-1,2-bis(pyridin-4-yl)ethene)-(mu!2$-5-hydroxyisophthalato)-zinc(ii) 1,2-bis(pyridin-4-yl)ethene solvate]"
metals = convert_file_content_into_list(f"chars_to_remove/list_of_metals.txt")
# solvents = convert_file_content_into_list(
#     f"chars_to_remove/csd_solvent_list.txt")
index_of_dollar_signs = find_symbol_in_string(name, "$")

# replace $ and numbers before them
cnt = 0
for index in index_of_dollar_signs:
    index += cnt
    print(name[index - 1] + name[index])
    name = name.replace(name[index - 1] + name[index], "", 1)
    cnt -= 2

# remove solvents
name = name.split(" ")[0]
# replace all the metals
name = replace_with_string(convert_chars_to_string(name), metals, "")
# replace question marks
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
    linkers.append(linker[:index_of_dash_1[-1]])

print(linkers)


data = { "code" : [], "linkers" : [],  "metals" : [],  "solvent": [] }