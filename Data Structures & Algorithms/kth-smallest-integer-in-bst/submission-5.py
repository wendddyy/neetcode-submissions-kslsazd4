# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # max heap of size k
        # use negative number

        heap = []
        queue = deque()

        queue.append(root)
        while queue:
            cur = queue.popleft()
            if len(heap) < k:
                heapq.heappush(heap, -cur.val)
            elif cur.val < -heap[0]:
                heapq.heappop(heap)
                heapq.heappush(heap, -cur.val)

            if cur.left:
                queue.append(cur.left)
            if cur.right:
                queue.append(cur.right)
            
        return -heap[0]


        