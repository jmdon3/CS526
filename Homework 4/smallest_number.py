#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# import sys library for standard in, out
import sys

# import io library to check that file is valid
import io


# In[ ]:


# defining core function, takes file as an argument
def smallest_num(file):
    # list variable to store the contents
    contents =  []
    # for loop going through the file by line
    for line in file:
        # put the contents of the file into a list with elements from line split
        contents += line.split()

    # target will be the index 1 element in the list, storing in variable
    target = int(contents[1])
    # storing list of elements in separate list, index 2 to the end
    lst = contents[2:]
    # putting the list into a string for the program output
    lst_str = ", ".join(lst)
    # remove first 2 elements from list and convert rest into integers
    lst = [int(x) for x in contents[2:]]
    # putting the list in descending order, largest numbers will hit target fastest
    lst.sort(reverse = True)
    # ind to store the answer being found
    ind = 0
    # variable to check against the target
    run_tot = 0
    # while loop running until the running total exceeds the target
    while run_tot <= target:
        # adding to the running total using ind for index
        run_tot += int(lst[ind])
        # adding to ind to track answer
        ind += 1
    # format and return output, includes input, target, and answer
    return f"Input: {lst_str} Target: {target} Answer: {ind}"


# In[ ]:


# variable for standard in file
smol_num = sys.stdin

# if the file is the right file type, run function on file, put result into standard out
if type(smol_num) is io.TextIOWrapper:
    res = smallest_num(smol_num)
    sys.stdout.write(res)
# else print message to standard out and exit file
else:
    sys.stdout.write("File type is not compatible. Exiting\n")
    sys.exit

