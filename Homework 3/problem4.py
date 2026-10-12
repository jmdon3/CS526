#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# importing sys for standard in, out capabilities
import sys

# importing io for file type testing
import io


# In[ ]:


# if statement ensuring that the file type is compatible, only gives message if the file is not compatible
if type(sys.stdin) is io.TextIOWrapper:
    pass
else:
    sys.stdout.write("File type is not compatible. Exiting\n")
    sys.exit


# In[ ]:


# creating aliases for list of slope and axis intercepts of beams, number of ghosts/ghostbusters
slopelist = []
axis_int = []
ghost_count = None

# for loop going through each line of standard in file
for line in sys.stdin:
    # split contents of line and put in alias
    showdown = line.split()
    # set alias for individual pair's line slope
    slope = None
    # if there is more than one item in a line, set what should be buster and ghost coordinates as integers 
    if len(showdown) > 1:
        showdown[1] = int(showdown[1])
        showdown[2] = int(showdown[2])
        showdown[4] = int(showdown[4])
        showdown[5] = int(showdown[5])
    # if there is only 1, it should be the number of sets of busters and ghosts for file
    if len(showdown) == 1:
        ghost_count = int(showdown[0])
    # if the x coordinates match, the beam will be vertical and set axis intercept to x intercept to confirm no duplicate verticals
    elif showdown[1] == showdown[4]:
        slopelist.append("vert")
        axis_int.append(showdown[1])
    # else slope needs to be calculated
    else:
        # slope equals delta y over delta x
        slope = (showdown[5] - showdown[2])/(showdown[4] - showdown[1])
        # place slope into slope list
        slopelist.append(slope)
        # if statement to figure out y intercept. if buster is at x = 0, give buster's y
        if showdown[1] == 0:
            axis_int.append(showdown[2])
        # if ghost x is at 0, give ghost y
        elif showdown[4] == 0:
            axis_int.append(showdown[5])
        # else need to calculate y intercept
        else:
            # if statement determining sign needed to translate buster coordinate to y intercept
            # if slope is positive and buster y is negative, make slope negative
            if slope > 0 and showdown[2] < 0:
                slope = slope * -1
            # if slope is negative and buster y is positive, make slope positive
            elif slope < 0 and showdown[2] > 0:
                slope = slope * -1
            # add y intercept as x - y/slope
            axis_int.append(showdown[1] - (showdown[4]/slope))

# setting aliases for required results
success = "All Ghosts: were eliminated"
fail = "All Ghosts: were not eliminated"

# if there are different slopes, then the beams will cross, set resolution with fail message
if len(set(slopelist)) > 1:
    res = fail
# if slopes match but they don't all have different y intercepts, beams will cross. set resolution as fail
elif len(set(axis_int)) != ghost_count:
    res = fail
# else result is positive
else:
    res = success

# return result to standard out
sys.stdout.write(res)

