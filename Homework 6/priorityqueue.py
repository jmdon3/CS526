#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# defining function to sort sales from a nested list
def registerqueue(sales):
    # create a list to put the log of ordered sales into
    finallog = []
    # creating a copy of the nested list to not destroy the original
    reg = [list(sub) for sub in sales]

    # while loop checking that the copy isn't empty
    while any(reg):
        # for loop getting the first item from each sublist with an item and saving the minimum to a variable
        minsale = min(sub[0] for sub in reg if sub)
        # second inner for loop going through each sublist
        for i in range(len(reg)):
            # if there is something in this sublist and the first item matches the calculated minimum for the list
            if reg[i] and reg[i][0] == minsale:
                # append tuple to the final log with sale time and register number, indexed from 1
                finallog.append((minsale, i + 1))
                # pop the first item from the sublist
                reg[i].pop(0)
                # break out of the for loop
                break

    # copy is now blank, return the completed final log
    return finallog


# In[ ]:


# import sys library for standard in, standard out
import sys


# In[ ]:


# variable for file from standard in
file = sys.stdin
# empty list to put in contents from file
sales = []

# for loop going through file by line
for line in file:
    # strip excess spaces
    line = line.strip()
    # remove first character, the open bracket, from string
    line = line[1:]
    # remove final character, close bracket, from string
    line = line[:-1]
    # split the line by comma and space then append the split list to the sales list
    sales.append(line.split(", "))

# nested for loop creating a new list converted to integers
finsale = [[int(n) for n in sub if n.strip()] for sub in sales]

# run created function on nested list of integers, place into variable
res = registerqueue(finsale)

#print results to standard out matching output files
# get number of registers by length of initial list, total sales by length of the function results
# and then use the result for the ordered list of sales times and registers
sys.stdout.write(f"Registers: {len(sales)}\nTotal sales: {len(res)}\nMerged log: {str(res)}")

