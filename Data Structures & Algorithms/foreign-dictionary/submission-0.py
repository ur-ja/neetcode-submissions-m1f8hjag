class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj= {char: set() for word in words for char in word}

        for i in range(len(words) - 1):
            word1, word2 = words[i], words[i + 1]
            minLength = min(len(word1), len(word2))
            if len(word1) > len(word2) and word1[:minLength] == word2[:minLength]:
                return ""
            for j in range(minLength):
                if word1[j] != word2[j]:
                    adj[word1[j]].add(word2[j])
                    break

        visited = {} # if in list and false then not in path but has been visited if in list and true means cycle

        res = []

        def dfs(node):
            if node in visited:
                return visited[node]

            visited[node] = True

            for neighbour in adj[node]:
                if dfs(neighbour):
                    return ""

            visited[node] = False

            res.append(node)

        for char in adj:
            if dfs(char):
                return ""

        res.reverse()
        return "".join(res)

