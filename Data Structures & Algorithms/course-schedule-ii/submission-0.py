class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        res = []
        graph = {k:[] for k in range(numCourses)}        
        for a, b in prerequisites:
            graph[b].append(a)
        
        visiting = set()
        finished = set()
        
        def dfs(course):
            if course in visiting:
                return False
            if course in finished:
                return True

            visiting.add(course)
            for nxt in graph[course]:
                if not dfs(nxt):
                    return False
            visiting.remove(course)
            finished.add(course)
            res.append(course)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return []
            
        return res[::-1]




        