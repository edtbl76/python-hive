# Dynamic Programming

A programming technique used to solve recursive problems more efficiently. 

In order to be a candidate for dynamic programming, a problem must have 
_overlapping subproblems_ so that smaller pieces of the problem can be 
combined to solve the original problem. 

Example: _The Levenshtein Distance_ is finding the minimum number of 
letters to change one word into another. 


## Fibonacci

 The Fibonacci series is a classic mathematical series in which the next 
 number is calculated as the sum of the previous two numbers:

`0, 1, 1, 2, 3, 5, 8, 13, 21, etc.`

The series begins with a **0** and **1**. It can be calculated iteratively by 
summing the two previous numbers starting with the third entry.  
Alternatively, the nth Fibonacci number can be calculated recursively.  A 
recursive solution pseudocode is as follows.

```text
function fib(n):
    if n is 1 or 0
        return n
    else
        return fib(n - 1) + fib(n - 2)
```

 This technique breaks up calculating the nth number into many smaller 
  problems, calculating each step as the sum of calculating the previous 
 two numbers.

A lthough this technique will certainly work to find the correct number, 
 as n grows, the number of recursive calls grows very quickly. Let’s 
 visualize all the function calls if we were to calculate the fourth 
Fibonacci number:

```text
fib(4)  -> fib(3) + fib(2)
    fib(3)  -> fib(2) + fib(1)
        fib(2) -> fib(1) + fib(0)
    fib(2) -> fib(1) + fib(0)
```

 As we can see, fib(2) is called twice, and fib(1) is called three times. 
  If n were larger than 4, we’d see the number of these calls ascend very 
  quickly. For instance, to calculate the 10th number, we’d make 34 calls 
  to fib(2) and 177 total function calls! Why do we need to call the same 
 function multiple times with the same input?

We don’t! We can use a technique called `memoization` to cut down greatly 
on the number of function calls necessary to calculate the correct number.

## Memoization

A specialized form of caching used to store the result of a function call. 
 The next time that function is called, instead of running the function 
 itself, the result is used directly. Memoization can result in much 
 faster overall execution times (although it can increase memory 
requirements as function results are stored in memory).

 Memoization is a great technique to use alongside recursion. The memo can 
  even be saved between function calls if it’s being used for common 
 calculations in a program.

### Memoizing Fibonacci

 In the previous example, many function calls to fib() were redundant. 
 Let’s memoize it in order to speed up execution.

 To begin, we’ll use a Python dictionary to store the memoized values. 
  We’ll set keys using n and values to store the result of that Fibonacci 
  number. Then, whenever we need to calculate a number, if it’s already 
 been calculated, we can retrieve the value from the dictionary in O(1) time.

```python
memo = {}
```

In pseudocode, our approach to memoization will look something like this:

```text
Create a memo dictionary

function fibonacci(n)
  if the key, n, exists in memo dictionary
    return memo[n]
  else
    calculate current fibonacci number
    store answer in memo
    return answer
```



