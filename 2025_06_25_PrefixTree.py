class TrieNode:
    def __init__(self):
        self.tree_map = {} # "a" = TrieNode
        self.end_of_word = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:

        curr = self.root

        for c in word:
            if c not in curr.tree_map:
                curr.tree_map[c] = TrieNode()
            
            curr = curr.tree_map[c]

        curr.end_of_word = True
                

    def search(self, word: str) -> bool:
        curr = self.root

        for c in word:
            if c not in curr.tree_map:
                return False
            
            curr = curr.tree_map[c]

        return curr.end_of_word
        

    def startsWith(self, prefix: str) -> bool:
        curr = self.root

        for c in prefix:
            if c not in curr.tree_map:
                return False
            
            curr = curr.tree_map[c]

        return True


        



