class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # use map, key: num, value: index
        visited = {}

        for i in range(len(nums)):
            if nums[i] in visited:
                if abs(i - visited[nums[i]]) <= k:
                    return True
                else:
                    visited[nums[i]] = i
            else:
                visited[nums[i]] = i
        
        return False