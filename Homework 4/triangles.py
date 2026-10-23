#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# importing sys library for standard in and out
import sys

# importing math library for least common denominator function
import math


# In[ ]:


# defining triangles function to determine how many right triangles can be made from a set of points
def triangles(points):
    # setting a variable to keep track of the count of triangles
    triangle_count = 0
    # for loop for point at right angle
    for a in range(len(points)):
        # empty list to hold slopes, resets when outer loop goes to next point
        slopes = []
        # inner loop for other points in list
        for b in range(len(points)):
            # if the points match, continue to next point in loop
            if a == b:
                continue
            # if the x coordinate matches, then the line from a to b is vertical
            if points[a][0] == points[b][0]:
                line = "vert"
            # if the y coordinates match, then the line has a slope of 0
            elif points[a][1] == points[b][1]:
                line = "0"
            # or else ...
            else:
                # calculate dy and dx
                delta_y = points[b][1] - points[a][1]
                delta_x = points[b][0] - points[a][0]
                # calculate the greatest common denominator for those deltas
                red = math.gcd(delta_x, delta_y)
                # divide the deltas by that reducer, use // to keep results as integers
                delta_y = delta_y//red
                delta_x = delta_x//red
                # if statement determining sign for the slope and putting it into a varchar variable
                if delta_y > 0 and delta_x > 0:
                    line = f"{delta_y}/{delta_x}"
                elif delta_y < 0 and delta_x < 0:
                    line = f"{abs(delta_y)}/{abs(delta_x)}"
                else:
                    line = f"-{abs(delta_y)}/{abs(delta_x)}"

            # put that slope into the slopes list
            slopes += [line]

            # if statement getting inverse slope that will make a 90 degree angle            
            if line == "vert":
                check = "0"
            elif line == "0":
                check = "vert"
            elif delta_y > 0 and delta_x > 0:
                check = f"-{delta_x}/{delta_y}"
            elif delta_y < 0 and delta_x < 0:
                check = f"-{abs(delta_x)}/{abs(delta_y)}"
            else:
                check = f"{abs(delta_x)}/{abs(delta_y)}"
            # check if that inverse appears in the slopes list, adding count to the triangle count
            triangle_count += slopes.count(check)
    # after loops run, return that triangle count
    return triangle_count


# In[ ]:


# empty list to put in contents of file from standard in
coord = []
# None variable to take the count of points at the top of the file
points_count = None
# for loop to go through standard in file by line
for line in sys.stdin:
    # if this is the first line, place in the Nonve variable
    if points_count is None:
        points_count = line
    # else should be coordinates, split elements and place in list as sub list
    else:
        ll = line.split()
        coord.append([int(ll[0]), int(ll[1])])

# run triangles function on list of points, place in variable
res = triangles(coord)
# write result variable to standard out
sys.stdout.write(str(res))

