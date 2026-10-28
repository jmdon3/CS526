#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# importing sys library for standard in, out
import sys

# importing math library to calculate square roots
import math


# In[ ]:


# defining function that checks whether or not a puzzle board is valid, takes board, valid symbols, and number n as arguments
def puzzle(board, sym, num):
    # setting variable with invalid message, each check to determine invalidness, only valid if it passes all 
    res = "The board is invalid"
    # for loop to check rows for duplicate symbols
    for x in range(num):
        # inner loop going through valid symbol list
        for a in sym:
            # if current valid symbol appears more than once, return invalid message
            if board[x].count(a) > 1:
                return res

    # for loop to check columns
    for y in range(num):
        # empty list to be reset once all elements in the column are checked from inner loop
        vert = []
        # setting inner loop to iterate through row indices
        for z in range(num):
            # if current element not a valid symbol i.e. a period
            if board[z][y] not in sym:
                # continue looping
                continue
            # if the valid symbol is already in my column list
            if board[z][y] in vert:
                # return invalid message
                return res
            # else, append to the column list
            vert.append(board[z][y])

    # calculate the square root of n and put into variable
    sqr = int(math.sqrt(num))

    # triple for loop to go through sub boards, each using square root of n as the range
    # first establishing sub board loop
    for a in range(sqr):
        # multiply iteratable by square root of n so that inner indexing works
        subsqr = a * sqr
        # establish sub board list/clear in iteration
        sublst = []
        # second loop, calling rows
        for b in range(sqr):
            # third loop calling column 
            for c in range(sqr):
                # if the current element (using sub board integer to index correctly) is not a valid symbol
                if board[b + subsqr][c + subsqr] not in sym:
                    # continue looping
                    continue
                # valid symbol, if it is already in the sub square list
                if board[b + subsqr][c + subsqr] in sublst:
                    # return invalid message
                    return res
                # else add to the sub board list
                sublst += board[b + subsqr][c + subsqr]

    # all board validity tests passed, return valid message
    return "The board is valid"


# In[ ]:


# put file from standard in into variable
file = sys.stdin

# set none variable to catch n from file
n = None
# set none variable to catch valid symbol list
valid = None
# empty list to put puzzle board in
puz = []
# for loop to read file
for line in file:
    # strip extraneous spaces, line breaks from line
    line = line.strip()
    # if the line is empty
    if not line:
        # continue loop
        continue
    # if n is none ie first filled line
    if n is None:
        # place into n variable
        n = int(line)
    # if valid is none ie second filled line
    elif valid is None:
        # create valid list
        valid = []
        # and put line into it
        valid += line.split(",")
    # else belongs in board
    else:
        # so put into board
        puz.append(line.split(","))

# call puzzle function using info from file and write result to standard out
sys.stdout.write(puzzle(puz, valid, n))

