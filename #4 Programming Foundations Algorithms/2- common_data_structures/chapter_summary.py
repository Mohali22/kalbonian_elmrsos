##### Chapter Summary ( common data structures) #####
# ------------------------------------------------- #

# Introduction to data structures #
# ------------------------------- #

# what is data srtuctuers
# Data Structures are a specialized means of organizing and storing data in computers in such a way that we can perform operations on the stored data more efficiently.

# Most used data structures:
# 1- Array
# 2- Linked list
# 3- Trees
# 4- Hash tables


# [1] - Arrays
# what is an array?
# An array is a collection of elements where the position of each element is identified by an index or a key value. an array just contains a linear set of values, which is often called a one-dimensional array
# Arrays aren't limited to just a linear form. They can have multiple dimensions.
# Accessing elements of the array is a constant-time operation as long as the index of the element is known.

# Complexity in array

# [*] Search: O(1)
# Search on arrays are pretty efficient because as long as we know the index of the element we want, its lookup will be constant time.

# [*] Inserts: O(N)
# Insertions are a little more complex. Inserting elements on your array can cause a change of positions of other elements. For instance, if I have the following array: [1, 5, 6, 8, 3, x] and then I’d like to insert a 4 between 6 and 8. We’d have to scoot the elements 8 and 3 to the right and insert the 4 right where 8 was.

# Doing that is not constant time because the number of elements you'd have to shift to the right will depend on your array size, and that's a characteristic of a complexity that is not constant.


# [*] Appends: O(1)
# Insertions at the end are constant because we just need the current index of the empty slot of the array (if the array is not full, the last position).


# [*] Deletions: O(N)
# Just as insertions, when deleting an element from the array sometimes we will need to scoot certain elements to arrange them sequentially.


# [2] - Linked list
# what is an linked list?
# A linked list is a linear data structure that includes a series of connected nodes.
# each node store the data and the address of the next node.

# You have to start somewhere, so we give the address of the first node a special name called HEAD.
# Also, the last node in the linked list can be identified because its next portion points to NULL.

# example

#         ------------     ------------     ------------
# HEAD -> | 1 | next | ->  | 2 | next | ->  | 3 | next | -> null
#         ------------     ------------     ------------


# Linked List Complexity #
# ---------------------- #

# Time Complexity:

# Search O(n)
# Insert O(1)
# Deletion O(1)

# Space Complexity: --> O(n)
