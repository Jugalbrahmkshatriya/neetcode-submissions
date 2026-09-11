# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            left_height = dfs(node.left)
            if left_height == -1:
                return -1  # Left subtree is already unbalanced
            right_height = dfs(node.right)
            if right_height == -1:
                return -1  # Right subtree is already unbalanced
            # If height difference exceeds 1, this node is unbalanced
            if abs(left_height - right_height) > 1:
                return -1
            # Return actual height of current node
            return 1 + max(left_height, right_height)
        return dfs(root) != -1