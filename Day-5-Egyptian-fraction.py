"""
Problem Statement
Egyptian Fraction
You are an ancient Egyptian mathematician, and you have been tasked with representing the fraction 6/14 as a sum of unique unit fractions. You know that a unit fraction is a fraction with a numerator of 1 and a denominator of a positive integer. You also know that the sum of any number of unit fractions is always a rational number.

Example:

The first step is to find the largest possible unit fraction that is less than or equal to 6/14. This fraction is 1/3. The remaining fraction is 6/14 - 1/3 = 4/42. The largest possible unit fraction that is less than or equal to 4/42 is 1/11. The remaining fraction is 4/42 - 1/11 = 1/231.

Therefore, the Egyptian fraction representation of 6/14 is 1/3 + 1/11 + 1/231.

Exercise-1

Input:
6
14

Output:
3
11
231

Exercise-2

Input:
3
4

Output:
2
4
"""
import sys
import math #importing math to use ceil function
# function for egyptian fraction
def egyptianFraction(nr, dr): #nr-numerator,dr-denominator
    print("The Egyptian Fraction " +
          "Representation of {0}/{1} is".
                format(nr, dr), end="\n")
 
    # empty list ef to store denominator
    ef = []
 
    # while loop runs until fraction becomes 0 i.e, numerator becomes 0
    while nr != 0:
 
        # taking ceiling
        x = math.ceil(dr / nr)
 
        # storing value in ef list
        ef.append(x)
 
        # updating new nr and dr
        nr = x * nr - dr
        dr = dr * x
 
    # printing the values
    print(ef)
    
    
# Driver code
# EX-1
egyptianFraction(6, 14)

# EX-2
egyptianFraction(3,4)
                                                                                                                            
