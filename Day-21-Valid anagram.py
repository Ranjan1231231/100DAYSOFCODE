"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
 
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # dictonary for storing the first string chracters and their number of occurances
        dict={}
         # dictonary for storing the second string chracters and their number of occurances
        dict1={}
        # for storing the alphabets and their no of occurances in their respective dictionary
        for i in s:
            if i not in dict:
                dict[i]=0
                dict[i]+=1
            elif i in dict:
                dict[i]+=1
        for j in t:
            if j not in dict1:
                dict1[j]=0
                dict1[j]+=1
            elif j in dict1:
                dict1[j]+=1
        # returning if dictonary 1= dictonary
        return dict1==dict



"""
another way 
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        ssort = ''.join ( sorted ( s ) )
        tsort = ''.join ( sorted ( t ) )
        if ssort!=tsort:
            return False
        else:
            return True


"""
