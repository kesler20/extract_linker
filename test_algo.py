from utils import *
import pandas as pd
import time
metals = convert_file_content_into_list(
    f"chars_to_remove/list_of_metals.txt")
df = pd.read_excel("3ddigimofs_raw.tab.xlsx")

df: list[str] = [row for row in df["[_chemical_name_systematic]"]]
data_set = int(input("Enter the number of data points to check?:"))
for name in df[:data_set]:
    print("=================================")
    print("\nstep 0", name)
    time.sleep(1)

    # replace $ and numbers before them
    index_of_dollar_signs = find_symbol_in_string(name, "$")
    cnt = 0
    for index in index_of_dollar_signs:
        index += cnt
        name = name.replace(name[index - 1] + name[index], "", 1)
        cnt -= 2
    print("\nstep 1 replace $ and numbers before them:\n", name)
    time.sleep(1)

    # remove solvents
    name = name.split(" ")[0]
    print("\nstep 2 remove solvents:\n", name)
    time.sleep(1)

    # replace all the metals
    name = replace_with_string(convert_chars_to_string(name), metals, "")
    print("\nstep 3 replace all the metals:\n", name)
    time.sleep(1)


    # replace exclamation marks
    name = name.replace("!", "")
    print("\nstep 4 replace exclamation marks:\n", name)
    time.sleep(1)


    # replace ato with ate
    name = name.replace("ato", "ate")
    print("\nstep 5 replace ato with ate:\n", name)
    time.sleep(1)

    # split the name by (m to separate linkers
    name = name.split("(m")
    print("\nstep 6 split the name by (m to separate linkers:\n", name)
    time.sleep(1)


    # replace everything which does not start with the u- this will return a list of linkers
    name = [name.replace(
        "u-", "") for name in list(filter(lambda sub_string: sub_string.startswith("u"), name))]
    print("\nstep 7 replace everything which does not start with the u- this will return a list of linkers\n", name)
    time.sleep(1)


    # initialise the final list of linkers
    linkers = []
    for linker in name:
        # remove the last dash in the name of the linker
        index_of_dash_1 = find_symbol_in_string(linker, ")-")
        if len(index_of_dash_1) == 0:
            linkers.append(linker)
        else:
            linkers.append(linker[:index_of_dash_1[-1]])

    print("Result:\n",linkers)
    time.sleep(1)


