#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# establish a class for nodes within a binary search tree
class Node():
    # takes a value as argument
    def __init__(self, value):
        # stores value
        self.value = value
        # also has a parent node, left child node, and right child node
        self.parent = None
        self.left = None
        self.right = None


# In[ ]:


# class for the tree itself
class Tree():
    def __init__(self):
        # has a root 
        self.root = None

    # function to add a node to the tree, takes a value as an argument
    def AddNode(self, value):
        # calls the node class, places in a variable
        my_node = Node(value)

        # if the tree doesn't have a root node, it is the first node for the tree
        if not self.root:
            # set the node as the root
            self.root = my_node
        else:
            # if not, set the root in a separate variable
            cur = self.root
            # variable set to false for finishing the traversal loop
            done = False
            # while loop to traverse tree, uses false variable to maintain
            while not done:
                # if value already exists in the tree
                if cur.value == value:
                    # raise a value error
                    raise ValueError("Value is already in tree")
                
                # if the value of the current node is greater than the value to be added 
                if cur.value > value:
                    # and if the current node doesn't have a left child
                    if not cur.left:
                        # set this node as the left child node
                        cur.left = my_node
                        # complete the link by making the current node the parent to the added one
                        my_node.parent = cur
                        # flip the done variable to true, finishing the loop
                        done = True
                    # else new value is still less than the current, so update the current node to the left child
                    cur = cur.left
                # else value is greater than
                else:
                    # if current node doesn't have a right child
                    if not cur.right:
                        # set new node as right child
                        cur.right = my_node
                        # set added node's parent accordingly
                        my_node.parent = cur
                        # and update loop variable to finish
                        done = True
                    # else move to the right child
                    cur = cur.right

    # setting a delete function that takes a value as an argument
    def DeleteNode(self, value):
        # set root in a variable
        cur = self.root
        # create a previous variable to help with deletion
        prev = None
        # direction variable to help with deletion
        dir = None

        # while loop dependent on there being a current node and that the node doesn't match the given value
        while cur and cur.value != value:
            # set the current node to the previous variable
            prev = cur
            # if the current value is greater than the given
            if cur.value > value:
                # move to the left child
                cur = cur.left
                # update the direction variable accordingly
                dir = "left"
            # else it is less 
            else:
                # so move to the right child
                cur = cur.right
                # and update the direction variable
                dir = "right"

        # loop is finished
        # if the current variable doesn't contain a node
        if not cur:
            # value wasn't found, return false
            return False

        # else there is node to be deleted
        # if statement going through cases
        # start with the node has no children
        if not cur.left and not cur.right:
            # if the current node is also the root
            if cur == self.root:
                # then update the tree root to none
                self.root = None
            # else the while loop iterated at least once, if the direction it last moved was left 
            elif dir == "left":
                # update the left child attribute for the previous node to none
                prev.left = None
            # else it moved right
            else:
                # update right child attr for previous node to none
                prev.right = None
        # and if one is empty, it has one child
        elif not cur.left or not cur.right:
            # if statement assigning the one child to a variable
            child = cur.right if not cur.left else cur.left

            # in case the current is also the root
            if cur == self.root:
                # then the child should be made the root
                self.root = child
                # and its parent is now none
                child.parent = None
            # else it is past the root
            else:
                # if current is the left child of the previous node
                if dir == "left":
                    # then current's child is now the previous node's left child
                    prev.left = child
                else:
                    # current child is now previous node's right child
                    prev.right = child
                # either way, child's parent is previous node
                child.parent = prev
        # else the node to be deleted has 2 children
        else:
            # setting the node to be deleted's left child in a variable
            predcur = cur.left

            # while loop iterating through the predecessors for the largest node on the left
            while predcur.right:
                # if there is a child to the right, repoint the variable
                predcur = predcur.right

            # loop is finished, have identified the largest node on the left side of the node to be deleted
            # updating the current node to the predecessor's value, "deleting" the current one
            cur.value = predcur.value
            # set the predecessor to 0 for easy identification. must be outside of possible range according to instructions
            predcur.value = 0
            # recursivly call the delete function on the value 0 to instead remove the predecessor 
            return self.DeleteNode(0)

        # all cases accounted for, potential false cases already identified so must be true that a node was deleted
        return True

    # find node function by value
    def FindNode(self, value):
        # setting a variable for the root
        cur = self.root

        # in case tree is empty. if so
        if not cur:
            # raise value error
            raise ValueError("This tree is empty")

        # while loop iterating until current no longer points to a node
        while cur is not None:
            # if the loop has reached the value it is looking for
            if cur.value == value:
                # return true
                return True
            # does not match, if the node is bigger
            elif cur.value > value:
                # move the pointer left
                cur = cur.left
            else:
                # else move it right
                cur = cur.right

        # loop has finished without finding the value, must not exist so return false
        return False

    # define a function to print the tree
    # takes current node and level variables as arguments
    def PrintTree(self, cur = None, lvl = 0):
        # if neither argument has been filled,
        if cur is None and lvl == 0:
            # set cur to the root
            cur = self.root
            # and if there is no root
            if not cur:
                # raise value error
                raise ValueError("This tree is empty")

        # if statement ensuring a node is being pointed to in recursives
        if cur is not None:
            # recursivly call function on the right child and advance the level
            self.PrintTree(cur.right, lvl + 1)

            # print the current node using level to multiply how much identation is done
            print(f"{"       " * lvl} --- {cur.value}")

            # recursivly call function on left child. advance the level here as well
            self.PrintTree(cur.left, lvl + 1)


