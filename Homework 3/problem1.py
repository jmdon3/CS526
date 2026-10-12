#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# function evaluating string as a palindrome
def palindrome(string):
    # if it is 1 character, return True
    if len(string) == 1:
        return True
    # if it is 2 characters and the char match, return True
    elif len(string) == 2 and string[0] == string[1]:
        return True
    # if the first character and last character match ...
    elif string[0] == string[len(string) - 1]:
        # update the string removing the first and last characters
        string = string[1:len(string) - 1]
        # put the new string in the palindrome function
        return palindrome(string)
    # else it isn't a palindrome, return False
    else:
        return False


# In[ ]:


# function taking a file as input
def check_file(file):
    # set alias for empty string and integer set to 0
    res = ""
    pal_count = 0
    # loop to go through the file by line
    for line in file:
        # remove any trailing spaces and spaces in the middle
        line = line.strip().replace(" ", "")
        # put return of palindrome function for the line into string
        res += f"{palindrome(line)}\n"
        # if the palindrome function returns true, add to the palindrome counter
        if palindrome(line) == True:
            pal_count += 1
    # loop has finished, add palindrome counter to end of string
    res += str(pal_count)
    # return string
    return res


# In[ ]:


# importing sys library for standard in and out
import sys

# importing io for file type testing
import io


# In[ ]:


pal_file = sys.stdin

if type(pal_file) is io.TextIOWrapper:
    pal_res = check_file(pal_file)
    sys.stdout.write(pal_res)
else:
    sys.stdout.write("File type is not compatible. Exiting\n")
    sys.exit

