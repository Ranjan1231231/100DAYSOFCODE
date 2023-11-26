import sys

#this function checks if there is any duplicate value in the row or nor
def rowchecking(arr,row):
    temp=set()#to store all the values checked so far
    for i in range(0,9):
        #if already incountered return false
        if arr[row][i] in temp:
            return False
        #if the value is not a empty cell insert it into the temp
        if arr[row][i]!='.':
            temp.add(arr[row][i])
    return True
    
#checking if there is a duplicate value in the column or not
def columnchecking(arr,col):
    temp=set()
    for i in range(0,9):
        #if already encountered return false
        if arr[i][col] in temp:
            return False
        # if it is not empty cell and not present in temp put it in temp
        if arr[i][col]!='.':
            temp.add(arr[i][col])
    return True

#checking for duplicate values in 3X3 matrix
def checkbox(arr,startrow,startcolumn):
    temp=set()
    for row in range (0,3):
        for col in range (0,3):
            curr=arr[row+startrow][col+startcolumn]
            # if already encountered return false
            if curr in temp:
                return False
            
            #if not add to temp except empty box
            if curr!='.':
                temp.add(curr)
    return True

#checking if all is valid or not
def isvalid(arr,row,col):
    return(rowchecking(arr,row) and columnchecking(arr,col) and checkbox(arr,row-row%3,col-col%3))

def isvalidconfig(arr,n):
    for i in range(0,n):
        for j in range(0,n):
            if not isvalid(arr,i,j):
                return False
    return True


#drivercode
board=[['5', '3' ,'.', '.', '7' ,'.', '.', '.', '.'],
        ['6', '.', '.', '1', '9', '5', '.', '.', '.'],
        ['.', '9', '8', '.', '.', '.', '.', '6', '.'],
        ['8', '.', '.', '.', '6', '.', '.', '.', '3'],
        ['4', '.', '.', '8', '.', '3', '.', '.', '1'],
        ['7', '.', '.', '.', '2', '.', '.', '.', '6'],
        ['.', '6', '.', '.', '.', '.', '2', '8', '.'],
        ['.', '.' ,'.', '4', '1', '9', '.', '.', '5'],
        ['.', '.', '.', '.', '8', '.', '.', '7', '9']]
if isvalidconfig(board,9):
    print("YES")
else:
    print("NO")
                                                                                                                            
