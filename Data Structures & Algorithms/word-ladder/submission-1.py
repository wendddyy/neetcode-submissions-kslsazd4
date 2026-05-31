class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        wordSet = set(wordList)
        if endWord not in wordSet:
            return 0

        q = deque()
        q.append((beginWord, 1))

        visited = set()
        visited.add(beginWord)

        while q:
            cur, length = q.popleft()
            if cur == endWord:
                return length

            for i in range(len(cur)):
               for c in "abcdefghijklmnopqrstuvwxyz":
                word = cur[:i] + c + cur[i+1:]
                if word in wordSet and word not in visited:
                    visited.add(word)
                    q.append((word, length + 1))
        
        return 0

