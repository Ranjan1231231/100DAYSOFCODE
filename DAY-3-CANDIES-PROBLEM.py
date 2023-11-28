'''Candies
You have a collection of candies, and each candy has a certain sweetness value. Your goal is to combine the candies to create new candies until you reach a specific target sweetness level. Find how many steps need to reach candies sweetness target.
To achieve this, you can select any two candies with the least sweetness and combine them into a new candy with sweetness calculated as follows:
sweetness = (least sweet candy + 2 * second least sweet candy)
For example, consider the following scenario:
You are given a target sweetness level of 12, and you have the following candies: [2, 8, 3, 7, 4, 6]. To reach the target sweetness of 12.
you can perform the following steps:
Ascending order = 2,3,4,6,7,8
Combine the two least sweet candies: 2 + 2*3 = 8. Updated candies: [ 8, 4, 6, 7, 8].
Combine the two least sweet candies: 4 + 2*6 = 16. Updated candies: [8, 16, 7, 8].
Combine the two least sweet candies: 7 + 2*8 = 23. Updated candies: [8,16,23].
Combine the two least sweet candies: 8 + 2*16 = 17. Updated candies: [40,23].
The sweetness of the first candy in the updated candies array is now 40, which exceeds the target sweetness of 12.
Exercise-1
Input:
7
1 2 3 4 5
Note:
Line 1 : Target of the sweetness
Line 2 Each candies sweetness
output:
3
Exercise-2
input:
11
2 5 3 7 6 1
output:
4'''


import sys
#defining a function to calculate the sweetness of two candies 
def sweetness(candy1,candy2):
    return min(candy1,candy2)+2*(max(candy1,candy2))
    
candyarray=[2,5,3,7,6,1]
desired_sweetness=11
steps=0
# sorting the array for first while loop
candyarray.sort()
# after sorting if the least sweetness is less than the desired_sweetness then add the least two sweetness candy
while candyarray[0] < desired_sweetness:
    # increment the step each time two candies are added
    steps += 1
    # since the candy array is sorted , the least two candies should be at first and seconf position of the array
    candy1,candy2  = candyarray[0],candyarray[1]
    # removing the least two candies since it has to be replaced by their added sweetness
    candyarray.pop(1)
    candyarray.pop(0)
    candyarray.append(sweetness(candy1,candy2))
    # sorting the candyarray after adding the least two sweetness candy so that the loop can check the least value will be checked by the loop when it runs again
    candyarray.sort()
        
print("The total number of steps until all the candies are above the desired sweetness are : " , steps)
