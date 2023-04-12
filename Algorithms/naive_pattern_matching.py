def naive_pattern_matching(pattern, text):
    pattern_length = len(pattern)
    text_length = len(text)
    occurrences = 0

    # There are text_length - pattern_length + 1 substrings in `text` that
    # are equal in length to `pattern`
    #   - in order to check for a match, we have to iterate over all char indexes in
    #   - text that range from index 0 up to (noninclusive) text_length - pattern_length + 1
    for i in range(text_length - pattern_length + 1):
        pattern_match = True

        # here we iterate over the length of substrings that are equal in length to the pattern_length
        # if any char in the pattern doesn't equal the char at the corresponding index in the substring we
        # are iterating over, then we set 'match' to false and break out of the loop.
        for j in range(pattern_length):
            if pattern[j] != text[i + j]:
                pattern_match = False
                break

        # for every match, we increment occurrences.
        if pattern_match:
            occurrences += 1


pattern = 1000*'A'
text = 100000*'A'
print(naive_pattern_matching(pattern, text))