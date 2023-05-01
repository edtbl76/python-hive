# Write your count_multi_char_x function here:
def count_multi_char_x(word, x):
  # split the word based on the input
  splits = word.split(x)
  print(splits)
  #
  # We will return 1 more element
  # than there was substring
  #
  return (len(splits) - 1)
  

# Uncomment these function calls to test your function:
print(count_multi_char_x("mississippi", "iss"))
# should print 2
print(count_multi_char_x("apple", "pp"))
# should print 1
