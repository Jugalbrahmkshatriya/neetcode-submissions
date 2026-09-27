# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Base Case: If the tree is empty, return an empty list immediately
        if not root:
            return []
        
        result = []
        # Use a double-ended queue (deque) for O(1) pops from the left side
        queue = collections.deque([root])
        
        # Continue traversing as long as there are nodes in the queue
        while queue:
            # Snapshot the number of nodes at the current level
            level_size = len(queue)
            current_level = []
            
            # Process exactly all nodes that belong to this current level
            for k in range(level_size):
                # Remove the leftmost node from the queue
                node = queue.popleft()
                current_level.append(node.val)
                
                # Add child nodes to the back of the queue for the next level
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            # Add the completed level list to our final answer
            result.append(current_level)
            
        return result