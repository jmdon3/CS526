#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# creating an array class that stores a stack as a list and keeps a count of its items
class Array:
    def __init__(self):
        self.stack = []
        self.count = 0

    # creating a push function, takes a value that is pushed to the top of the stack
    def push(self, value):
        # adding value to the stack
        self.stack += [value]
        # updating the count of items
        self.count += 1

    # pop function, takes no argument
    def pop(self):
        # if the array is empty, nothing to pop, return error
        if self.count == 0:
            raise IndexError("Array is empty")
        # setting the index for the last item in the stack in an alias
        last_in = self.count - 1
        # putting that items value into a separate alias
        res = self.stack[last_in]
        # updating the stack to be everything but the top item
        self.stack = self.stack[0:last_in]
        # correspondingly decreasing the count
        self.count -= 1
        # return the popped value
        return res

    # peek function, no argument
    def peek(self):
        # if the array is empty, return error
        if self.count == 0:
            raise IndexError("Array is empty")
        # using the same last in alias
        last_in = self.count - 1
        # returning that value
        return self.stack[last_in]

    # is_empty function, no argument
    def is_empty(self):
        # if the count of the array is 0, then it is empty so return true
        if self.count == 0:
            return True
        # else it has items, return false
        return False

    # the reversal function for the question
    # stores an indicator and a before both set to none to start
    def reversal(self, ind = None, bef = None):
        # if the function is just starting, update the ind to equal 0
        if ind is None:
            ind = 0
            # and if the array is empty, return a message saying so
            if self.count == 0:
                return "Array is empty"
            # if the array has 1 item, set before string with just one item
            if self.count == 1:
                bef = f"Before: {self.stack[0]}\n"
            # else set up longer before string
            else:
                # starts with words indicating it is the "before" array
                bef = "Before: "
                # then set an indicator i at 0 to loop through the list for printing purposes
                i = 0
                # loop from bottom to top but stop once you've reached the top
                while i in range(0, self.count - 1):
                    # add the current item's value along with a comma and space
                    bef += f"{self.stack[i]}, "
                    # update the iterating alias
                    i += 1
                # loop has finished, add top value and then return carriage
                bef += f"{self.stack[i]}\n"

        # special cases for arrays of 1 or 2 items
        # if 1 item
        if self.count == 1:
            # can just print one item 
            aft = f"After: {self.stack[0]}"
            # and return before and after messages
            return bef + aft
        # if the array is 2 long
        elif self.count == 2:
            # just need to flip order
            self.stack = [self.stack[1]] + [self.stack[0]]
            # then set after message
            aft = f"After: {self.stack[0]}, {self.stack[1]}"
            # and returning messages here
            return bef + aft

        # else flipping is more involved. get top value
        val = self.stack[self.count - 1]

        # if at index 0
        if ind == 0:
            # updating stack with top item at bottom with the rest on top as is
            self.stack = [val] + self.stack[0:self.count - 1]
        # if index is second from top item
        elif ind == self.count - 2:
            # stack is the existing stack through the third to top, then top, then second to top
            self.stack = self.stack[0:self.count - 2] + [val] + [self.stack[self.count - 2]]
            # now setting up after message for longer arrays same as for before message
            aft = "After: "
            i = 0
            # while loop 
            while i in range(0, self.count - 1):
                # if its not the top, print with a comma and as space
                aft += f"{self.stack[i]}, "
                # add to index indicator
                i += 1
            # loop is done, just add the top item
            aft += f"{self.stack[i]}"
            # and return before and after
            return bef + aft
        # else somewhere in the middle
        else:
            # array should be the existing bottom up to the index, then the index, finally from the index to the top
            self.stack = self.stack[0:ind] + [val] + self.stack[ind:self.count - 1]
        # index indicator for the recursion to keep track
        ind += 1
        # if the code made it this far, recurse storing the updated array, index, and before message
        return self.reversal(ind, bef)


# In[ ]:


# import sys to print results to standard out
import sys

# set alias for my array
a = Array()

# set alias for pushing values to the array
i = 1

# while loop to do the pushing
while i in range(1, 11):
    a.push(i)
    i += 1

# set alias for results of reversal function on array
res = a.reversal()
# print said results to standard out
sys.stdout.write(res)

