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

nput = [int(x) for x in nput]

# creating a heap
a = Heap()

# run runningmedian function on line and store in variable
res = a.running_median(nput)

# convert resulting list to string and return to standard out
sys.stdout.write(str(res))

