class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False

    def addWord(self, word):
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.isWord = True


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        root = TrieNode()
        for word in words:
            root.addWord(word)

        rows, cols = len(board), len(board[0])
        res, visit = set(), set()

        def dfs(row, col, curr, word):
            if (row < 0 or col < 0 or row >= rows or col >= cols or (row, col) in visit or 
                board[row][col] not in curr.children):
                return 

            visit.add((row, col))
            curr = curr.children[board[row][col]]
            word += board[row][col]

            if curr.isWord:
                res.add(word)

            dfs(row + 1, col, curr, word)
            dfs(row, col + 1, curr, word) 
            dfs(row - 1, col, curr, word) 
            dfs(row, col - 1, curr, word) 

            visit.remove((row, col))

        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root, "")

        return list(res)




        


        