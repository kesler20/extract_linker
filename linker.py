import pandas as pd
from utils import *

path = "3ddigimofs_raw.tab.xlsx"
df = pd.read_excel(path)

sample_df = [name for name in df["[_chemical_name_systematic]"]]

# each step "step_n" contains a list of things that will be removed
# the last item in te list is the string which will be replacing all the other strings
#
step_1: 'list[str]' = [
    "catena-(", "catena-[", "catena(", "catena[", ""]

step_2 = [
    "$-", "$", "mu-", "mu!", "!", "i)", "%"]

step_3_4 = convert_file_content_into_list("step_3_4.txt")
step_3_4.append("%")

step_5 = convert_file_content_into_list("list_of_metals.txt")
step_5.append("%")

step_6 = [" ", "_"]
step_7 = [" %", "% ", ""]
step_8 = ["-(%", "%"]

steps = [step_1, step_2, step_3_4, step_5, step_6, step_7, step_8]

# apply from step 1 to 8 to sample_df
for step in steps:
    sample_df = [replace_with_string(
        name, step[:-1], step[-1]) for name in sample_df]


# remove all the %% until there are only %
sample_df_8a: 'list[str]' = []
for name in sample_df:
    clean_name = ""
    while find_substring(name, r"%%") != -1:
        clean_name = name.replace(r"%%", "%")
        name = clean_name
    sample_df_8a.append(name)

# replace all the -- with %
sample_df_8b: 'list[str]' = []
for name in sample_df_8a:
    clean_name = ""
    while find_substring(name, "--") != -1:
        clean_name = name.replace("--", "%")
        name = clean_name
    sample_df_8b.append(name)

# removing leading % in each name
sample_df_11a = []
for name in sample_df_8b:
    if name[0] == "%":
        clean_name = ""
        for char in list(name)[1:]:
            clean_name += char
        name = clean_name
    sample_df_11a.append(name)

# remove all the solvents
list_of_solvents = convert_file_content_into_list("csd_solvent_list.txt")
sample_df_11b: 'list[str]' = []
for name in sample_df_11a:
    sample_df_11b.append(replace_with_string(name, list_of_solvents, ""))

# remove all the words containing solvate
sample_df_11c = []
for name in sample_df_11b:
    clean_name = ""
    raw_name_list = name.split("%")
    for char in raw_name_list:
        if find_substring(char, "solvate") != -1:
            pass
        else:
            clean_name += char
    sample_df_11c.append(clean_name)

step_14 = [")-(", ") (", "  ", "%", "%", "%))", "%)",
        "%]", "(%", "-%", "%"]
sample_df_14: 'list[str]' = []
for name in sample_df_11c:
    sample_df_14.append(replace_with_string(name, step_14[:-1], step_14[-1]))

sample_df_15: 'list[str]'  = []
for name in sample_df_14:
    name = name.replace(" -bis(", "-bis(")
    name = name.replace(" -carboxylat", "-carboxylat")
    sample_df_15.append(name)

# remove all the words containing unknown
sample_df_16 = []
for name in sample_df_15:
    clean_name = ""
    raw_name_list = name.split("%")
    for char in raw_name_list:
        if find_substring(char, "unknown") != -1:
            pass
        else:
            clean_name += char
    sample_df_16.append(clean_name)
    

pp(sample_df)