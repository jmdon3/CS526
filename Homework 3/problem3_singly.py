#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# setting the class node, needs a value and can have a next attribute
class Node():
    def __init__(self, value):
        self.value = value
        self.next = None


# In[ ]:


# setting singly linked list class, has a bottom, top, and count
class SinglyLinkedList():
    def __init__(self):
        self.bot = None
        self.top = None
        self.count = 0

    # push function, takes a value as an argument
    def push(self, value):
        # creating a node from the new class
        my_node = Node(value)

        # if there is no bottom node (empty list), make the pushed node the bottom and top
        if not self.bot:
            self.bot = my_node
            self.top = my_node
        # else set the current top's next node as the new node and the new node is the top
        else:
            self.top.next = my_node
            self.top = my_node

        # add to list count
        self.count += 1

    # pop function, no argument
    def pop(self):
        # if the list node count is 0
        if self.count == 0:
            # rais an error that the list is empty
            raise IndexError("Linked list is empty")

        # set aliases for the top and the bottom of list, also putting the top value in an alias
        top = self.top
        cur = self.bot
        res = top.value

        # if the list is just one node, set the bottom and top to none
        if self.count == 1:
            self.bot = None
            self.top = None
        # if there are 2 nodes, the bottom should also be the top, and it shouldn't have a next
        elif self.count == 2:
            self.top = cur
            cur.next = None
        # else, loop
        else:
            # until the second to last node
            while cur.next.next is not None:
                cur = cur.next

        # the second to last should now be the top
        self.top = cur
        # and shouldn't have a next node link
        cur.next = None
        # decrease node count
        self.count -= 1
        # and return the value of the popped node
        return res

    # peek function, no argument
    def peek(self):
        # if the list is empty, raise an error saying so
        if self.count == 0:
            raise IndexError("Linked list is empty")

        # else return the value from the top node
        return self.top.value

    # is_empty function
    def is_empty(self):
        # if there are no nodes in the list, return true
        if self.count == 0:
            return True
        # else return false
        return False

    # reversal function, contains aliases for current node, old top node, previously moved node
    # index, and before reversal string
    def reversal(self, cur = None, old_top = None, prev = None, ind = None, bef = None):
        # if cur is none, function just started
        if cur is None:
            # set current to the bottom node and index to 0
            cur = self.bot
            ind = 0

            # if the list count is 0, return message saying so
            if self.count == 0:
                return "Array is empty"
            # if the node count is 1, before message is easy
            if self.count == 1:
                bef = f"Before: {cur.value}\n"
            # else, using a loop
            else:
                bef = "Before: "
                # loop until you hit the top of the list
                while cur.next is not None:
                    bef += f"{cur.value}, "
                    cur = cur.next
                # add final node value to before string
                bef += f"{cur.value}\n"

            # before finishing if statement, set old top to the original top
            old_top = self.top
            # and reset current to the bottom
            cur = self.bot
            
        # now for reversing, start with special cases
        # if there is one node, no reversal happening so before matches after
        if self.count == 1:
            aft = f"After: {cur.value}"
            # and return the two result strings
            return bef + aft
        # if there are 2
        elif self.count == 2:
            # flip bottom and top attributes
            self.bot, self.top = self.top, self.bot
            # current now pointing to the top, shouldn't have a next
            cur.next = None
            # old top now on the bottom, should link to current
            old_top.next = cur
            # create after string
            aft = f"After: {old_top.value}, {cur.value}"
            # return strings
            return bef + aft

        # now for longer lists, for the first move
        if ind == 0:
            # moving the bottom to the top
            old_top.next = cur
            # making the node linked to the current the new bottom
            self.bot = cur.next
            # removing the link from the current node
            cur.next = None
            # and name it the top
            self.top = cur
            # setting the current as the previously moved
            prev = cur
            # now assigning the new bottom as the current
            cur = self.bot
            # updating the index
            ind += 1
            # recursion with the shifted node 
            return self.reversal(cur, old_top, prev, ind, bef)
        # if the ind is 2 less than the count, this is the final move 
        elif ind == self.count - 2:
            # the old top is now the bottom
            self.bot = old_top
            # the new bottom is now linked to the current node
            old_top.next = cur
            # the current node is now linked to the previously moved node
            cur.next = prev
            # list has been reversed. start on after string
            aft = "After: "
            # new alias for string creation loop
            nod = self.bot
            # until the top, add value to the string
            while nod.next is not None:
                aft += f"{nod.value}, "
                nod = nod.next
            # now at the top, one final add to the string
            aft += f"{nod.value}"
            # return messages
            return bef + aft
        # for all other nodes in between, update the bottom
        self.bot = cur.next
        # put the current after the old top
        old_top.next = cur
        # the current is now linked to the previously moved node
        cur.next = prev
        # updating the current as the previously moved
        prev = cur
        # new bottom is now the current node
        cur = self.bot
        # update the index
        ind += 1
        # recurse the function
        return self.reversal(cur, old_top, prev, ind, bef)


# In[ ]:


# import sys library to write to standard out
import sys

# create alias for singly linked list
a = SinglyLinkedList()

# alias for pushing nodes to the list with a loop
i = 1

# loop going from 1 to 11
while i in range(1, 11):
    # push a node to the list with the current integer in the range
    a.push(i)
    # update the integer
    i += 1

# reverse the node and put the return in an alias
res = a.reversal()
# write the return to standard out
sys.stdout.write(res)

