#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# creating Node class, contains a value and a reference "link" to the next node
class Node():
    def __init__(self, value):
        self.value = value
        self.next = None


# In[ ]:


# creating SinglyLinkedList class as composed of Nodes. has a head, tail, and count
class SinglyLinkedList():
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    # append function to add node with value to end of list
    def append(self, value):
        # incorporating Node class, contains value given in append function 
        my_node = Node(value)

        # if statement saying if there is no head of the list (no nodes) then make it the head and tail
        if not self.head:
            self.head = my_node
            self.tail = my_node
        # else it should be the tail and the current tail's "next" connection
        else:
            self.tail.next = my_node
            self.tail = my_node
       
        # plus one to the list's count as it is adding a node
        self.count += 1

    # prepend function. add node to the beginning of the list
    def prepend(self, value):
        # prepending node. takes value from function
        my_node = Node(value)

        # if statement for if the list is empty, node should be tail and head
        if not self.head:
            self.head = my_node
            self.tail = my_node
        # else it should just be the head and the current head should be this one's "next"
        else:
            my_node.next = self.head
            self.head = my_node

        # plus one to list's count
        self.count += 1

    # insert func. takes index and value arguments for where to insert and what it contains
    def insert(self, index, value):
        # if statement to throw error if the index is invalid
        if index < 0 or index > self.count:
            raise IndexError("Index not valid")

        # node that takes value arg
        my_node = Node(value)

        # if statement for if the list is empty, makes node head and tail
        if not self.head:
            self.head = my_node
            self.tail = my_node
        # if the given index is 0 and the list isn't empty, make node head and old head next
        elif index == 0:
            my_node.next = self.head
            self.head = my_node
        # if index is the count, make the node the tail and current tail's next
        elif index == self.count:
            self.tail.next = my_node
            self.tail = my_node
        # else iterate through list to index
        else:
            # alias to store "current" node for loop, starting at head
            cur = self.head
            # iterating up to one less than index, can then reference next where node will be placed
            for i in range(index - 1):
                cur = cur.next

            # setting node into list, new node links to "next" node", node currently at index links to new
            my_node.next = cur.next
            cur.next = my_node

        # plus one to node count
        self.count += 1

    # get func to return value at specified index
    def get(self, index):
        # if index outside of count, return error
        if index < 0 or index > self.count:
            raise IndexError("Index not valid")

        # aliases for node and index for iterating, "res" to store value
        cur = self.head
        ind = 0
        res = None

        # loop to iterate through list
        while ind <= index:
            # if the index has been reached, put the value in designated alias and break
            if ind == index:
                res = str(cur.value)
                break
            # else iterate through list and update ind alias
            else:
                cur = cur.next
                ind += 1

        # return found value
        return res

    # find func to id first node with given value
    def find(self, value):
        # aliases for iterating
        cur = self.head
        ind = 0

        # loop to check through list for value
        while ind <= self.count:
            # if the node value is a match, break from loop
            if cur.value == value:
                break
            # if the node viewed is the tail, can break from loop
            elif cur == self.tail:
                break
            # else iterate
            else:
                cur = cur.next
                ind += 1

        # if loop found a match, return the index
        if cur.value == value:
            return str(ind)
        # else return -1 to indicate the value isn't in list
        else:
            return "-1"

    # taking the len func to work with SinglyLinkedList class
    def __len__(self):
        # using logic discussed in class, using create functions to maintain count, just returns that value
        return self.count

    # update func, takes index and value to change stored value of node
    def update(self, index, value):
        # if index isn't valid, return error
        if index < 0 or index > self.count:
            raise IndexError("Index not valid")

        # aliases to iterate to given index
        cur = self.head
        ind = 0

        # loop
        while ind <= index:
            # if given index has been reached, replace the stored value
            if ind == index:
                cur.value = value
                break
            # else iterate
            else:
                cur = cur.next
                ind += 1

    # delete func to remove node by value, first only if there are multiple
    # will return True if a node is deleted, False if not
    def delete(self, value):
        # set alias to iterate
        cur = self.head

        # if the list is empty, then nothing to delete
        if cur is None:
            return False

        # if the head node matches, make the next node the head and decrease list count
        if cur.value == value:
            self.head = cur.next
            # if there wasn't a next node, then tail should also be cleared
            if self.head is None:
                self.tail = None
            self.count -= 1
            return True

        # while loop to iterate
        while cur.next is not None:
            # if the next node has the value, repoint the link to delete
            # look ahead to repoint the current link
            if cur.next.value == value:
                # if the next node is also the tail, reassign current node as tail, clear link, decrease count
                if cur.next == self.tail:
                    self.tail = cur
                    cur.next = None
                    self.count -= 1
                # not the tail, relink node to the node after and decrease count
                else:
                    cur.next = cur.next.next
                    self.count -= 1
                # can end loop and return True
                return True
            # not a match, set variable to next node
            cur = cur.next

        # if loop completes without deleting, then return false
        return False

    # delete_at func, delete node by index
    def delete_at(self, index):
        # if the index is invalid, return error
        if index < 0 or index >= self.count:
            raise IndexError("Index not valid")

        # aliases for iterating including res to store returned value
        cur = self.head
        ind = 0
        res = None

        # if index is 0, then the head must be reassigned, can avoid looping
        if index == 0:
            res = cur.value
            self.head = cur.next
            # if there was no next, tail should also be cleared
            if self.head is None:
                self.tail = None
            self.count -= 1
            return res

        # loop to go through list up to node before index
        while ind < index - 1:
            cur = cur.next
            ind += 1

        # cur now node before, set res as next value
        res = cur.next.value
        # if the next node is the tail, set current node to be tail, remove link
        if cur.next == self.tail:
            self.tail = cur
            cur.next = None
        # else update link to point to node after deleted node
        else:
            cur.next = cur.next.next
        # reduce list count
        self.count -= 1
        # return stored value
        return res

    # print_list func to print list of nodex
    def print_list(self):
        # if the list is empty, return specified message
        if not self.head:
            return "(empty)"

        # else create aliases to iterate through list for recording values
        res = ""
        cur = self.head

        # iterating loop contingent on the alias containing a node
        while cur:
            # if the current node is the tail, add value to the res alias
            if cur == self.tail:
                res += str(cur.value)
            # else add value and singly linked symbol
            else:
                res += str(cur.value)
                res += " -> "

            # then iterate
            cur = cur.next

        # loop completed, return resolution
        return res

