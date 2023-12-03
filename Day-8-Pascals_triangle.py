"""
Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it .

Example 1:

Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
Example 2:

Input: numRows = 1
Output: [[1]]
"""

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # creating a new row
        triangle = [[1]]
        # for loop from 1 to number of rows given
        for i in range(1,numRows): 
            #assigning the previous row in the triange to a variable
            prev_row = triangle[-1] 
            new_row = [1] 
            for j in range(1,i): 
                #add the two values eg if n=3 on third iteration of i this loop will execute twice and add the values 1+2 = 3, 2+1=3
                new_ele = prev_row[j-1] + prev_row[j] 
                #append the 1 to the end of the row 
                new_row.append(new_ele) 
            new_row.append(1) 
            triangle.append(new_row) 
        return triangle

            