# In[ ]:


# tree class is finished, now to show it functioning
# import sys library to print to standard out
import sys
# import random library in order to randomize node values
import random

# set variable to 1 for loop to create initial tree
i = 1
# empty list to store random integers for initial set to be printed
helper = []

# call tree class, place in variable
bst = Tree()

# while loop to run through 5 times
while i <= 5:
    # call random integer function and store in variable
    num = random.randint(1, 1000)
    # if that number is in the tree
    if num in helper:
        # continue to next loop
        continue
    else:
        # else append the integer to the list
        helper.append(num)
        # and add it as a node to the tree
        bst.AddNode(num)
        # update iterable integer
        i += 1

# now print initial list to standard out
sys.stdout.write(f"{str(helper)}\n")
# and then print the tree to standard out
sys.stdout.write(str(bst.PrintTree()))


# In[ ]:


# new loop using same integer, should only run 3 times
while i <= 8:
    # again calling random int function
    num = random.randint(1, 1000)
    # if it is in the tree already
    if num in helper:
        # continue loop
        continue
    else:
        # else append to list
        helper.append(num)
        # write to standard out that integer is being added
        sys.stdout.write(f"\nAdding: {num}\n")
        # add to tree
        bst.AddNode(num)
        # print updated tree
        sys.stdout.write(str(bst.PrintTree()))

    # now demonstrating delete, using choice function on the helper list to get a valid integer
    num1 = random.choice(helper)
    # remove it from the helper list
    helper.remove(num1)
    # write to standard out what the code is doing
    sys.stdout.write(f"\nDeleting: {num1}\n")
    # delete that number from the tree
    bst.DeleteNode(num1)
    # print new tree to standard out
    sys.stdout.write(str(bst.PrintTree()))
    # and update iterable
    i += 1


# In[ ]:


# creating variables to ensure that find node has positive and negative cases
found = 0
not_found = 0

# while loop for positives
while found < 3:
    # random integer in given range
    tbf = random.randint(1, 1000)

    # if the random integer is in the tree list
    if tbf in helper:
        # write to standard out that code is looking for this node
        sys.stdout.write(f"\nLooking for: {tbf}\n")
        # write to standard out positive result
        sys.stdout.write(str(bst.FindNode(tbf)))
        # update iterable
        found += 1

# while loop for negatives
while not_found < 3:
    # random int
    tbf = random.randint(1, 1000)

    # if its not in the helper list
    if tbf not in helper:
        # write to standard out find function and integer
        sys.stdout.write(f"\nLooking for: {tbf}\n")
        # write to standard out presumed false result
        sys.stdout.write(str(bst.FindNode(tbf)))
        # and update iterable
        not_found += 1

