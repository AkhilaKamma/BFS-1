#Time Compelxity: O(N) - You are visiting each node only once
#Space Complexity: O(N) - If it s complete binary tree in worst case N/2 leaf nodes in queue O(N/2)~ O(N)
from collections import deque
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        #first take a empty queue
        #empty result list
        result = []

        if root is None:
            return result
        
        queue = deque()
        queue.append(root)
        
        while queue:
            len_queue = len(queue)
            inter_list = []
            while len_queue > 0:
                node = queue.popleft()
                inter_list.append(node.val)
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
                len_queue -= 1

            result.append(inter_list)
                
    
        return result
            

#Level order using DFS:

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        #first take a empty queue
        #empty result list
        self.result = []

        def dfs(node, level):
            if not node:
                return

            # If this level doesn't exist in result, create a sublist
            if level == len(self.result):
                self.result.append([])

            # Append current node's value to its corresponding level
            self.result[level].append(node.val)

            # Recurse left and right
            dfs(node.left, level + 1)
            dfs(node.right, level + 1)

        dfs(root, 0)
        return self.result


        
        
        