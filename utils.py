import pandas as pd


def find_substring(string: str, sub_string: str):
    '''
    Uses the string.index() built in method, however
    if the sub-string is not found it returns -1 rather than rasing a ValueError

    ---
    Params:
    - string : the initial string which should contain the substring
    - sub_string : the string that we our looking for in the string

    ---
    Returns: 
    - index: an integer which is -1 if no substring was found'''
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


def convert_file_content_into_list(filename: str):
    '''
    Reads the specified filename and it returns a list containing each lines of the file
    and it removes "\ n" within each line

    ---
    Params:
    - filename: the path of the file containing the items of the list

    ---
    Returns:
    - final _list : a list of strings containing each line of the file'''
    final_list = []
    with open(filename, "r") as f:
        for string in f.readlines():
            final_list.append(string.replace("\n", ""))
    return final_list


def pp(array: list):
    '''
    Save list to excel on file called "cc.xlsx" 

    ---
    Params:
    - array : a list which can be passed to a pandas data frame
    '''
    df = pd.DataFrame(array)
    df.to_excel("cc.xlsx", index=False)


def replace_string_recursively(raw_sample_list: 'list[str]', string_replaced: str, string_replacing: str):
    '''
    Replace a sub-string from a raw sample list of strings iteratively until 
    all the instances of the sub-string in each string within the list are removed
    ```python
    raw_sample_list = ["string1-1-1","string2","string3-1-1"] 
    print(replace_string_recursively(raw_sample_list, "1-1", ""))
    ```
    will return ["string-1","string2","string3-"]

    ---
    Params:
    - raw_sample_list : a list of strings containing sub-strings which will be replaced iteratively
    - string_to_replace : a string which will be replaced iteratively
    - string_replacing : a string which will be used to replace the string_to_replace variable

    ---
    Returns:
    - clean_sample_list : a list of strings without any instance of the sub-strings replaced  
    '''
    clean_sample_list: 'list[str]' = []
    for name in raw_sample_list:
        clean_name = ""
        while find_substring(name, string_replaced) != -1:
            clean_name = name.replace(string_replaced, string_replacing)
            name = clean_name
        clean_sample_list.append(name)

    return clean_sample_list


def remove_substring_from_string_list(raw_sample_list: 'list[str]', sub_string_to_remove: str, separator: str):
    '''
    Removes all the instances of a sub-strings from a list of strings.

    ---
    Params:
    - raw_sample_list: a list of strings
    - sub_string_to_remove: a sub-string which will be searched over all the strings within the raw_sample_list
    - separator : a string which indicates when a string within the raw_sample_list should be split

    ---
    Returns:
    - clean_sample_list : a copy of the raw_sample_list which do not contain any instance of the sub-string specified

    '''
    clean_sample_list: 'list[str]' = []
    for name in raw_sample_list:
        clean_name = ""
        raw_name_list = name.split(separator)
        for char in raw_name_list:
            if find_substring(char, sub_string_to_remove) != -1:
                pass
            else:
                clean_name += char
        clean_sample_list.append(clean_name)

    return clean_sample_list


def find_symbol_in_string(name: str, symbol: str) -> list[int]:
    # list of integers containing the indexes of the dollar signs in the string
    dollar_signs_indexes: list[int] = []
    for i in range(name.count(symbol)):
        dollar_signs_indexes.append(name.find(symbol) + i)
        name = name.replace(symbol, "", 1)
    return dollar_signs_indexes


def convert_chars_to_string(chars: 'list[str]'):
    '''
    Take a list of characters and converts appends them to an empty string
    ---
    Params:
    - chars : list of characters i.e. ["c","a", "r"]
    ---
    Returns:
    - string: a string i.e. "car" 
    '''
    new_string = ''
    for char in chars:
        new_string += char
    return new_string

def convert_chars_to_string_recursive(chars: 'list[str]'):
    '''
    Take a list of characters and converts appends them to an empty string
    ---
    Params:
    - chars : list of characters i.e. ["c","a", "r"]
    ---
    Returns:
    - string: a string i.e. "car" 
    '''
    new_string = ''
    while type(chars) != str:
        for char in chars:
            new_string += char
        result = convert_chars_to_string_recursive(chars)
        chars = result


def split_without_removing_symbol(string: str, symbol: str):
    string = string.replace(symbol, f"%%{symbol}")
    list_str = string.split(f"%{symbol}")
    return [name.replace("%",symbol) for name in list_str]