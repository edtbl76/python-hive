#!/usr/bin/env python
from __future__ import print_function
from timeit import Timer
import traceback

def fibby(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibby(n-1) + fibby(n-2)


def fibby_iter(n):
    old, new = 0, 1
    if n == 0:
        return 0
    for i in range(n - 1):
        old, new = new, old + new
    return new


memo = {0:0, 1:1}
def fibby_mem(n):
    if n not in memo:
        memo[n] = fibby_mem(n - 1) + fibby_mem(n - 2)
    return memo[n]


def main():

    #
    # Fibonacci
    #
    print()
    print(fibby(10))
    print(fibby_iter(10))

    #
    # Fibonacci Race    (Iterative tends to be much faster than recursive)
    #
    print("Recursion vs. Iteration")
    t1 = Timer("fibby(10)", "from __main__ import fibby")

    for i in range(1, 31):
        s = "fibby({})".format(str(i))
        try:
          t1 = Timer(s, "from __main__ import fibby")
        except NameError:
            print(traceback.format_exc().split()[-1])
        time1 = t1.timeit(3)
        s = "fibby_iter({})".format(str(i))
        t2 = Timer(s, "from __main__ import fibby_iter")
        time2 = t2.timeit(3)
        print("n={:2}, fibby: {:8.6f}, fibby_iter: {:7.6f}, percent: {:10.2f}"
              .format(i, time1, time2, time1 / time2))

    """ Recursion (on its own) is much slower than iteration because recursion has no way to remember its
        previous iterations
    """

    #
    # RECURSION WITH MEMORY
    #
    print()
    print("Recursion w/ Memory vs. Iteration")
    t3 = Timer("fibby_mem(10)", "from __main__ import fibby_mem")

    for i in range(1, 31):
        s = "fibby_mem({})".format(str(i))
        t3 = Timer(s, "from __main__ import fibby_mem")
        time3 = t3.timeit(3)
        s = "fibby_iter({})".format(str(i))
        t4 = Timer(s, "from __main__ import fibby_iter")
        time4 = t4.timeit(3)
        print("n={:2}, fibby: {:8.6f}, fibby_iter: {:7.6f}, percent: {:10.2f}"
              .format(i, time3, time4, time3 / time4))

    """ Stateful Recursion is faster than iteration. Live it Love it KNOW IT."""

if __name__ == '__main__':
    main()
