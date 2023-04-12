from Trie import Trie

# Checkpoint 1
trie = Trie()
# Checkpoint 2
words = ["AMBER", "ALICE", "AMPLE", "BALLOON", "BALL", "BLAST", "BAND", "DENSE", "DUTCH", "DECK", "DANCE", "DRAMA",
         "MESS", "MAVERICK", "MAVEN", "PHYSICS", "PHONE", "PHANTOM", "PASS", "PEAK", "PACK", "ZEST", "ZEAL", "ZAP",
         "ZIP", "ZIPPER"]

for word in words:
    trie.add_string(word)
# Checkpoint 3
more_words = ["APPLE", "AMPLIFIER", "AMPLE", "BALLOON", "BALL", "DART", "DUTCH", "DECK", "DRAM", "FLAG", "MOP",
              "MAVERICK", "MANSION", "PHYSICS", "PHONE", "PHANTOM", "PASS", "PECK", "PAIN", "ZAM", "ZEST", "ZAP", "ZIP",
              "ZEBRA"]

for word in more_words:
    if trie.search_string(word):
        print(word)
# Checkpoint 4

prefixes = ["A", "AM", "B", "BALL", "BA", "C", "CA" "DUTCH", "DECK", "GA", "J", "MA", "P", "PH", "PE", "Z", "ZIP"]

for prefix in prefixes:
    print(trie.count_prefix(prefix))
