uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def polynomial_hash(s):
    hash_value = 0
    for i in range(len(s)):
        hash_value += (ord(s[i]) * (26 ** (len(s) - i - 1)))
    return hash_value


# Checkpoint 1
polynomial_hash_ABCD = polynomial_hash('ABCD')
rolling_hash_BCDE = polynomial_hash_ABCD - polynomial_hash('A') + polynomial_hash('E')
polynomial_hash_BCDE = polynomial_hash('BCDE')

print(rolling_hash_BCDE)
print(polynomial_hash_BCDE)

# Checkpoint 2
polynomial_hash_ABCD = polynomial_hash('ABCD')
rolling_hash_BCDE = (polynomial_hash_ABCD - ord('A') * (26 ** 3)) * 26 + ord('E')
polynomial_hash_BCDE = polynomial_hash('BCDE')

print(rolling_hash_BCDE)
print(polynomial_hash_BCDE)


# Checkpoint 3
def polynomial_rolling_hash(s, H, c):
    return (H - ord(s[0]) * 26 ** (len(s) - 1)) * 26 + ord(c)


# Checkpoint 4
s = 'ABCD'
H = polynomial_hash(s)
polynomial_rolling_hash_values = {s: H}
for c in uppercase[4:]:
    H = polynomial_rolling_hash(s, H, c)
    s = s[1:] + c
    polynomial_rolling_hash_values[s] = H
print(polynomial_rolling_hash_values)
