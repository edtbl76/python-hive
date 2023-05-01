# Define factorial() below:
def factorial(n):
    # Base Case
    if n == 1:
        return 1

    # Recursive Step
    # - current input value * recursive call
    return n * factorial(n - 1)


print(factorial(12))
# Causes RecursionError -- Too Big!
print(factorial(1000))



