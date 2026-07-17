class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        neighbours = collections.defaultdict(list)
        wordList.append(beginWord)

        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j + 1:]
                neighbours[pattern].append(word)

        visited = set([beginWord])
        level = 1
        q = collections.deque([beginWord])

        while q:
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return level
                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j + 1:]
                    for nei in neighbours[pattern]:
                        if nei not in visited:
                            visited.add(nei)
                            q.append(nei)

            level += 1


        return 0
