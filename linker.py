import pandas as pd
from utils import *

'''
Naming Convention
---

each step "step_n" variable contains a list of things that will be removed @ the step n
the last item in te list is the string which will be replacing all the other strings
'''

path = "3ddigimofs_raw.tab.xlsx"
df = pd.read_excel(path)

sample_df = [name for name in df["[_chemical_name_systematic]"]]


step_1: 'list[str]' = [
    "catena-(", "catena-[", "catena(", "catena[", ""]
step_2 = [
    "$-", "$", "mu-", "mu!", "!", "i)", "%"]

step_3_4 = convert_file_content_into_list(r"chars_to_remove\step_3_4.txt")
step_3_4.append("%")

step_5 = convert_file_content_into_list(r"chars_to_remove\list_of_metals.txt")
step_5.append("%")

step_6 = [" ", "_"]
step_7a = [" %", "% ", ""]
step_7b = ["-(%", "%"]

steps = [step_1, step_2, step_3_4, step_5, step_6, step_7a, step_7b]

# apply steps from step 1 to 7 to sample_df
for step in steps:
    sample_df = [replace_with_string(
        name, step[:-1], step[-1]) for name in sample_df]

# remove all the %% until there are only %
sample_df_8a = replace_string_recursively(sample_df, r"%%", "%")

# replace all the -- with %
sample_df_8b = replace_string_recursively(sample_df_8a, "--", "%")


####################################### MODIFIED STEPS (9-14) #####################
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
list_of_solvents = convert_file_content_into_list(r"chars_to_remove\csd_solvent_list.txt")
sample_df_11b: 'list[str]' = [replace_with_string(
    name, list_of_solvents, "") for name in sample_df_11a]

# remove all the words containing solvate
sample_df_11c = remove_substring_from_string_list(sample_df_11b,"solvate","%")

######################################################### END OF MODIFIED STEPS #####

step_14 = [")-(", ") (", "  ", "%", "%", "%))", "%)",
           "%]", "(%", "-%", "%"]
sample_df_14: 'list[str]' = []
for name in sample_df_11c:
    sample_df_14.append(replace_with_string(name, step_14[:-1], step_14[-1]))

########## DUE TO THE EARLIER MODIFICATION THE FOLLOWING STEPS (15-18) WILL BE MODIFIED ###########
sample_df_15: 'list[str]' = []
for name in sample_df_14:
    name = name.replace(" -bis(", "-bis(")
    name = name.replace(" -carboxylat", "-carboxylat")
    sample_df_15.append(name)

# remove all the words containing unknown
sample_df_16 = remove_substring_from_string_list(sample_df_15,"unknown","%")


