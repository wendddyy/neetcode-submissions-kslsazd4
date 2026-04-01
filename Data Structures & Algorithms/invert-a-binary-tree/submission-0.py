# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # use recursion
        # base case: when the function stops
        if root is None:
            return None
        
        # recursive case:
        left_val = self.invertTree(root.left)
        right_val = self.invertTree(root.right)

        root.left = right_val
        root.right = left_val

        return root