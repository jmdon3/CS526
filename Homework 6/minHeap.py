#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# class for individual nodes in heap
class Node():
    # takes value as an argument
    def __init__(self, value):
        # contains references to value, parent node, left child node , and right child
        self.value = value
        self.parent = None
        self.left = None
        self.right = None


# In[ ]:


# import copy library for deep copy
import copy


# In[ ]:


# heap class
class Heap():
    def __init__(self):
        # stores references for its root node and node count
        self.root = None
        self.count = 0

    # function for swapping node values for bubble up and down, takes 2 nodes as argument
    def _swap(self, prev, cur):
        # swapping the given nodes' values
        prev.value, cur.value = cur.value, prev.value

    # internal function for inserting to a maxheap for running median
    def _maxinsert(self, value):
        my_node = Node(value)
        self.count += 1

        if not self.root:
            self.root = my_node
        else:
            bi = bin(self.count)
            cur = self.root

            for i in bi[3:-1]:
                if i == "0":
                    cur = cur.left
                else:
                    cur = cur.right

            if not cur.left:
                cur.left = my_node
            else:
                cur.right = my_node

            my_node.parent = cur

            prev = cur
            cur = my_node

            while prev and prev.value < cur.value:
                self._swap(prev, cur)
                cur = prev
                prev = cur.parent

    # internal function to extract the maximum value from a maxheap for running median
    def _extract_max(self):
        cur = self.root

        if not cur:
            raise IndexError("Heap is empty")
        elif self.count == 1:
            self.root = None
            self.count -= 1
            return cur.value

        bi = bin(self.count)
        res = cur.value
        last = cur

        for i in bi[3:]:
            prev = last
            if i == "0":
                last = last.left
            else:
                last = last.right
        cur.value = last.value

        if prev.right:
            prev.right = None
        else:
            prev.left = None

        self.count -= 1

        while cur.left:
            if cur.right:
                child = cur.left if cur.left.value == max(cur.left.value, cur.right.value) else cur.right
            else:
                child = cur.left

            if cur.value < child.value:
                self._swap(cur, child)
                cur = child
            else:
                break

        return res

    # insert function, takes value as argument
    def insert(self, value):
        # creating the node to be inserted and placing in variable
        my_node = Node(value)
        # increasing heap node count
        self.count += 1

        # if there isn't a root
        if not self.root:
            # make inserted node the root
            self.root = my_node
        # else already has root
        else:
            # getting binary of heap node count including inserting node
            bi = bin(self.count)
            # place root in variable
            cur = self.root

            # for loop going through characters from binary of count to reach next available spot
            # starting from index 3 to avoid leading 1 and characters added by function
            for i in bi[3:-1]:
                # if the character is a 0
                if i == "0":
                    # signifies to move left
                    cur = cur.left
                # else is a 1
                else:
                    # signals moving right
                    cur = cur.right

            # reached parent of next spot
            # if it doesn't have a left child
            if not cur.left:
                # no children, fill in from left
                cur.left = my_node
            # else has 1 by heap logic
            else:
                # fill in empty spot on right
                cur.right = my_node
            # and complete link with parent reference back to current
            my_node.parent = cur

            # node in place, time to determine if the value is valid
            # updating current node to be inserted one and previous as its parent
            prev = cur
            cur = my_node

            # while loop checking if there is a parent to bubble up to and if they should be swapped
            while prev and prev.value > cur.value:
                # call swap function on the current node and its parent
                self._swap(prev, cur)
                # updating references to move up the heap
                cur = prev
                prev = cur.parent

    # peek function to return root of heap
    def peek(self):
        # if there is no root
        if not self.root:
            # raise index error
            raise IndexError("Heap is empty")
        
        # else can return value of root
        return self.root.value

    # function to delete the minimum/root of the heap and return its value
    def extract_min(self):
        # set root to variable current
        cur = self.root

        # if there is no root
        if not cur:
            # raise index error
            raise IndexError("Heap is empty")
        # if the root is the only node on the heap
        elif self.count == 1:
            # clear the root attribute
            self.root = None
            # subtract one from the count attribute
            self.count -= 1
            # and return the value held
            return cur.value

        # else there are at least 2 nodes
        # convert the count to binary and store in a variable
        bi = bin(self.count)
        # store the root's value in a resolution variable
        res = cur.value
        # create a last node variable also pointed to root
        last = cur

        # for loop iterating through characters of the binary count
        for i in bi[3:]:
            # variable to keep track of the parent of the "last" node
            prev = last
            # if the character is a 0
            if i == "0":
                # move last to the left
                last = last.left
            # else a 1
            else:
                # move last right
                last = last.right

        # last is the last node added to the heap
        # set cur, still the root, as the value of last
        cur.value = last.value
        # if last's parent has a right child
        if prev.right:
            # last is to the right, clear the link from the parent
            prev.right = None
        # else right is empty
        else:
            # last is to the left, clear the link
            prev.left = None

        # decrease the count by 1
        self.count -= 1

        # now loop as long as there is a child on the left
        # because the heap is a complete binary tree, there cannot be just a right child
        while cur.left:
            # and if there is also a right child
            if cur.right:
                # set a variable child to be the child with the lower value
                child = cur.left if cur.left.value == min(cur.left.value, cur.right.value) else cur.right
            # else just a left child
            else:
                # set the child as the left one
                child = cur.left

            # if the current node's value is greater than its child's value
            if cur.value > child.value:
                # call the swap function on them to swap values
                self._swap(cur, child)
                # set that child as the new current node
                cur = child
            # else it is less than or equal to and the heap is again valid
            else:
                # break out of the loop
                break

        # the last node has been removed but the minimum is the value deleted
        # return that minimum
        return res

    # function to delete a node by value
    def delete(self, value):
        # store root in variable
        cur = self.root
        # if there is no root
        if not cur:
            # raise index error
            raise IndexError("Heap is empty")
        # if there is only one node on the heap
        elif self.count == 1:
            # if the root's value is what is to be deleted
            if cur.value == value:
                # delete the root and return true
                self.root = None
                self.count -= 1
                return True
            # else it is not, therefore the value is not on the heap
            else:
                # return false
                return False

        # false variable for edge case where the last node added is the one being deleted
        last = False
        # variable for the previous node
        prev = None
        
        # for loop going from 1 to the count. + 1 to run the code at the count value
        for i in range(1, self.count + 1):
            # if the value matches
            if cur.value == value:
                # break out of the loop
                break
            # if the iterable is at the heap count
            if i == self.count:
                # set the last variable to true
                last = True
                
            # convert the iterable to binary and store in variable
            bi = bin(i)
            # reset current to the root for traversal 
            cur = self.root
            # for loop over the binary characters for traversal
            for j in bi[3:]:
                # set the previous node to the current
                prev = cur
                # if the character is a 0
                if j == "0":
                    # move current left
                    cur = cur.left
                else:
                    # else move right
                    cur = cur.right

        # loops have finished, either the value has been found or the heap has been traversed without finding the value
        # if the value doesn't match
        if cur.value != value:
            # return false
            return False
        # else value has been found, if it was found at the last node added
        elif last == True:
            # if its parent has a right child
            if prev.right:
                # it must be the right, so remove link
                prev.right = None
            else:
                # else it must be left, so remove that link
                prev.left = None
        # else it is somewhere in the middle
        else:
            # new variable pointed to root
            rep = self.root
            # getting the binary for the count
            bi = bin(self.count)
            # for loop to get the last node added and its parent
            for j in bi[3:]:
                prevrep = rep
                if j == "0":
                    rep = rep.left
                else:
                    rep = rep.right

            # set cur, node to be deleted, to the value of the last node added
            cur.value = rep.value
            # if the parent of the last node added has a right child
            if prevrep.right:
                # last added is on the right, remove link to right child
                prevrep.right = None
            else:
                # else it is on the left, remove link to left child
                prevrep.left = None

            # while loop in case moved value is smaller than its new parent
            while prev and prev.value > cur.value:
                # swap values
                self._swap(prev, cur)
                # set current to its parent
                cur = prev
                # set previous as its parent
                prev = prev.parent

            # while loop as long as there is a child to bubble down to
            while cur.left:
                # if statement to create a child variable
                if cur.right:
                    # set to minimum if there are 2
                    child = cur.left if cur.left.value == min(cur.left.value, cur.right.value) else cur.right
                else:
                    # or else must be the left
                    child = cur.left

                # if current value is larger than the minimum child's
                if cur.value > child.value:
                    # swap those values
                    self._swap(cur, child)
                    # set current to point to that swapped child
                    cur = child
                # else it is less than or equal to and the heap is back to being valid
                else:
                    # break out of the loop
                    break

        # heap is valid, after deletion, subtract from count
        self.count -= 1
        # return
        return True
                

    # function to build heap from a list of values
    def build(self, values):
        # for loop iterating through list
        for i in values:
            # call insert function to add to heap
           self.insert(i)

    # function to return the list of values from the heap sorted ascending
    def heap_sort(self):
        # if there is no root
        if not self.root:
            # raise index error
            raise IndexError("Heap is empty")

        # make a deep copy of the heap to be destroyed
        dup = copy.deepcopy(self)

        # empty list to store values to be returned
        res = []
        # while loop using is empty function on deep copy
        while not dup.is_empty():
            # run extract min on deep copy and append return to the resolution list
            res.append(dup.extract_min())
            # plus one to iterable
            i += 1

        # return resolution
        return res

    # function to check if the heap is empty
    def is_empty(self):
        # if there isn't a root
        if not self.root:
            # return true
            return True
        else:
            # else return false
            return False

    # function overriding len to work on heap class
    def __len__(self):
        # returns count of nodes
        return self.count

    # print heap function gotten from Google
    def print_heap(self):
        if not self.root:
            print("(Empty tree)")
            return
        lines, *_ = self._build_ascii(self.root)
        for line in lines:
            print(line.rstrip())

    # helper function for print heap
    def _build_ascii(self, node):
        """Returns list of strings, width, height, and horizontal root coordinate."""
        val_str = str(node.value)
        width = len(val_str)

        # Base case: Leaf node
        if node.left is None and node.right is None:
            return [val_str], width, 1, width // 2

        # Only left child exists
        if node.right is None:
            lines, n_width, n_height, n_mid = self._build_ascii(node.left)
            first_line = (n_mid + 1) * " " + (n_width - n_mid - 1) * "_" + val_str
            second_line = n_mid * " " + "/" + (n_width - n_mid - 1 + width) * " "
            shifted_lines = [line + width * " " for line in lines]
            return [first_line, second_line] + shifted_lines, n_width + width, n_height + 2, n_width + width // 2

        # Only right child exists
        if node.left is None:
            lines, n_width, n_height, n_mid = self._build_ascii(node.right)
            first_line = val_str + n_mid * "_" + (n_width - n_mid) * " "
            second_line = (width + n_mid) * " " + "\\" + (n_width - n_mid - 1) * " "
            shifted_lines = [width * " " + line for line in lines]
            return [first_line, second_line] + shifted_lines, n_width + width, n_height + 2, width // 2

        # Both children exist
        left, l_width, l_height, l_mid = self._build_ascii(node.left)
        right, r_width, r_height, r_mid = self._build_ascii(node.right)

        first_line = (l_mid + 1) * " " + (l_width - l_mid - 1) * "_" + val_str + r_mid * "_" + (r_width - r_mid) * " "
        second_line = l_mid * " " + "/" + (l_width - l_mid - 1 + width + r_mid) * " " + "\\" + (r_width - r_mid - 1) * " "

        # Pad shorter subtree with blank lines so rows align
        if l_height < r_height:
            left += [l_width * " "] * (r_height - l_height)
        elif r_height < l_height:
            right += [r_width * " "] * (l_height - r_height)

        merged_lines = [l_line + width * " " + r_line for l_line, r_line in zip(left, right)]
        return [first_line, second_line] + merged_lines, l_width + r_width + width, max(l_height, r_height) + 2, l_width + width // 2

    # function to get the running median value from a set of values using heaps
    def running_median(self, values):
        # make mini a heap
        mini = Heap()
        # make maxi a heap
        maxi = Heap()
        # create an empty list to store running medians
        res = []

        # for loop going through values put through function
        for i in values:
            # if both heaps are empty
            if mini.is_empty() and maxi.is_empty():
                # insert value into maxheap with maxinsert function
                maxi._maxinsert(i)
            # at least maxheap has a node
            # if value is greater than the root of the maxheap
            elif maxi.root.value > i:
                # insert into maxheap with maxinsert
                maxi._maxinsert(i)
            # else less than or equal to
            else:
                # so insert into minheap
                mini.insert(i)

            # now check that heaps are even or off 1
            # if the absolute value of the difference of the counts is more than 1
            if abs(maxi.count - mini.count) > 1:
                # then needs adjustment
                # if there are more in the maxheap
                if maxi.count > mini.count:
                    # extract the maximum from the maxheap and put into variable
                    val = maxi._extract_max()
                    # and insert into minheap
                    mini.insert(val)
                # else there are more in the minheap
                else:
                    # extract minimum from minheap, put into variable
                    val = mini.extract_min()
                    # and maxinsert into maxheap
                    maxi._maxinsert(val)

            # finally, calculate the running median
            # if the heaps are even, the total count is even
            if maxi.count == mini.count:
                # append the average of the heaps' roots to the median list
                res.append((maxi.root.value + mini.root.value)/2)
            # else the total count is odd
            # if there are more in the maxheap
            elif maxi.count > mini.count:
                # append the root of the maxheap converted to a float
                res.append(float(maxi.root.value))
            # else there are more in the minheap
            else:
                # so append the minheap's root converted to a float
                res.append(float(mini.root.value))

        # loop has finished going through all values from the input
        # return the list of running medians
        return(res)

