from DataStructures.TrieNode import TrieNode

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def add_string(self, word: str) -> None:
        nxt = self.root
        for i in word:
            nxt = nxt.add_char(i)
            nxt.freq += 1
        nxt.end_of_key = True

    def search_string(self, string: str) -> bool:
        nxt = self.root
        for i in string:
            if i not in nxt.nodes:
                return False
            nxt = nxt.nodes[i]
        return nxt.end_of_key


    def count_prefix(self, prefix: str) -> int:
        nxt = self.root
        for i in prefix:
            if i not in nxt.nodes:
                return 0
            nxt = nxt.nodes[i]
        return nxt.freq
