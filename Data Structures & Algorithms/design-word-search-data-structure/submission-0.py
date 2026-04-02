class TrieNode:

    def __init__(self):
        self.children = {}
        self.endOfWord = False


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root

        for letter in word:
            if letter not in cur.children:
                cur.children[letter] = TrieNode()
            cur = cur.children[letter]

        cur.endOfWord = True
        
    def search(self, word: str) -> bool:

        def dfs(j, root):
            cur = root

            for i in range(j, len(word)):
                letter = word[i]
                if letter == '.':
                    for child in cur.children.values():
                        if dfs(i + 1, child): # skip the "."
                            return True
                    return False
                else:
                    if letter not in cur.children:
                        return False
                    cur = cur.children[letter]

            return cur.endOfWord

        return dfs(0, self.root)
        