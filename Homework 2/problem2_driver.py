#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# importing sys library to get standard in functions
import sys
# importing io library to test for file type
import io

# import Node and SinglyLinkedList from problem2 file
from problem2 import Node
from problem2 import SinglyLinkedList


# In[ ]:


# if the standard in file is the right file type, print message and proceed
if type(sys.stdin) is io.TextIOWrapper:
    sys.stdout.write("File type is compatible. Proceeding:\n")
# else print fail message, exit
else:
    sys.stdout.write("File type is not compatible. Exiting")
    sys.exit()


# In[ ]:


# create variable for singlylinkedlist
res = SinglyLinkedList()
# tuples to check for commands
# commands with single argument and no required return
crt_dlt = ("append", "prepend", "delete", "delete_at")
# commands with 2 arguments
crt_upd = ("insert", "update")
# commands with single argument and return
red_one = ("get", "find")
# commands with no argument
red_zer = ("len", "print_list")
# combining commands into single tuple
keys = crt_dlt + crt_upd + red_one + red_zer
# looping through standard in by line
for line in sys.stdin:
    # splitting line into individual components and putting into alias
    cog = line.split()
    # if the line is empty or starts with # then it should be ignored
    if not cog or cog[0].startswith("#"):
        continue  
    # making the first component which should be command all lower case, avoid error from capital letters
    cog[0] = cog[0].lower()
 
    # if the line doesn't start with a keyword, return that the command couldn't be found
    if cog[0] not in keys:
        sys.stdout.write("Command not found. Proceeding:\n")
    # if there are more than 3 components, then it doesn't meet requirement
    elif len(cog) > 3:
        sys.stdout.write("Too many arguments. Proceeding:\n")
    # if there are 3 components and one of commands that require 2 arguments
    elif len(cog) == 3 and cog[0] in crt_upd:
        # and if the second two components are positive whole numbers
        if cog[1].isdigit() and cog[2].isdigit():
            # try running the line as python code
            cmd = f"res.{cog[0]}({cog[1]}, {cog[2]})"
            try:
                exec(cmd)
            # general exception but nested ifs ensure that it is a recognizable command and valid arguments
            except Exception:
                sys.stdout.write("Index out of range\n")
        # invalid arguments, presumable index
        else:
            sys.stdout.write("Incorrect argument given\n")
    # if there are 2 components and recognizable command with one arg
    elif len(cog) == 2 and cog[0] in crt_dlt:
        # if the second component is positive, whole number
        if cog[1].isdigit():
            # try code
            cmd = f"res.{cog[0]}({cog[1]})"
            try:
                exec(cmd)
            # exception if the code doesn't work
            except Exception:
                sys.stdout.write("Exception found\n")
        # invalid arg
        else:
            sys.stdout.write("Incorrect argument given\n")
    # two components and a read command
    elif len(cog) == 2 and cog[0] in red_one:
        # check second comp as pos, whole num
        if cog[0] == "get" and cog[1].isdigit():
            try:
                sys.stdout.write(f"get({cog[1]}) = {res.get(int(cog[1]))}\n") 
            # nested ifs, likely index
            except Exception:
                sys.stdout.write("Index out of range\n")
        elif cog[0] == "find" and cog[1].isdigit():
            try:
                sys.stdout.write(f"find({cog[1]}) = {res.find(int(cog[1]))}\n")
            # error, should be value not found
            except Exception:
                sys.stdout.write("Value not found\n")
        else:
            sys.stdout.write("Incorrect argument given\n")
    # single comp, command with no arguments
    elif len(cog) == 1 and cog[0] in red_zer:
        # if it is len, run len function for list
        if cog[0] == "len":
            sys.stdout.write(f"len = {res.__len__()}\n")
        # else it is print_list
        else:
            sys.stdout.write(f"{res.print_list()}\n")
    # else some how missed exceptions at top, finishes if statement
    else:
        sys.stdout.write("Command not recognized")

# loop finished, print final list
sys.stdout.write(f"Final list: {res.print_list()}")

