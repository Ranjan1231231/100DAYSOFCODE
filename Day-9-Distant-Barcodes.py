"""
In a warehouse, there is a row of barcodes, where the ith barcode is barcodes[i].

Rearrange the barcodes so that no two adjacent barcodes are equal. You may return any answer, and it is guaranteed an answer exists.

 

Example 1:

Input: barcodes = [1,1,1,2,2,2]
Output: [2,1,2,1,2,1]
Example 2:

Input: barcodes = [1,1,1,1,2,2,3,3]
Output: [1,3,1,3,1,2,1,2]
 
"""


class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        resultlist=[]
        counts=collections.Counter(barcodes)
        heap=[[-v,k] for k ,v in counts.items()]
        heapq.heapify(heap)
        item=heapq.heappop(heap)
        while heap:
            resultlist.append(item[1])
            item[0]+=1
            item = heapq.heapreplace(heap, [item[0], item[-1]]) if item[0] < 0 else heapq.heappop(heap)
        resultlist.append(item[1])
        return resultlist

            
