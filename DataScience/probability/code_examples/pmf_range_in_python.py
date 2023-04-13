#!/usr/bin/env python3

import scipy.stats as stats

# Coin flip - Binomial PMF Range
#
#   x = The value of interest (heads or tails)
#   n = the sample size (number of fair coin flips)
#   p = probability of success
#
#   For a range, we have to add all of the values in the range.
#   EX: P(2-4 heads) = P(2 heads) + P(3 heads) + P(4 heads)
#   x is going to change, but n and p will remain constant.
n = 10
p = 0.5

# You could do this with a loop...
heads_2 = stats.binom.pmf(2, n, p)
heads_3 = stats.binom.pmf(3, n, p)
heads_4 = stats.binom.pmf(4, n, p)
print(heads_2 + heads_3 + heads_4)


# Example 1, 10 flips, 4 - 6 heads
print(stats.binom.pmf(4, n, p) + stats.binom.pmf(5, n, p) + stats.binom.pmf(6, n, p))


# Example 2 2 - 10 heads.
#
#   We want 3 - 10
#   so P(0-2) + P(3-10) = 1
#   P(3-10) = 1 - P(0-2)
print(1 - (stats.binom.pmf(0, n, p) + stats.binom.pmf(1, n, p) + stats.binom.pmf(2, n, p)))
