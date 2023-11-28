"""
Problem Statement
Check string prefix
You are given a list of passwords, where each password consists of lowercase letters from 'a' to 'z' inclusive. The set of passwords is said to be a 'GOOD PASSWORD' if no password is a prefix of another password in the set, except for identical passwords (which are considered prefixes of each other). In this case, print 'GOOD PASSWORD'. Otherwise, print 'BAD PASSWORD' on the first line, followed by the first pair of passwords where one password is a prefix of the other.
Consider the following list of words: ['apple', 'banana', 'application', 'bananas'].
In this case, the word 'banana' is a prefix of 'bananas'.

So we would print: 'BAD PASSWORD'

Now let's take another example with a different set of words: ['cat', 'dog', 'elephant']. In this scenario, none of the strings are prefixes of each other.

Therefore, we can conclude that: GOOD PASSWORD

Exercise-1

Input:
abc zxy pqr

Output:
GOOD PASSWORD
Exercise-2

Input:
abc abczxy abcpqr

Output:
BAD PASSWORD
"""


import sys
#defining the password checking function
def passwordchecking(password):
    # setting badpassword count to 0 when it reaches one the program breaks
    badpassword=0
    #storing the first bad password pair in the array
    passwordpair=[]
    
    for i in password :
        # making a copy of the password array to remove the current selected password and to match it with other passwords
        temp_password = password.copy ( )
        temp_password.remove ( i )
        for j in temp_password :
            a = str ( i ).lower ( )
            b = str ( j ).lower ( )
            # if one password string is in onther password string then that password bad password will increment by one and the loop will break
            if a in b :
                badpassword +=1
                passwordpair.append(a)
                passwordpair.append(b)
                break
    if badpassword >=1:
        print("BAD PASSWORD")
        return passwordpair
    else:
        return "GOOD PASSWORD"
        


password=["mango","banana","leechi","mangoes"]
print(passwordchecking(password),"\n")

password=["abc","zxy","pqr"]
print(passwordchecking(password),"\n")

password=["abc" ,"abczxy", "abcpqr"]
print(passwordchecking(password),"\n")
