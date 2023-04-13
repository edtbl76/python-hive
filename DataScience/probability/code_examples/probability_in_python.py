#!/usr/bin/env python3

import scipy.stats as stats

# Coin flip - Binomial PMF

# value of interest (Heads/Tails)
x = 5

# sample size (# of flips)
n = 10

# calculate probability
prob_1 = stats.binom.pmf(x, n, 0.5)
print(prob_1)


# Question 2
x = 7 # heads
n = 20 # fair coin flips
prob_2 =  stats.binom.pmf(x, n, 0.5);
print(prob_2)