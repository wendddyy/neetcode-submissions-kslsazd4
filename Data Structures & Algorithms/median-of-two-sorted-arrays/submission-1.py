class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        A, B = nums1, nums2
        if len(A) < len(B):
            A, B = B, A
        
        half = (len(A) + len(B))//2
        left = 0
        right = len(A)

        while True:
            i = (left + right) // 2
            j = half - i

            A_left = A[i - 1] if i > 0 else float('-inf')
            A_right = A[i] if i < len(A) else float('inf')
            B_left = B[j - 1] if j > 0 else float('-inf')
            B_right = B[j] if j < len(B) else float('inf')

            if A_left <= B_right and B_left <= A_right:
                if (len(A) + len(B)) % 2 != 0:
                    return min(A_right, B_right)
                else:
                    return (max(A_left, B_left) + min(A_right, B_right)) / 2
            elif A_left > B_right:
                right = i - 1
            else:
                left = i + 1