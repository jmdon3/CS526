#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#importing sys library to get standard in name, exit, standard in, standard out write
import sys
#importing io library to test for file type
import io

#if statement to determine if the standard in file can be written using the below code
if type(sys.stdin) is io.TextIOWrapper:
    #True result: print message saying it will work and the code is continuing
    sys.stdout.write("File type is compatible. Proceeding:\n")
else:
    #False result: print message that it won't work and then exit the code
    sys.stdout.write("File type is not compatible. Exiting:")
    sys.exit()

#for loop taking a text file from standard in and then printing each line from it to standard out
for line in sys.stdin:
    sys.stdout.write(line)

