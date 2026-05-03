# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # corner case

        def backTracking(tree1, tree2):
            if not tree1 and not tree2:
                return True
            if not tree1 or not tree2:
                return False

            if tree1.val != tree2.val:
                return False

            return backTracking(tree1.left, tree2.left) and backTracking(tree1.right, tree2.right)

        return backTracking(p, q)
        