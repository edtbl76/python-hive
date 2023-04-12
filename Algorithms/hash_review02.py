# Solving Hashing Collisions
# - using prime values to ensure a unique mapping
uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]


def prime_value(c):
    return prime_numbers[ord(c) - ord('A')]


# Checkpoint 1
prime_values = dict()
for c_u in uppercase:
    prime_values[c_u] = prime_value(c_u)
print(prime_values)


def prime_hash(s):
    hash_value = 1
    for c in s:
        hash_value *= prime_value(c)
    return hash_value

    # Checkpoint 2


prime_hash_values = dict()
for i in range(len(uppercase) - 3):
    inner_hash_value = 1
    substring = uppercase[i: i + 4]
    prime_hash_values[substring] = prime_hash(substring)
print(prime_hash_values)

# Checkpoint 3
# Better, but we still get matching hashes by reordering strings w/ the same
# characters (these should be unique) 
string1 = "AB"
string2 = "BA"
colliding_hash_values = {
    string1: prime_hash(string1),
    string2: prime_hash(string2)
}
print(colliding_hash_values)
