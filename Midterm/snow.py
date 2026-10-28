#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# import sys library for standard in and out
import sys


# In[ ]:


# defining a function that takes a file as input
def snowfall(file):
    # input variable as an empty list
    nput = []
    # for loop to go through file by line
    for line in file:
        # splits each line into individual elements and puts it into the input variable
        nput += line.split()

    # gets the number of days from the first index of the list and puts it into a variable
    days = int(nput[0])
    # if that days variable is less than 3, then the function should return no
    if days < 3:
        return "NO"
    # put the rest of input into a new variable as integers
    snow_tot = [int(x) for x in nput[1:]]
    # new empty list for the daily amounts of snow fall
    snow_daily = []
    # variable set to 0 for a running total to calculate daily snow fall
    run_tot = 0
    # for loop to calculate the daily snow fall
    for d in range(0, len(snow_tot)):
        # puts the snow total less the running total into the daily list
        snow_daily += [snow_tot[d] - run_tot]
        # update running total to the current from snow total
        run_tot = snow_tot[d]

    # set a new variable to 0 for a loop to check the 3 day total condition
    w = 0
    # halving the total snowfall for the target to be used in the loop
    target = run_tot / 2
    # while loop to go up to the point where the 3 day total can be tested
    while w < days - 2:
        # if these 3 days surpass the target number, return yes
        if snow_daily[w] + snow_daily[w + 1] + snow_daily[w + 2] > target:
            return "YES"
        # else, iterate the looping variable
        w += 1

    # while loop has finished with no yes, return no
    return "NO"


# In[ ]:


# place the file from standard in into a variable
snow = sys.stdin

# write to standard out the result of running the snowfall function on the standard in file
sys.stdout.write(snowfall(snow))

