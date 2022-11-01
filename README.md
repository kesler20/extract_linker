## Linker Extraction

- the ``chars_to_remove`` folder contains all the txt files used to list all the strings to remove
- the ``scripts`` folder contains python scripts which can be used to aid the implementation of the algorithm in excel
- the ``utils.py`` file contains all the functions which are used for the algorithm
- the ``main.py`` file contains the main script to run
- the ``3ddigimofs_raw.tab.xlsx`` file contains the raw sample of roughly 10 thousand rows

#### Naming Convention

---
each step ``step_n`` variable contains a list of things that will be removed @ the step n
the last item in te list is the string which will be replacing all the other strings,

``step_n_m`` means that the list contain both the items which need to be removed at step m and n 
and that both the items at steps n and m can be replaced with the item ``step_n_m[-1]``

---

#### TODOs
- [ ] merge and seperate columns by using pandas (fill the unequal rows and columns with NaNs)
- [ ] seperate step_n_m lists into different steps to be applied individually ?
