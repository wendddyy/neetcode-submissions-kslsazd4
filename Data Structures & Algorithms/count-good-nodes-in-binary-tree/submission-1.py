# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(root, cur):
            if root == None:
                return 0

            count = 0
            if root.val >= cur:
                count = 1
                cur = root.val
            left = dfs(root.left, cur)
            right = dfs(root.right, cur)
            return left + right + count
        
        return dfs(root, root.val)
            
