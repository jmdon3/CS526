#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# importing sys library to get standard in functions
import sys
# importing io library to test for file type
import io

# import Node and SortedDoublyLinkedList from problem4 file
from problem4 import Node
from problem4 import SortedDoublyLinkedList


# In[ ]:


# if the file type is acceptable, print confirmation and continue
if type(sys.stdin) is io.TextIOWrapper:
    sys.stdout.write("File type is compatible. Proceeding:\n")
# else return error message and stop
else:
    sys.stdout.write("File type is not compatible. Exiting")
    sys.exit


# In[ ]:


# alias for list being made
res = SortedDoublyLinkedList()

# tuple for add, only single arg, no return
add_f = ("add", )
# tuple for single arguments with a return
sing_arg = ("delete", "exists", "count")
# tuple for functions with no argument
self_arg = ("print_list", "total", "sum_middle_three", "median")
# combining tuples for lookup to ignore lines that don't start with recognized function
keys = add_f + sing_arg + self_arg

# loop going through the standard in file by line
for line in sys.stdin:
    # split each line into components
    cog = line.split()

    # if the line is blank or is a comment, continue to next loop
    if not cog or cog[0].startswith("#"):
        continue

    # making the first component all lower case, avoid capital letters breaking the code
    cog[0] = cog[0].lower()

    # if first comp is not a key word, return message saying so
    if cog[0] not in keys:
        sys.stdout.write("Command not found. Proceeding:\n")
    # if there are more than 2 components, it doesn't fit the convention
    # print error message
    elif len(cog) > 2:
        sys.stdout.write("Too many arguments. Proceeding:\n")
    # if it starts with add and has 2 components
    elif cog[0] in add_f and len(cog) == 2:
        # first confirm that the second comp is a pos, whole number
        if cog[1].isdigit():
            # put string into code syntax
            cmd = f"res.{cog[0]}({cog[1]})"
            # try to run the code
            try:
                exec(cmd)
                sys.stdout.write(f"{line}")
            # if it doesn't work, print generic error
            except Exception:
                sys.stdout.write("Exception found\n")
        # 2nd comp isn't valid, incorrect argument given
        else:
            sys.stdout.write("Incorrect argument given\n")
    # if it has 2 comps and is a single argument command
    elif cog[0] in sing_arg and len(cog) == 2:
        # and if the second comp is a valid number
        if cog[1].isdigit():
            # if it is a count, need to include double underscore in syntax
            if cog[0] == "count":
                cmd = eval(f"res.__count__({int(cog[1])})")
            # else it is list name period function name (#)
            else:
                cmd = eval(f"res.{cog[0]}({int(cog[1])})")
            # now try to print message with function, number, and result
            try:
                sys.stdout.write(f"{cog[0]}.({cog[1]}) = {cmd}\n")
            # generic error
            except Exception:
                sys.stdout.write("Exeption found\n")
        # else the number isn't valid, index error
        else:
            sys.stdout.write("Index not found\n")
    # self argument func, only 1 component
    elif cog[0] in self_arg and len(cog) == 1:
        # coding syntax
        cmd = eval(f"res.{cog[0]}()")
        # try to print message with function and result
        try:
            sys.stdout.write(f"{cog[0]}.() = {cmd}\n")
        # standard error
        except Exception:
            sys.stdout.write("Exception found\n")
    # else something is wrong with command, print message
    else:
        sys.stdout.write("Command not valid")

# loop has finished, print final version of the list
sys.stdout.write(f"Final list: {res.print_list()}")

