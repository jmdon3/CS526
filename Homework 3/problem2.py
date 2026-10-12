#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# import sys library for standard in, out
import sys

# import io library to check file type
import io


# In[ ]:


# if the standard in file is text based, proceed
if type(sys.stdin) is io.TextIOWrapper:
    pass
# else put message saying it isn't compatible to standard out and exit
else:
    sys.stdout.write("File type is not compatible. Exiting\n")
    sys.exit


# In[ ]:


# creating substrings function
# takes a string as argument and can also store a beginning integer, ending integer
# and a substring list for storing
def substrings(s, begin = 0, end = 1, sbstr_lst = None):
    # if the substring list doesn't have a type, make it a list
    if sbstr_lst is None:
        sbstr_lst = []

    # if the beginning indicator matches the length of the string ...
    if begin == len(s):
        # if that length is 0, return string is empty message
        if len(s) == 0:
            return "String is empty"
        # else go through wrap up
        else:
            # making the substring list a set to confirm uniquness then switching back to a list
            sbstr_lst = list(set(sbstr_lst))
            # then set a loop the number of substrings in the list
            for i in range(len(sbstr_lst)):
                # sub-loop that takes each substring and checks if it is placed in alphabetical order
                for c in range(0, len(sbstr_lst) - i - 1):
                    # if the current substring should come after the next, switch places
                    if sbstr_lst[c] > sbstr_lst[c + 1]:
                        sbstr_lst[c], sbstr_lst[c + 1] = sbstr_lst[c + 1], sbstr_lst[c]
            # after alphabetizing, append the number of substrings to the end of the list
            sbstr_lst.append(str(len(sbstr_lst)))
            # and return the completed list
            return sbstr_lst

    # if the ending indicator has reached the end of the string, return the function as a recursive
    # updating the beginning character to the next one and ending character to the one after
    if end > len(s):
        return substrings(s, begin + 1, begin + 2, sbstr_lst)

    # if none of these ifs fit, then append a substring using the stored indices
    sbstr_lst.append(s[begin:end])

    # and return the recursive just iterating the ending indicator
    return substrings(s, begin, end + 1, sbstr_lst)


# In[ ]:


# setting up function to work with a standard in file
# for loop going line by line, 
for line in sys.stdin:
    # assigning to a different alias
    string = line
    # removing all spaces with strip and replace functions
    string = string.strip().replace(" ", "")

# putting the substrings function's return into a resolution alias
res = substrings(string)

# for loop to print the results as required, goes through list by index
for t in range(0, len(res)):
    # individually print the substrings on their own line to standard out
    sys.stdout.write(f"{res[t]}\n")

