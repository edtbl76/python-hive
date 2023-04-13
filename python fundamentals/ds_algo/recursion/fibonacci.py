# define the fibonacci() function below...
def fibonacci(n):
    # Base Cases
    if n == 0:
        return 0
    if n == 1:
        return 1

    # Recursive Step
    # 2 recursive calls
    # last step and second to last step
    return fibonacci(n - 2) + fibonacci(n - 1)


print(fibonacci(6))
# set the appropriate runtime:
# 1, logN, N, N^2, 2^N, N!
fibonacci_runtime = "2^N"