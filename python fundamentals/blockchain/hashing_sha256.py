# import sha256
from hashlib import sha256
# text to hash
text = "I am excited to learn about blockchain"

# print result
hash_result = sha256(text.encode())
print(hash_result.hexdigest())

text += "!"
hash_result = sha256(text.encode())
print(hash_result.hexdigest())


# OUTPUT
# 6866cb54011a5562052b7dbce8d7afa26195cbb7a73c3e70a56dc1a25d6df831
# 32ad45b332a7e5869d6d5aac178a1af413b04b206047709ea021df8d4d21ff56

