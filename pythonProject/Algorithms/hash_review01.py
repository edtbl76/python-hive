uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
ascii_values = dict()
for c in uppercase:
    ascii_values[c] = ord(c)
print(ascii_values)


# Checkpoint 1
def ascii_hash(s):
    inner_hash_value = 1
    for s_c in s:
        inner_hash_value *= ord(s_c)
    return inner_hash_value


# Checkpoint 2
ascii_hash_values = dict()
for i in range(len(uppercase) - 3):
    hash_value = 1
    substring = uppercase[i: i + 4]
    ascii_hash_values[substring] = ascii_hash(substring)
print(ascii_hash_values)

# Checkpoint 3
string1 = 'AT'
string2 = 'NF'
colliding_hash_values = {string1: ascii_hash(string1), string2: ascii_hash(string2)}
print(colliding_hash_values)
