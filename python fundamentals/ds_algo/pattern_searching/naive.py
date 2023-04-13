# Define pattern_search
def pattern_search(my_text, my_pattern):
    print(my_text)
    print(my_pattern)
    for index in range(0, len(my_text) - 1):
        print(f"Text Index: {index}")
        match_count = 0
        for char in range(0, len(my_pattern) - 1):
            print(f'Pattern Index: {char}')
            if my_pattern[char] == my_text[index + char]:
                print("Matching Index Found")
                print(f"Match Count: {match_count}")
                match_count += 1
            else:
                break

        if match_count == len(my_pattern):
            print(f'{pattern} found at index {index}')


text = "HAYHAYNEEDLEHAYHAYHAYNEEDLEHAYHAYHAYHAYNEEDLE"
pattern = "NEEDLE"
# Invoke pattern_search
pattern_search(text, pattern)

# New inputs to test
text2 = "SOMEMORERANDOMWORDSTOpatternSEARCHTHROUGH"
pattern2 = "pattern"
text3 = "This   still      works with    spaces"
pattern3 = "works"
text4 = "722615457824612704202682179992552072047396"
pattern4 = "42"

pattern_search(text2, pattern2)
pattern_search(text3, pattern3)
pattern_search(text4, pattern4)
