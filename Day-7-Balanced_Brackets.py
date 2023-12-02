"""
You are given a set of strings, each consisting of brackets (, ), {, }, [, or ]. A bracket is considered an opening bracket if it is one of (, {, or [, and it is considered a closing bracket if it is one of ), }, or ].

A string of brackets is considered balanced if it meets the following conditions:

It contains no unmatched brackets.
For every opening bracket, there is a corresponding closing bracket of the same type, and the brackets are properly nested.

Your task is to determine, for each given string, whether it is balanced or not. If a string is balanced, output "YES"; otherwise, output "NO".

Important Note: Ensure that you save your solution before progressing to the next question and before submitting your answer.

Exercise-1
input:
{[()]},{[(])},{{[[(())]]}}

Output:
YES
NO
YES

Exercise-2
input:
[],{},(),[}
Output:
YES
YES
YES
NO
"""

import sys
def balancedbrackets ( string ) :
    temparr = [ ]
    for i in string :
        if i == "(" or i == "{" or i == "[" :
            temparr.append ( i )
        elif i == ")":
            if temparr [ -1 ] == "(" :
                temparr.pop ( )
        elif i == "}" :
            if temparr [ -1 ] == "{" :
                temparr.pop ( )
        elif i == "]" :
            if temparr [ -1 ] == "[" :
                temparr.pop ( )
    if len(temparr)==0:
        return "YES"
    else:
        return "NO"


print ( balancedbrackets ( "{([])}" ) )
print ( balancedbrackets ( "{][}" ) )
    

