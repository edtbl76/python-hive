class TrieNode:
    def __init__(self):
        self.nodes = {}
        self.end_of_key =  False
        self.freq = 0


    def add_char(self, c: chr):
        if c not in self.nodes:
            self.nodes[c] = TrieNode()
        return self.nodes[c]
