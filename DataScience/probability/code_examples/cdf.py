#!/usr/bin/env python3

import scipy.stats as stats

# Coin Flips
n = 10

# Probability
p = 0.5


# Checkpoint 1
prob_1 = stats.binom.cdf(3, n, p)
print(prob_1)

# compare to pmf code
#
#   Range of 0-4 (4 is exclusive)
#
#
prob_1_pmf = 0
for i in range(0, 4):
    prob_1_pmf += stats.binom.pmf(i, n, p)
print(prob_1_pmf)


# Checkpoint 2
#
#   In order to calculate MORE than 5, we can simply subtract the range of 0-5 from 1 (which represents the
#   sum of all probabilities)
#
prob_2 = 1 - stats.binom.cdf(5, 10, .5)
print(prob_2)


# Checkpoint 3
#
#   In order to calculate the probability between 2 and 5, we subtract the CDF of 1 from 5.
#
#
prob_3 = stats.binom.cdf(5, 10, .5) - stats.binom.cdf(1, 10, .5)
print(prob_3)