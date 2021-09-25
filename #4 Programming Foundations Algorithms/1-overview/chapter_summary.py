##### Chapter Summary ( overview) #####
# ----------------------------------- #


# what are algorithms #
# ------------------- #

# An algorithm is an effective step-by-step procedure for solving a problem in a finite number of steps. In other words, it is a finite set of well-defined instructions or step-by-step description of the procedure written in human readable language for solving a given problem.

# An algorithm itself is division of a problem into small steps which are ordered in sequence and easily understandable. Algorithms are very important to the way computers process information, because a computer program is basically an algorithm that tells computer what specific tasks to perform in what specific order to accomplish a specific task. The same problem can be solved with different methods.

# So, for solving the same problem, different algorithms can be designed. In these algorithms, number of steps, time and efforts may vary more or less.


# Characteristics of an Algorithm #
# ------------------------------- #

# An algorithm must possess following characteristics:
# 1- Finiteness: An algorithm should have finite number of steps and it should end after a finite time.
# 2- Input: An algorithm may have many inputs or no inputs at all.
# 3- Output: It should result at least one output.
# 4- Definiteness: Each step must be clear, well-defined and precise. There should be no any ambiguity.
# 5- Effectiveness: Each step must be simple and should take a finite amount of time.

# [*] Any given algorithm has associated complexity and there are usually more than one.
# [*] There is space complexity: which describes how much memory and storage space an algorithm needs to do its work.
# [*] There is also time complexity: which describes how efficient the algorithm is in relation to the given amount of input to work on.


# Common algorithms in programming #
# -------------------------------- #

# 1- searh algorithms
# Search algorithms are used in cases where you need to find a specific piece of data within a larger data structure. For example, searching for a substring within a larger string

# 2- sorting algorithms
# A sorting algorithm is a method for reorganizing a large number of items into a specific order, such as alphabetical, highest-to-lowest value or shortest-to-longest distance. Sorting algorithms take lists of items as input data, perform specific operations on those lists and deliver ordered arrays as output

# 3- computational algorithms
#  Computational algorithms are used to take one set of data and derive another set of data from it. And a simple example might be calculating whether a given number is a prime number

# 4- collection algorithms
#  Collection algorithms, which involve manipulating or navigating among sets of data that are stored within a particular structure.


# example

# Find the greatest common denominator of two numbers
# using Euclid's algorithm

def gcd(a, b):
    while (b != 0):
        t = a       # set aside the value of a
        a = b       # set a equal to b
        b = t % b   # divide t (which is a) by b

    return a


# try out the function with a few examples
print(gcd(60, 96))  # should be 12
print(gcd(20, 8))   # should be 4


# Measuring algorithm performance #
# ------------------------------- #

# what is Big-O?
# Big-O notation is the language we use for talking about how long an algorithm takes to run (time complexity) or how much memory is used by an algorithm (space complexity). Big-O notation can express the best, worst, and average-case running time of an algorithm.

# what are the most operations/steps that could happen for an input of size n?

# 1- O(1) => Constant Time
# O(1) means that it takes a constant time to run an algorithm, regardless of the size of the input.

# 2- O(n) => Linear Time
# O(n) means that the run time increases at the same pace as the input.

# 3- O(n²) => Quadratic Time
# O(n²) means that the calculation runs in quadratic time, which is the squared size of the input data.

# 4- O(log n) => Logarithmic Time
# O(log n) means that the running time grows in proportion to the logarithm of the input size, meaning that the run time barely increases as you exponentially increase the input.
