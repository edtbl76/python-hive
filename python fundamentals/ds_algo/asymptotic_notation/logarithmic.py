def count(N):
    count = 0
    while N > 1:
        N = N // 2
        count += 1
    return count


# 1 = 1, exit (count = 0)
num_iterations_1 = 0  # REPLACE
print("The while loop performs {0} iterations when N is 1".format(num_iterations_1))

# 2 > 1, 2 // 2 = 1, (count = 1)
# 1 = 1 (count = 0)
num_iterations_2 = 1  # REPLACE
print("\nThe while loop performs {0} iterations when N is 2".format(num_iterations_2))

# 4 > 1, 4 // 2 = 2 (count = 1)
# 2 (we already know what this does) (count = 2)
num_iterations_4 = 2  # REPLACE
print("\nThe while loop performs {0} iterations when N is 4".format(num_iterations_4))

# 32 > 1, 32 // 2 = 16 (count = 1)
# 16 > 1, 16 // 2 = 8 (count = 2)
# 8 > 1, 8 // 2 = 4 (count = 3)
# 4 (we already know) 3 + 2 = 5
num_iterations_32 = 5  # REPLACE
print("\nThe while loop performs {0} iterations when N is 32".format(num_iterations_32))

# Deduction. this is 1 more than previous, 6
num_iterations_64 = 6  # REPLACE
print("\nThe while loop performs {0} iterations when N is 64".format(num_iterations_64))

runtime = "log N"
print("\nThe runtime for this function is O({0})".format(runtime))
