class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        order = {k : [] for k in range(numCourses)}
        for a, b in prerequisites:
            order[a].append(b)       
        visiting = set()
        finished = set()

        def dfs(course):
            if course in visiting:
                return False
            if course in finished:
                return True
            
            visiting.add(course)
            for nxt in order[course]:
                if not dfs(nxt):
                    return False
                
            visiting.remove(course)
            finished.add(course)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False

        return True

