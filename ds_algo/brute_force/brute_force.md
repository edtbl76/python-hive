# Brute Force Algorithms

Learn about the pros and cons of brute force algorithms.

We have all heard of the saying, “Work smarter, not harder”. This phrase is 
not only sound advice for everyday life but also for programming. After all, 
the reason why we study algorithms is to learn smarter ways to solve 
problems. A “smart” algorithm is fast and often complex; on the other hand, 
a “_brute force_“ algorithm is slow but much easier to implement.

As its name implies, a _brute force_ algorithm is a straightforward method 
that solves a problem by going through every possible choice _**one by one**_ 
until a solution is found. Instead of utilizing clever techniques, brute 
force algorithms rely on sheer computing power to solve problems. In this
article, we will learn about brute force algorithms and analyze their pros
and cons.

## Brute Force in Real Life
Imagine you are a student in the middle of a math lecture and your professor 
instructs everyone in the class to open the textbook and turn to the 
“Quadratic Formula” chapter as quickly as possible. There’s a slight problem: 
the textbook has 1000 pages and you don’t remember which page the chapter is 
on. What do you do?

The brute force approach here is to start at the very first page of your 
textbook and flip the pages one by one until you reach the “Quadratic Formula” 
chapter. Assuming it is the first chapter of the textbook, then this approach
is fine as you wouldn’t waste too much time; however, if the chapter is on 
page 815, then you will be flipping the textbook for a long time, miss out on 
the lecture, and get a bad grade on the upcoming test!

Of course, no sensible person would ever use this brute force approach in 
real life. A better method might be to look for “Quadratic Formula” in the 
table of content and then directly flip to that page. You will be able to
reach the chapter much faster and keep paying attention in class.

![img.png](img.png)

## Brute Force in Programming
In programming, brute force algorithms are rarely the most efficient. However, 
we still learn about them because they are easy to implement and serve as good 
segways to more complex algorithms. In fact, you should have already come 
across some brute force algorithms in this course. The bubble sort and 
selection sort algorithms, for example, fall under the brute force category 
because they are less efficient compared to more optimized algorithms like
merge sort and quicksort.

Let’s take a look at a problem where a brute force algorithm can be applied.

We want to print all divisors of a given natural number `n` (a divisor of `n` 
is an integer that evenly divides `n`). For example:

```text
Input: n = 10
Output: 1 2 5 10
Explanation: 1, 2, 5, 10 are all numbers that evenly divide 10.
```

A brute force algorithm can solve this problem in three steps:

1. Iterate all numbers from `1` to `n` in a loop.
2. Check if each number is a divisor of `n`.
3. If it is, printing that number.

## Efficiency of Brute Force
The time complexity of a brute force algorithm is usually proportional to the 
size of the input data because it needs to test every possible answer. In the 
flipping textbook example described earlier, the Big O runtime of the brute 
force algorithm is `O(N)`, where `N` is the number of pages. If we want to find 
some information on the last page of the textbook, there are no other ways to 
get there other than to painfully flip through `N` pages, regardless of how 
large `N` is.

The space complexity of brute force algorithms varies from problem to problem. 
There is no general rule that applies to every algorithm, so the programmer 
needs to determine the space complexity on a case-by-case basis.

![img_1.png](img_1.png)

## The Pros and Cons of Brute Force
The main disadvantage of brute force algorithms is that they are slow. 
They should not be used in real-world problems, which often deal with large 
and unorganized data. The cost of a brute force algorithm can also grow very 
quickly as the size of the problem increases.

This concept can be demonstrated in the password cracking problem: If we want 
to crack a 10 character long numerical password using a brute force algorithm, 
the process would take less than 10 seconds. However, if we increase the 
password length to 20, the algorithm would need on average about 10 years to 
crack that password.

Needless to say, 10 seconds versus 10 years is an astronomical difference. 
Now you see why brute force algorithms are not the best idea.

Another comparison that we have already touched on is bubble sort vs. 
quicksort. If you are wondering just much faster quicksort is, here is a 
graph showing the time to sort as the number of elements 
increases:
![img_2.png](img_2.png)

With that said, brute force algorithms do come with some upsides. For one, 
they are much easier for programmers to implement. It allows you to quickly 
make progress and come up with something that works. The simplicity of brute 
force algorithms also means that they are less likely to contain 
inconsistencies and bugs. Lastly, if you are more concerned about memory 
resources than time, some brute force algorithms require less overhead than 
their optimized counterparts. For example, bubble sort is slower than merge 
sort (`O(N^2)` vs `O(NlogN)`) but uses less memory (`O(1)` vs `O(N)`).

# Review

Let’s review what we learned:

- A brute force algorithm solves a problem by going through all possible 
choices until either a solution is found or all possibilities have been 
exhausted (no solution).
- The time complexity of a brute force algorithm is often proportional to 
  the input size.

<u>Pros of brute force:</u>
- Easier to implement than more optimized algorithms
- Simple, consistent, and bug-free
- Some brute force algorithms (ie. bubble sort) require less memory than 
  their more optimized counterparts

<u>Cons of brute force:</u>
- Slow runtime when there are many possible choices to compute
- Inapplicable for real-world problems