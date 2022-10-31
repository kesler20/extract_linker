import pandas as pd


path = "3ddigimofs_raw.tab.xlsx"

# this is the algorithm https://chemrxiv.org/engage/api-gateway/chemrxiv/assets/orp/resource/item/630b6fe7d858fb84335f93f5/original/a-database-to-compare-possible-mo-fs-for-volumetric-hydrogen-storage-taking-into-account-the-cost-of-their-building-blocks-supporting-information.pdf

df = pd.read_excel(path)

sample_df = [name for name in df["[_chemical_name_systematic]"][:15]]
print(sample_df)


def find_substring(string: str, sub_string: str):
    try:
        return string.index(sub_string)
    except ValueError as err:
        return -1


def replace_with_string(raw_string: str, list_of_strings_to_replace: 'list[str ]', strings_to_replace_with: str):
    '''
    Replaces a list of unwanted string with a string

    ---
    Params:
    - raw_string : initial string to modify
    - list_of_strings_to_replace : an array containing all the strings that need to be replaced
    - strings_to_replace_with : a string which will replace all the strings in the list_of_strings_to_replace array

    ---
    Returns:
    - clean_string : the initial string with the replaced strings
    '''
    clean_string = ""
    for string in list_of_strings_to_replace:
        clean_string = raw_string.replace(string, strings_to_replace_with)
        raw_string = clean_string
    return clean_string


list_of_strings_to_remove: 'list[str]' = [
    "catena-(", "catena-[", "catena(", "catena[", ""]
symbols_to_replace_with_column_separator = [
    "$-", "$", "mu-", "mu!", "!", "i)", "%"]

other_things_to_remove = []
with open("step_3_4.txt", "r") as f:
    for string in f.readlines():
        other_things_to_remove.append(string.replace("\n", ""))
other_things_to_remove.append("%")

metals = []
with open("list_of_metals.txt", "r") as f:
    for metal in f.readlines():
        metals.append(metal.replace("\n", ""))

metals.append("%")

blank_spaces = [" ", "_"]

spaces_before_after_prcnt = [" %", "% ", ""]
other_prcnt_thing_to_replace = ["-(%", "%"]

to_remove = [list_of_strings_to_remove, symbols_to_replace_with_column_separator,
             other_things_to_remove, metals, blank_spaces, spaces_before_after_prcnt, other_prcnt_thing_to_replace]


for thing in to_remove:
    sample_df = [replace_with_string(
        name, thing[:-1], thing[-1]) for name in sample_df]

new_sample_df: 'list[str]' = []
for name in sample_df:
    clean_name = ""
    while find_substring(name, r"%%") != -1:
        clean_name = name.replace(r"%%", "%")
        name = clean_name
    new_sample_df.append(name)

print(new_sample_df)


new_new_sample_df = []
for name in new_sample_df:
    clean_name = ""
    while find_substring(name, "--") != -1:
        clean_name = name.replace("--", "%")
        name = clean_name
    new_new_sample_df.append(name)
    
print(new_new_sample_df)



