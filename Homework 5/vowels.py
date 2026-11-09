#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# import sys library for standard in, out
import sys

# get Path function from pathlib library to get file name for the required output
from pathlib import Path


# In[ ]:


# defining function to find how many vowel combinations can be made from morse code from file
# takes the number of symbols in the text and the text itself as arguments
def MorseVowels(symb_count, text):
    # create a state table to record how many combinations are possible
    # uses individual rows for vowels that need 1, 2, or 3 characters
    state_tbl = [[], [], []]

    # hard code how each vowel is made in morse code to check the input
    E = "."
    A = ".-"
    I = ".."
    O = "---"
    U = "..-"

    # integer j starting at 0 to iterate through the input text
    j = 0

    # while loop using the count of symbols from the text as the limit
    while j <= symb_count:
        # if statements keeping track of the offset for the state table
        # if the loop is looking at the first couple of characters
        if j < 2:
            # offset is 1
            offset = 1
        # if the loop is on the 3rd character
        elif j == 2:
            # offset is the sum of the offset for 1 character at the second character
            # and for 2 characters at the first character
            offset = state_tbl[0][1] + state_tbl[1][0]
        # else beyond that ...
        else:
            # sum of offsets for 1 character from previous character
            # 2 characters from character before that
            # and 3 characters from the one before the last one
            offset = state_tbl[0][j - 1] + state_tbl[1][j - 2] + state_tbl[2][j - 3]

        # if j is at the symbol count, text is finished
        if j == symb_count:
            # so return the offset for count of potential combinations
            return offset

        # if current character matches code for E
        if text[j] == E:
            # one char variable equals the offset
            one = offset
        else:
            # else it should be 0
            one = 0

        # if current character and the next one matches A or I AND there are at least 2 characters to be looked at
        if text[j:j + 2] in [A, I] and j < symb_count - 1:
            # then the count for two char should be the offset
            two = offset
        else:
            # else it should be 0
            two = 0

        # if current character plus the next 2 matches O or U AND there are at least 3 characters to be looked at
        if text[j:j + 3] in [O, U] and j < symb_count - 2:
            # count for three char should be offset
            three = offset
        else:
            # else it should be 0
            three = 0

        # update the state table with the combinations counts for 1, 2, or 3 characters
        state_tbl[0].append(one)
        state_tbl[1].append(two)
        state_tbl[2].append(three)

        # and iterate the j integer
        j += 1


# In[ ]:


# place the file from standard in into a variable
file = sys.stdin

# variables to store information from the input file
symb_count = 0
code = None

# for loop to iterate through the file by line
for line in file:
    # if symbol count is 0, then its the first line
    if symb_count == 0:
        # convert to integer and put into count variable
        symb_count = int(line)
    # else its the second line
    else:
        # put into morse code variable
        code = line

# use libraries to extract file name from the standard in
# file_path = sys.stdin.read()
# filename = Path(file_path).name


# formatting text for response including running the function against the info from the input file
sys.stdout.write(f"File Input: {sys.stdin.name}\nThe Number of Vowel combinations is: {MorseVowels(symb_count, code)}")

