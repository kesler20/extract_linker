import pandas as pd

def find_substring(string: str, sub_string: str):
    '''uses the string.index() built in method, however
    if the sub-string is not found it returns -1 rather than rasing a ValueError
    
    ---
    Params:
    - string : the initial string which should contain the substring
    - sub_string : the s'''
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

def pp(value):
    df = pd.DataFrame(value)
    df.to_excel("cc.xlsx", index=False)

def convert_file_content_into_list(filename: str):
    '''reads the specified filename and it returns a list containing each lines of the file
    and it removes "\ n" within each line'''
    final_list = []
    with open(filename, "r") as f:
        for string in f.readlines():
            final_list.append(string.replace("\n", ""))
    return final_list