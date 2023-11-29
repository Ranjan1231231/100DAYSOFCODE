"""
Problem Statement
Mix the array
Given a 1-indexed array initially filled with zeros and a list of operations, perform each operation by adding a value to each element of the array between two given indices (inclusive). After performing all operations, find and return the maximum value in the array.

For example, let's consider the following scenario:
q = {[2,4,5],[3,6,3],[1,7,10]}
Initial Array size = 7

Array: [0, 0, 0, 0, 0, 0, 0]

Operations:

Add 5 between indices 2 and 4: [0, 5, 5, 5, 0, 0, 0]
Add 3 between indices 3 and 6: [0, 5, 8, 8, 3, 3, 0]
Add 10 between indices 1 and 7: [10, 15, 18, 18, 13, 13, 10]
In this scenario, the maximum value in the array is 18.

Important Note: Ensure that you save your solution before progressing to the next question and before submitting your answer.

Exercise-1

Input:

5
3
2 4 3
4 5 9
3 3 11

Output:
14

Note:
Line -1 : array size
Line -2 : query count

Exercise-2

Input:

10
3
3 10 3
4 5 9
2 9 11

Output:
23
"""

import sys
# Defining the array manupulation function
def arraymanupulation(arraysize,query):
    # set initial array to empty and add 0 according to the given array size
    initialarray=[]
    for i in range(arraysize):
        initialarray.append(0)
    # this for  loop selects the elements in the q i.e is q=[[2,4,5],[3,6,3]] it selects [2,4,5] and store it in variable i
    for i in query:
        # this for loop iterates k from the first element in i to the second element in i  and save it as variable k
        for k in range(i[0]-1,i[1]):
            # adding the third value of i to the k'th position in the initialarray
            initialarray[k]+=i[2]
            
    # displaying the result
    print(max(initialarray))
    return

# Driver code

arraysize=7
query=[[2,4,5],[3,6,3],[1,7,10]]
arraymanupulation(arraysize,query)

# EX-1
arraysize=5
query=[[2,4,3],[4,5,9],[3,3,11]]
arraymanupulation(arraysize,query)

# EX-2
arraysize=10
query=[[3,10,3],[4,5,9],[2,9,11]]
arraymanupulation(arraysize,query)
                                                                                                                            
