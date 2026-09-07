# This is your first coding assignment for Computational BME.
# As discussed in class, feel free to use AI tools to help you complete this assignment, but remember to cite them.
# I encourage you to try the problems yourself first and only use AI tools when you are stuck to benefit your learning. 

# Matthew Cherry

# Computing ID: vdq3xk

# AI Citation: I used OpenAI on this assignment to check and proof-read my code.

# %% ###########################################################
# Problem 1: Practice writing pseudocode

# Write pseudocode that will input a integer N and output the sum of the first N numbers in the fibonacci sequence.
# Fibonacci sequence starts: 0, 1, 1, 2, 3, 5, 8, 13, 21, ...
# Example: If N = 5, the output should be 0 + 1 + 1 + 2 + 3 = 7

""" # you can use three double-quotes to write multi-line comments

Set N equal to an integer.

Set a equal to 0 (the first fibonacci number).
Set b equal to 1 (the second fibonacci number).

Set count equal to 0.
Set total equal to 0.

While count is less than N:
    Add a to total.

    Set next_value equal to a + b.
    Set a equal to b.
    Set b equal to next_value.

    Add 1 to count.

Print total.

"""

# %% ###########################################################
# Problem 2: Comment your code
# Comments are very helpful for others (especially when pair-coding!) and yourself to understand your code! Add comments to the following code, which will run but produces the wrong output. Once you comment the code, you should be able to identify the error and fix it (the correct total that should be printed is 12).
N = 6 # N set as an integer representing the number of fibonacci numbers to sum

a = 0 # set a to the first fibonacci number
b = 1 # set b to the second fibonacci number
count = 0 # set count to 0 to keep track of how many fibonacci numbers have been summed
total = 0 # set total to 0 to keep track of the sum of the fibonacci numbers

while count < N: # loop while "count" less than N
    total = total + a # add the current fibonacci number to the total

    next_value = a + b # calculate the next fibonacci number by adding the previous two numbers
    a = b # set a to the current fibonacci number for the next iteration
    b = next_value # set b to the next fibonacci number for the next iteration

    count = count + 1 # Add 1 to count to keep track of how many fibonacci numbers have been summed

print(total) # print total sum of the first N fibonacci numbers

# %% ###########################################################
# Problem 3: Using common Python libraries
# What is the standard deviation of the first 10 numbers in the fibonacci sequence? Use the numpy library to calculate the standard deviation.

import numpy # import the numpy library

fibonacci = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34] # create a list with first 10 numbers in fibonacci sequence
std = numpy.std(fibonacci) # take standard dev of list and assign value to variable "std"
print(std) # print std variable which holds standard dev of list


# %% ###########################################################
# Problem 4: Don't repeat yourself by writing functions
# Write a function that takes an integer N as input and returns the sum of the first N numbers in the fibonacci sequence.
# Then use this function to calculate the sums for N = 5, 10, 15, 20, 25, and 30 and print them as a list.

def fibonacci_sums(N):
    a = 0 # set a to the first fibonacci number
    b = 1 # set b to the second fibonacci number
    count = 0 # set count to 0 to keep track of how many fibonacci numbers have been summed
    total = 0 # set total to 0 to keep track of the sum of the fibonacci numbers

    while count < N: # loop while count is less than N
        total = total + a # add the current fibonacci number to the total

        next_value = a + b # calculate the next fibonacci number by adding the previous two numbers
        a = b # set a to the current fibonacci number for the next iteration
        b = next_value # set b to the next fibonacci number for the next iteration

        count = count + 1 # Add 1 to count to keep track of how many fibonacci numbers have been summed

    return total #returns sum without printing anything

N_values = [5, 10, 15, 20, 25, 30] # declare list on N values given in problem
N_sums = [] # declare empty list for future N sums

for N in N_values: # for loop through values in N_values list
    N_sums.append(fibonacci_sums(N)) # adds sums to N_sums list

print(N_sums) # prints the list of sums


# %% ###########################################################
# Problem 5: Read your error messages
# Run the following code block to see what the error messages are. Then, for each error:
# 1. Identify what type of error it is (SyntaxError, NameError, TypeError, etc.)
# 2. Add a comment to the line that is throwing the error explaining what the error is
# 3. Fix the error so that the code runs correctly

# You will only see one error at a time when you run the code. After fixing one error, run the code again to see the next error. Your final code should work correctly and will have comments where the original errors were.


def find_fib_above_limit(limit):
    """# The function inputs an integer called "limit" and finds the first number that goes above "limit" in the fibonacci sequence. It returns the index of that number.
    :param limit: limit of fibonacci sequence
    :type limit: integer
    :return: index of the first number above limit
    :rtype: integer
    """
    a = 0 # TypeError: these variables (a & b) need to be integers not strings
    b = 1 

    index = 0 # defined the index variable due to the error mentioned below

    while a <= limit:
        next_value = a + b
        a = b
        b = next_value
        index += 1 # NameError: the variable "index" has not been defined before being used in the while loop

    return index


result = find_fib_above_limit(50)
print("The index of the first number above your limit is: ", result)
# %% ###########################################################
# Problem 6: Test your code
# The following function will run but will output the wrong answer sometimes. Add test cases to verify that the function works correctly for a variety of inputs. If you find any inputs that produce incorrect outputs, fix the function. The function, when working properly, should return the sum of all odd Fibonacci numbers less than or equal to the input "limit".


def sum_even_fib(limit):
    a, b = 0, 1
    total = 0
    while b <= limit:
        if b % 2 != 0:  # This line checks if the Fibonacci number is odd
            total = total + b
        a, b = b, a + b
    return total


# Add your test cases here
print(sum_even_fib(2)) # 1) prints 2, adds 1 + 1 (odd numbers), correct
print(sum_even_fib(0)) # 2) prints 0, correct
print(sum_even_fib(13)) # 3) prints 23, adds 1 + 1 + 3 + 5 + 13, correct
print(sum_even_fib(21)) # 4) prints 44, adds 1 + 1 + 3 + 5 + 13 + 21, correct
print(sum_even_fib(20)) # 5) prints 23, does not include 20 because it is an even number and not in the fibonacci sequence, correct
# %%