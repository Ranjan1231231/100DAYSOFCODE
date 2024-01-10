"""
You are given the root of a binary tree with unique values, and an integer start. At minute 0, an infection starts from the node with value start.

Each minute, a node becomes infected if:

The node is currently uninfected.
The node is adjacent to an infected node.
Return the number of minutes needed for the entire tree to be infected.

 

Example 1:


Input: root = [1,5,3,null,4,10,6,9,2], start = 3
Output: 4
Explanation: The following nodes are infected during:
- Minute 0: Node 3
- Minute 1: Nodes 1, 10 and 6
- Minute 2: Node 5
- Minute 3: Node 4
- Minute 4: Nodes 9 and 2
It takes 4 minutes for the whole tree to be infected so we return 4.
Example 2:


Input: root = [1], start = 1
Output: 0
Explanation: At minute 0, the only node in the tree is infected so we return 0.
 
"""
class Solution:
    def findNode(self, root, start):
        if root == None:
            return
        if root.val == start:
            return root
        else:
            return self.findNode(root.left, start) or self.findNode(root.right, start)

    def markParents(self, root, parentMap):
        queue = deque()
        queue.append(root)
        while queue:
            n = len(queue)
            for i in range(n):
                curr = queue.popleft()
                if curr.left != None:
                    parentMap[curr.left] = curr
                    queue.append(curr.left)
                if curr.right != None:
                    parentMap[curr.right] = curr
                    queue.append(curr.right)
        
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        # 1. Get the target Node first
        target = self.findNode(root, start)
        # 2. make the parentMap as done in previous question i.e all Nodes at distance k using the bfs traversal
        parentMap = defaultdict()   # {child : parent}
        self.markParents(root, parentMap)
        queue = deque()
        queue.append(target)
        visited = defaultdict()
        visited[target] = True
        time = 0
        # 3. use a second bfs traversal to mark them all as visited and each time increase the time += 1
        while queue:
            n = len(queue)
            
            for i in range(n):
                curr = queue.popleft()
                if curr.left != None and visited.get(curr.left) == None:
                    visited[curr.left] = True
                    queue.append(curr.left)
                if curr.right != None and visited.get(curr.right) == None:
                    visited[curr.right] = True
                    queue.append(curr.right)
                if parentMap.get(curr) != None and visited.get(parentMap.get(curr)) == None:
                    visited[parentMap.get(curr)] = True
                    queue.append(parentMap.get(curr))
            # 4. After marking all of them , time is incremented to 1
            time += 1
        
        # Since we dont count the target Node time so final time is decremented by 1
        return time - 1         
