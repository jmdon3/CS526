#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# import sys library for standard in and out
import sys

# import node class from file minHeap
from minHeap import Node
# import heap class from file minHeap
from minHeap import Heap


# In[ ]:


# put file from standard in into variable
file = sys.stdin
# empty list to put values from file
nput = []

# for loop to read lines from standard in
for line in file:
    # strip extraneous spaces
    line = line.strip()
    # slice everything but first and last characters, should be [ and ]
    line = line[1:-1]
    # if the remaining line is empty
    if len(line) == 0:
        # continue to next line
        continue
    # split line into elements with comma and space as a separator, extend list with these elements
    nput.extend(line.split(", "))

# creating a heap
a = Heap()

# print list of inputs from file to standard out
sys.stdout.write(f"Input values: {nput}\n")

if len(nput) == 0:
    pass
else:
    # for loop going through contents of list
    for i in nput:
        # convert element to integer
        i = int(i)
        # write message that integer is being inserted
        sys.stdout.write(f"\nafter insert({i}):\n")
        # insert
        a.insert(i)
        # write printed heap
        sys.stdout.write(f"{a.print_heap()}")

