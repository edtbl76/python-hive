doubles_by_3 = [x * 2 for x in range(1, 6) if (x * 2) % 3 == 0]

# Complete the following line. Use the line above for help.
even_squares = [x ** 2 for x in range(1,12) if (x ** 2) % 2 == 0]

print(doubles_by_3)
print(even_squares)

cubes_by_four = [x ** 3 for x in range(1, 11) if (x ** 3) % 4 == 0]
print(cubes_by_four)

l = [i ** 2 for i in range(1, 11)]
# Should be [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

print(l[2:9:2])

# print odds
my_list = range(1, 11) # List of numbers 1 - 10

#odds
print(my_list[::2])

# Backwards
backwards = my_list[::-1]

# Backwards By Ten
to_one_hundred = range(101)
# Add your code below!
backwards_by_tens = to_one_hundred[::-10]
print(backwards_by_tens)

# slicing
to_21 = range(1,22)
odds = to_21[::2]
middle_third = to_21[7:14]


threes_and_fives = [x for x in range(1, 16) if x % 3 == 0 or x % 5 == 0]
print(threes_and_fives) # [3, 5, 6, 9, 10, 12, 15]


# Slicing and reversing to decade a message
garbled = "!XeXgXaXsXsXeXmX XtXeXrXcXeXsX XeXhXtX XmXaX XI"
message = garbled[::-2]
print(message) # I am the secret message!



