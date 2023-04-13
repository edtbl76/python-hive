my_list = range(16)
print(filter(lambda x: x % 3 == 0, my_list))  # [0, 3, 6, 9, 12, 15]


languages = ["HTML", "JavaScript", "Python", "Ruby"]

# Add arguments to the filter()
print(filter(lambda x: x == "Python", languages))  # ['Python']

squares = [x ** 2 for x in range(1, 11)]
filt = filter(lambda x: 30 <= x <= 70, squares)
print(filt)   # [36, 49, 64]


# secret message
garbled = "IXXX aXXmX aXXXnXoXXXXXtXhXeXXXXrX sXXXXeXcXXXrXeXt mXXeXsXXXsXaXXXXXXgXeX!XX"

message = filter(lambda x: x != "X", garbled)
print(message) # I am another secret message!


