#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# function to get count of largest subsequence
# takes size of list a, list a, size of list b, and list b as arguments
def sequence(size_a, a, size_b, b):
    # create a list the size of list a for storing offsets
    suba = [1] * size_a
    # create a list the size of list b for storing offsets
    subb = [1] * size_b

    # for loop length of list b
    for j in range(size_b):
        # first inner loop looking at all characters from j on 
        for i in range(min(j, size_a)):
            # if iterated integer in a is smaller than the fixed one at b
            if a[i] < b[j]:
                # take the largest of the offsets
                subb[j] = max(subb[j], suba[i] + 1)

        # second, separate inner loop looking at the possible integers past the first
        for i in range(j + 1, size_a):
            # if the iterated integer is larger than the fixed one at b
            if b[j] < a[i]:
                # take the largest of the offsets
                suba[i] = max(suba[i], subb[j] + 1)

    # store in resolution b the max from the 2 offset lists
    resb = max(max(suba, default = 0), max(subb, default = 0))

    # resetting offset lists
    suba = [1] * size_a
    subb = [1] * size_b

    # second outer loop, iterating up to the size of list a
    for i in range(size_a):
        # first inner loop of the second set
        for j in range(min(i, size_b)):
            # if the iterated from b is smaller than the fixed from a
            if b[j] < a[i]:
                # update the offset list with the larger offset
                suba[i] = max(suba[i], subb[j] + 1)

        # second inner loop for second set
        for j in range(i + 1, size_b):
            # if iterated from b is larger than the fixed from a
            if a[i] < b[j]:
                # update the offset list with the larger offset
                subb[j] = max(subb[j], suba[i] + 1)

    # and update resolution a with the larger of the largest offsets from the 2 offset lists
    resa = max(max(suba, default = 0), max(subb, default = 0))

    # return the larger of the 2 resolutions
    return max(resa, resb)


# In[ ]:


# import sys library for standard in and out
import sys


# In[ ]:


# none variables for the list sizes
sz_one = None
sz_two = None

# empty lists for the lists
lst_one = []
lst_two = []

# variable for the file from standard in
file = sys.stdin

# for loop going through file by line
for line in file:
    # if size of list one isn't set
    if not sz_one:
        # set line as integer for variable
        sz_one = int(line)
    # same for size of list 2
    elif not sz_two:
        sz_two = int(line)
    # if list one is empty
    elif len(lst_one) == 0:
        # fill it
        lst_one = line.split()
    else:
        # else we're on the final line, this is list 2
        lst_two = line.split()

# for loops to update contents of both lists to integers for proper comparison
lst_one = [int(x) for x in lst_one]
lst_two = [int(x) for x in lst_two]

# call sequence variable within formatted response
sys.stdout.write(f"File Input: {sys.stdin.name}\nLongest sequence: {sequence(sz_one, lst_one, sz_two, lst_two)}")

