# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
               # bfs
               # corner
            if not root:
                return []
            res = []
            heap = deque([root])
            while heap:
                size = len(heap)
                curL = []
                for i in range(size):
                    cur = heap.popleft()
                    if cur.left:
                        heap.append(cur.left)
                    if cur.right:
                        heap.append(cur.right)
                    curL.append(cur.val)
                res.append(curL)

            return res
                    


