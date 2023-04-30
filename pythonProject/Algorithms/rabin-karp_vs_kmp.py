import time


def prefix_function(pattern):
    pi = [0 for i in range(len(pattern))]
    for i in range(1, len(pattern)):
        j = pi[i - 1]
        while j > 0 and pattern[i] != pattern[j]:
            j = pi[j - 1]
        if pattern[i] == pattern[j]:
            j += 1
        pi[i] = j
    return pi


def kmp_algorithm(pattern, text):
    m = len(pattern)
    n = len(text)
    pi = prefix_function(pattern)
    j = 0
    count = 0
    for i in range(n):
        while j > 0 and pattern[j] != text[i]:
            j = pi[j - 1]
        if pattern[j] == text[i]:
            j += 1
        if j == m:
            count += 1
            j = pi[j - 1]
    return count


def polynomial_hash(s):
    hash_value = 0
    for i in range(len(s)):
        hash_value += (ord(s[i]) * (26 ** (len(s) - i - 1)))
    return hash_value


def polynomial_rolling_hash(previous_hash, c1, c2, pattern_length):
    return (previous_hash - ord(c1) * (26 ** (pattern_length - 1))) * 26 + ord(c2)


def rabin_karp_algorithm(pattern, text):
    pattern_hash = polynomial_hash(pattern)
    occurrences = 0
    text_length = len(text)
    pattern_length = len(pattern)
    substring_hash = polynomial_hash(text[:pattern_length])
    if substring_hash == pattern_hash:
        occurrences += 1
    for i in range(text_length - pattern_length):
        previous_hash = substring_hash
        substring_hash = polynomial_rolling_hash(previous_hash, text[i], text[i + pattern_length], pattern_length)
        if substring_hash == pattern_hash:
            occurrences += 1
    return occurrences


pattern = ""
for i in range(1000):
    pattern += "A"
text = ""
for i in range(100000):
    text += "A"
start_time = time.time()
print("Matches found: ", rabin_karp_algorithm(pattern, text))
print("Rabin-Karp took %s seconds" % (time.time() - start_time))
start_time = time.time()
print("Matches found: ", kmp_algorithm(pattern, text))
print("KMP took %s seconds" % (time.time() - start_time))

pattern = "ababbabbabbababbabb"
text = 100000 * pattern
start_time = time.time()
print("Matches found: ", rabin_karp_algorithm(pattern, text))
print("Rabin-Karp took %s seconds" % (time.time() - start_time))
start_time = time.time()
print("Matches found: ", kmp_algorithm(pattern, text))
print("KMP took %s seconds" % (time.time() - start_time))
