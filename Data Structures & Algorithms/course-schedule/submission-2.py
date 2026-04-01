class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # dfs + set + if cycle

        # corner
        if not prerequisites:
            return True
        
        graph = {i : [] for i in range(numCourses)}
        for a, b in prerequisites:
            graph[a].append(b)
        visiting = set()
        finished = set()

        #dfs
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
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True