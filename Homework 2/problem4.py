#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# first node class with a value to store given, provide for links to previous and next
class Node():
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


# In[ ]:


# separate class for the list itself
class SortedDoublyLinkedList():
    # has a head and a tail
    # also storing a count of nodes to help with indexing in functions
    # and sum of values for the total function
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0
        self.sum = 0

    # add function, needs a value for the node
    def add(self, value):
        # alias for the node that stores the value
        my_node = Node(value)

        # setting alias for the head node and tail node
        cur = self.head
        tl = self.tail

        # if there is no head then the list is empty
        if not self.head:
            # set added node as the head and the tail
            self.head = my_node
            self.tail = my_node
        # if the value in the head is larger than the added value, then new node is head    
        elif cur.value >= value:
            # set up links then reassign the head
            cur.prev = my_node
            my_node.next = cur
            self.head = my_node
        # if new value is bigger than or equal to the tail, make it the new tail
        elif tl.value <= value:
            # set links with tail and then reassign tail
            tl.next = my_node
            my_node.prev = tl
            self.tail = my_node
        # else the new node goes somewhere in the middle
        else:
            # loop as long as there is a node and its value is smaller than the new one
            while cur and cur.value < value:
                cur = cur.next

            # value is now either larger or equal to the current. inserting here
            # setting links for new node
            my_node.next = cur
            my_node.prev = cur.prev

            # updating links for existing nodes inserted between
            cur.prev.next = my_node
            cur.prev = my_node

        # updating list count and sum
        self.count += 1
        self.sum += value
    
    # delete function going by node value
    def delete(self, value):
        # alias for the node head
        cur = self.head

        # if the list is blank, no node to delete, return false
        if cur is None:
            return False

        # checking if the value is in the head
        if cur.value == value:
            # first subtracting value from the list sum
            self.sum -= value
            # updating the head
            self.head = cur.next
            # if there is a new head, remove previous link for new head
            if self.head is not None:
                cur.next.prev = None
            # else tail reference should also be removed
            else:
                self.tail = None
            # now subtract node from count and return true
            self.count -= 1
            return True

        # loop checking that there is a next node and it is smaller than value
        while cur.next is not None and cur.next.value <= value:
            # if they match, update the links and update sum
            if cur.next.value == value:
                targ = cur.next
                self.sum -= value

                cur.next = targ.next

                # if there is a node after the target, update the link
                if targ.next is not None:
                    targ.next.prev = cur
                # else it is now the tail
                else:
                    self.tail = cur
                self.count -= 1
                return True

            # updating the cur alias for the loop
            cur = cur.next

        # if the loop isn't interrupted (no delete) then return false
        return False

    # exists function to check for a value
    def exists(self, value):
        # alias for the head
        cur = self.head

        # loop for checking if the value is smaller than the current node's value
        while cur is not None and cur.value <= value:
            # if they match, return true
            if cur.value == value:
                return True
            # else iterate
            else:
                cur = cur.next
        # if the loop finished without a return then the value isn't in the list
        return False
    
    # print list func
    def print_list(self):
        # if the list is empty, return that
        if not self.head:
            return "(empty)"

        # aliases for the head node and the string to be printed
        res = ""
        cur = self.head

        # loop dependent on there being a node
        while cur:
            # edge case for single node, just print the value
            if cur == self.head and cur == self.tail:
                res += str(cur.value)
            # if there are multiple nodes and you reached the tail, just print the value
            elif cur == self.tail:
                res += str(cur.value)
            # else print the value and the doubly linked symbol
            else:
                res += str(cur.value)
                res += " <-> "
            # end of if statement, iterate
            cur = cur.next

        # loop is done, return the completed "resolution"
        return res

    # total func for the sum of the values in the nodes
    def total(self):
        # accounting for the sum as attribute of the list, just return that sum
        return self.sum

    # function to sum three nodes from the middle of the list
    def sum_middle_three(self):
        # if there are less than 3 nodes, then there aren't enough for the function
        if self.count < 3:
            raise ValueError("Not enough nodes")
        # set alias for head for iterating
        cur = self.head

        # if statements to figure out where to start adding values
        # if there are 3 nodes, just start at 0
        if self.count == 3:
            mid_str = 0
        # if there are an even number of nodes
        elif self.count % 2 == 0:
            # start 2 before the middle
            mid_str = (self.count // 2) - 2
        # else odd count, start 1 before the middle
        else:
            mid_str = (self.count // 2) - 1


        # adding 2 to the start of the middle to get the end of the middle
        # for loop end point
        mid_end = mid_str + 2

        # set aliases to help with tracking the index and the sum to be returned
        ind = 0
        val = 0
        # loop up to the end of the middle index
        while ind <= mid_end:
            # if the index is within the middle, add the node value to the result
            if ind >= mid_str:
                val += cur.value
            # else iterate
            cur = cur.next
            ind += 1
        # loop is finished, return the sum
        return val

    # list median function
    def median(self):
        # no median if the list is empty
        if self.count is None:
            raise ValueError("List is empty")

        # head alias for iterating
        cur = self.head

        # if the head is also the tail then it is also the median
        if cur == self.tail:
            return cur.value
        # if the list is 2 nodes long, return the average of the 2 values 
        elif self.count == 2:
            return (cur.value + cur.next.value)/2
        # else we have to iterate to get the middle
        else:
            # set middle alias and index helper
            mid = self.count // 2
            ind = 0
            # loop until ind matches middle
            while ind < mid:
                # if index has come to the final loop
                if ind == mid - 1:
                    # and if the list is even, then return average of value and next val
                    if self.count % 2 == 0:
                        return (cur.value + cur.next.value)/2
                    # else list is odd, just need the next value
                    else:
                        return cur.next.value
                # haven't reached middle, iterate
                cur = cur.next
                ind += 1

    # count function. double underscore as count is built in
    def __count__(self, value):
        # if list blank, no values to count
        if self.count is None:
            raise ValueError("List is empty")

        # head alias, index helper, and res to store count of value
        cur = self.head
        ind = 0
        res = 0

        # looping through index up to node count
        # list is sorted, so only need to iterate if the node value is <= value
        while ind < self.count and cur.value <= value:
            # if the node value matches, add to the stored count
            if cur.value == value:
                res += 1
            # either way, iterate
            cur = cur.next
            ind += 1

        # loop has finished, return result
        return res

