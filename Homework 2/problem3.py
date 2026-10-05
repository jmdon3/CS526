#!/usr/bin/env python
# coding: utf-8

# In[1]:


# importing cache from functools to improve big O, move burden to memory
from functools import cache

@cache
# creating function 
def ways(n):

    # base cases dealt with, if 0 steps, 0 ways to take them
    if n < 0:
        return 0
    # 1 step, 1 way to take them
    elif n == 0:
        return 1

    # recursion multiple times over, accounting for multiplying options as steps grow
    return ways(n - 1) + ways(n - 2) + ways(n - 3)


# In[ ]:


# importing sys to print results
import sys


# In[2]:


sys.stdout.write(f"Ways for 3 steps: {ways(3)}\n")


# In[3]:


sys.stdout.write(f"Ways for 5 steps: {ways(5)}\n")


# In[4]:


sys.stdout.write(f"Ways for 10 steps: {ways(10)}\n")


# In[ ]:




