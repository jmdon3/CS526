#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# import sys library for standard in, out
import sys

# import copy library to keep previous, current day separate
import copy


# In[ ]:


# defining function
def spread(state):
    # set list of previous day state
    prev_day = state
    # make a copy of previous day for current to store changes
    cur = copy.deepcopy(prev_day)
    # loop going through x coordinates
    for x in range(0, len(prev_day)):
        # inner loop for y coordinates
        for y in range(0, len(prev_day)):
            # list to store infected neighbors
            neigh = []
            # if the current county is infected, continue to next county
            if prev_day[x][y] == "X":
                continue
            # if there is an north neighbor and it is infected, add to neighbors list
            if x - 1 >= 0 and prev_day[x - 1][y] == "X":
                neigh += [prev_day[x - 1][y]]
            # if there is a east neighbor and it is infected, add to neighbor list
            if y + 1 < len(prev_day) and prev_day[x][y + 1] == "X":
                neigh += [prev_day[x][y + 1]]
            # if there is an south neighbor and it is infected, add to neighbor list
            if x + 1 < len(prev_day) and prev_day[x + 1][y] == "X":
                neigh += [prev_day[x + 1][y]]
            # if there west neighbor and it is infected, add to neighbor list
            if y - 1 >= 0 and prev_day[x][y - 1] == "X":
                neigh += [prev_day[x][y - 1]]
            # checked all neighbors, if there are at least 2
            if neigh.count("X") > 1:
                # make current county infected
                cur[x][y] = "X"

    # if there aren't any uninfected counties
    if all(" " not in a for a in cur):
        # return all infected message
        return "There are no healthy counties left"
    # if the previous and current day lists match, no new infected counties
    elif prev_day == cur:
        # return infection contained message
        return "There are healthy counties left"
    # or else return recursive function
    else:
        return spread(cur)


# In[ ]:


# put file from standard in into variable
file = sys.stdin

# empty list for input
nput = []
# for loop to get contents of file
for line in file:
    # split into separate elements and put into input list
    nput += line.split()

# convert contents of file into integers
nput = [int(x) for x in nput[0:]]
# create matrix of counties based on square size from input
counties = [[" "] * nput[0]] * nput[0]

# integer of 1 for loop to go through initially infected counties
i = 1
# loop to mark infected counties
while i in range(1, len(nput) - 1):
    # take 2 integers at a time and index county, update county as infected
    counties[nput[i]][nput[i + 1]] = "X"
    # increase iterative by 2 to account for coordinate pairs
    i += 2

# run spread function on counties, write result to standard out
sys.stdout.write(spread(counties))

