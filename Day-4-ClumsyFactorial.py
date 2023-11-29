"""
Problem Statement
Clumsy Factorial
The clumsy factorial of a positive integer n is obtained by applying a fixed rotation of operations, including multiplication '*', division '/', addition '+', and subtraction '-', to the integers in decreasing order. The operations are applied according to the usual order of operations in arithmetic, where multiplication and division are done before addition and subtraction.
For example, the clumsy factorial of n = 10 is calculated as follows:
clumsy(10) = 10 x 9 / 8 + 7 - 6 x 5 / 4 + 3 - 2 x 1.
We use floor division for the division operation, meaning the result is rounded down to the nearest integer.
Your task is to implement a function that takes a positive integer n as input and returns the clumsy factorial of n.

Important Note:
Ensure that you save your solution before progressing to the next question and before submitting your answer.

Exercise-1

Input : 
5

Output :
7
Exercise-2

Input:
10

Output:
11
"""

import sys
# Defining a function to calculate the clumsy factorial
def clumsy(n):
    # storing the operations in order in the stack
    clumsyoperations=["*","//","+","-"]
    # creating an empty expression string which will store the entire expression later
    expression=""
    for i in range(n):
        # adding the element in expression
        expression+=str(n-i)
        if i<n-1:# i<n-1 is checked so that the function doesnt add the operations after the last element 
            # adding the operation in the expression
            expression+=clumsyoperations[i%4]
    # printing the whole expression
    print(expression)
    # printing the evaluated expression result
    print(eval(expression))
    return


# Driver code
clumsy(5)
clumsy(10)

