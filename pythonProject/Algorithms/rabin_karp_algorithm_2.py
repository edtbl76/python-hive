def polynomial_hash(s):
    hash_value = 0
    for i in range(len(s)):
        hash_value += (ord(s[i]) * (26 ** (len(s) - i - 1)))
    return hash_value


def polynomial_rolling_hash(previous_hash, c1, c2, pattern_length):
    return (previous_hash - ord(c1) * (26 ** (pattern_length - 1))) * 26 + ord(c2)


def rabin_karp_algorithm_multiple(patterns, text):
    # Your code goes here
    pattern_hashes = dict()
    pattern_lengths = set()
    pattern_occurrences = dict()
    for patt in patterns:
        p_hash = polynomial_hash(patt)
        pattern_hashes[p_hash] = patt
        pattern_occurrences[patt] = 0
        pattern_lengths.add(len(patt))

    for pattern_length in pattern_lengths:
        substring_hash = polynomial_hash(text[:pattern_length])
        if substring_hash in pattern_hashes:
            this_pattern = pattern_hashes[substring_hash]
            pattern_occurrences[this_pattern] += 1

        for i in range(len(text) - pattern_length):
            previous_hash = substring_hash
            substring_hash = polynomial_rolling_hash(previous_hash, text[i], text[i + pattern_length], pattern_length)
            if substring_hash in pattern_hashes:
                this_pattern = pattern_hashes[substring_hash]
                pattern_occurrences[this_pattern] += 1
    return pattern_occurrences


patterns = ['ABC', 'BCD', 'CDE', 'DEF']
text = 'ABCBCDCDEDEF'
print(rabin_karp_algorithm_multiple(patterns, text))


def rabin_karp_algorithm_2D(pattern, text):
    # helpers
    m1 = len(pattern)
    m2 = len(pattern[0])
    n1 = len(text)
    n2 = len(text[0])
    occurrences = 0

    # combines individual 1D polynomial hash values of each row to use a
    # polynomial function.
    pattern_hash = 0
    for i in range(m1):
        pattern_hash += polynomial_hash(pattern[i]) * (10**(m1 - i - 1))


    all_hashes = [[0 for j in range(n2 - m2 + 1)] for i in range(n1)]
    for i in range(n1):
        substring_hash = polynomial_hash(text[i][:m2])
        all_hashes[i][0] = substring_hash

        for j in range(n2 - m2):
            previous_hash = substring_hash
            substring_hash = polynomial_rolling_hash(previous_hash, text[i][j], text[i][j + m2], m2)
            all_hashes[i][j + 1] = substring_hash


    for j in range(n2 - m2 + 1):
        column_hash = 0
        for i in range(m1):
            column_hash += all_hashes[i][j] * (10**(m1 - i - 1))
        if column_hash == pattern_hash:
            occurrences += 1

        for i in range(n1 - m1):
            previous_hash = column_hash
            column_hash = (previous_hash - all_hashes[i][j]*(10**(m1 - 1)))*10 + all_hashes[i + m1][j]
            if column_hash == pattern_hash:
                occurrences += 1
    return occurrences


# Your code goes here
pattern = ['ABC', 'GHI']
text = ['ABCDEF', 'GHIJKL', 'MNOPQR', 'STUVWX', 'YZABCD', 'EFGHIJ', 'KLMNOP']
print(rabin_karp_algorithm_2D(pattern, text))
