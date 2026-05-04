# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        index_map = {v : i for i, v in enumerate(inorder)}

        def build(preL, preR, inL, inR):
            if preL > preR:
                return None

            rootVal = preorder[preL]
            root = TreeNode(rootVal)

            k = index_map[rootVal]
            left_size = k - inL

            root.left = build(preL + 1, preL + left_size, inL, k - 1)
            root.right = build(preL + left_size + 1, preR, k + 1, inR)

            return root

        return build(0, len(preorder) - 1, 0, len(inorder) - 1)