#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# node class to populate doubly linked list
# attributes value, prev, next
class Node():
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


# In[ ]:


# doubly linked list class
class DoublyLinkedList():
    def __init__(self):
        # attributes bottom, top, and count of nodes
        self.bot = None
        self.top = None
        self.count = 0

    # push function, value argument. push node to top of list
    def push(self, value):
        # node to be pushed to list
        my_node = Node(value)

        # aliases for the bottom and top of the list
        bot = self.bot
        top = self.top

        # if the list doesn't have a bottom, new node should be the bottom and top
        if not bot:
            self.bot = my_node
            self.top = my_node
        # else make it the current top's next, double link with previous and make it the new top
        else:
            top.next = my_node
            my_node.prev = top
            self.top = my_node

        # for either result of the if statement, add to the count
        self.count += 1

    # pop function, no argument. pop node from top of list 
    def pop(self):
        # if there isn't a bottom node, raise error that the list is empty
        if not self.bot:
            raise IndexError("List is empty")

        # else there's at least one node, create alias for the top node and store its value in res
        top = self.top
        res = top.value

        # if there is only one node, remove it from bottom and top attribute
        if self.count == 1:
            self.bot = None
            self.top = None
        # else the top's previous node should be the new top. also remove next attribute
        else:
            self.top = top.prev
            self.top.next = None

        # either result of if statement should also see the count reduced and return the popped value
        self.count -= 1
        return res

    # peek function, no argument. peek at value of the top node
    def peek(self):
        # if there is no node, raise error
        if not self.bot:
            raise IndexError("List is empty")

        # else return that top node's value
        return self.top.value

    # is_empty function, checks if there is at least one node in the list
    def is_empty(self):
        # if the count is 0, return true
        if self.count == 0:
            return True
        # else return false
        return False

    # reversal function. stores current node and before string to be returned
    def reversal(self, cur = None, bef = None):
        # if cur alias doesn't have a node, should only trigger at first passthrough
        if cur is None:
            # set aliases for bottom and top nodes 
            fifp = self.bot
            cur = self.top
            # if there are no nodes, return message that list is empty
            if self.count == 0:
                return "List is empty"
            # if there is only one node, no reversal needed, just return required message 
            if self.count == 1:
                bef = f"Before: {cur.value}\nAfter: {cur.value}"
                return bef
            # else form before string
            else:
                bef = "Before: "
                # while loop that will run up to the top
                while fifp.next is not None:
                    # add node value to string and move along list with next
                    bef += f"{fifp.value}, "
                    fifp = fifp.next
                # fifp is now top, add value to string
                bef += f"{fifp.value}\n"
                # and reset fifp for count = 2
                fifp = self.bot

        # function has established there are at least 2 nodes, address edge cases
        # if there are 2 nodes
        if self.count == 2:
            # flip order in the after string
            aft = f"After: {cur.value}, {fifp.value}"
            # flip next and prev attributes for bottom
            fifp.next, fifp.prev = fifp.prev, fifp.next
            # flip attributes for top
            cur.next, cur.prev = cur.prev, cur.next
            # update bottom and top ids
            self.bot = cur
            self.top = fifp
            # and return strings
            return bef + aft
        # last edge case, current is now pointed at the bottom node
        elif cur == self.bot:
            # flip next and previous for bottom node
            cur.next, cur.prev = cur.prev, cur.next
            # flip bottom and top now that all node attributes are updated
            self.bot, self.top = self.top, self.bot
            # list has been reversed, start building after string
            aft = "After: "
            # resetting cur to the bottom, was just made top
            cur = self.bot
            # while loop for returned string using next attribute to stop at top
            while cur.next is not None:
                # update string and move cur along list
                aft += f"{cur.value}, "
                cur = cur.next
            # cur is back at the top, update with final value
            aft += f"{cur.value}"
            # and return strings
            return bef + aft

        # for all nodes between top and bottom, just need to flip prev and next
        cur.next, cur.prev = cur.prev, cur.next
        # and then move cur to the next node, was until previous line the prev node
        cur = cur.next
        # then return recursive function
        return self.reversal(cur, bef)


# In[ ]:


# import sys library to write to standard out
import sys

# create a list for demonstration
a = DoublyLinkedList()

# set alias to push multiple nodes with a loop
i = 1

# loop going from 1 to 10
while i in range(1, 11):
    # each value is pushed into a new node on the list
    a.push(i)
    # iterate values to move loop and demonstrate reversal
    i += 1

# run reversal function and place in alias
res = a.reversal()
# write result to standard out
sys.stdout.write(res)

