"""
You are given the array paths, where paths[i] = [cityAi, cityBi] means there exists a direct path going from cityAi to cityBi. Return the destination city, that is, the city without any path outgoing to another city.

It is guaranteed that the graph of paths forms a line without any loop, therefore, there will be exactly one destination city.

 

Example 1:

Input: paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]
Output: "Sao Paulo" 
Explanation: Starting at "London" city you will reach "Sao Paulo" city which is the destination city. Your trip consist of: "London" -> "New York" -> "Lima" -> "Sao Paulo".
Example 2:

Input: paths = [["B","C"],["D","B"],["C","A"]]
Output: "A"
Explanation: All possible trips are: 
"D" -> "B" -> "C" -> "A". 
"B" -> "C" -> "A". 
"C" -> "A". 
"A". 
Clearly the destination city is "A".
Example 3:

Input: paths = [["A","Z"]]
Output: "Z"
 
"""

class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        dict={}
        # for counting the individual elements , since there will be only one mentions of starting and ending element 
        for i in paths:
            for j in i:
                if j not in dict:
                    dict[j]=0
                    dict[j]+=1
                    # print(dict)
                elif j in dict:
                    dict[j]+=1
                    # print(dict)
        # storing the key whose value is one i.e starting and ending
        keys = [key for key, value in dict.items() if value == 1]
        # returning the key value who occured in only 2 position in an element since the destination has to be a second charater of the one of the elemnts in the list
        for i in keys:
            for j in paths:
                if j[1]==i:
                    return i
