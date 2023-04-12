def polynomial_hash(substring):
    hash_value = 0
    for i in range(len(substring)):
        hash_value += (ord(substring[i]) * (26 ** (len(substring) - i - 1)))
    return hash_value


def polynomial_rolling_hash(substring, polynomial_hash_value, next_character):
    return (polynomial_hash_value - ord(substring[0]) * 26 ** (len(substring) - 1)) * 26 + ord(next_character)


def rabin_karp_algorithm(pattern, text):
    pattern_length = len(pattern)
    occurrences = 0
    substring = text[: pattern_length]
    substring_hash = polynomial_hash(substring)
    pattern_hash = polynomial_hash(pattern)
    if pattern_hash == substring_hash:
        occurrences += 1
    for character in text[pattern_length:]:
        substring_hash = polynomial_rolling_hash(substring, substring_hash, character)
        substring = substring[1:] + character
        if pattern_hash == substring_hash:
            occurrences += 1
    return occurrences


pattern = 1000*'A'
text = 100000*'A'
print(rabin_karp_algorithm(pattern, text))

