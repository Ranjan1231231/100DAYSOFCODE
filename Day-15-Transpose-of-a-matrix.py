"""
The transpose of a matrix is the matrix flipped over its main diagonal, switching the matrix's row and column indices.



 

Example 1:

Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[1,4,7],[2,5,8],[3,6,9]]
Example 2:

Input: matrix = [[1,2,3],[4,5,6]]
Output: [[1,4],[2,5],[3,6]]

"""


class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        # create an empty list for storing the result
        transposematrix=[]
        # selecting the number of rows for transpose matrix and iterating the main matrix
        for i in range(0,len(matrix[0])):
            # tempmatrix for creating the transpose entire row at a time
            tempmatrix=[]
            # selecting the column values for each row
            for k in range(0,len(matrix)):
                temp=matrix[k]
                tempmatrix.append(temp[i])
            transposematrix.append(tempmatrix)
        return transposematrix
