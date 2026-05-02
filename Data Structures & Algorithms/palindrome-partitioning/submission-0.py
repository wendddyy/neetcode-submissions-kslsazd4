class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        path = []

        def isPalindrome(sub):
            return sub == sub[::-1]
        
        def dfs(start):
            if start == len(s):
                res.append(path[:]) # why cant directly append path?
                return 
            
            for end in range(start + 1, len(s) + 1): # why range is from start+1? what if there is 1 element?
                sub = s[start:end]
                
                if isPalindrome(sub):
                    path.append(sub)
                    dfs(end)
                    path.pop()
        dfs(0)
        return res


            
        