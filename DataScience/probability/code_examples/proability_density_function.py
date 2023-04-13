#!/usr/bin/env python3

import scipy.stats as stats

# basic Example
#
#   x = value of interest (height of person in cm)
#   loc = the mean of the probability distribution (i.e. the average value)
#   scale = standard deviation of the probability distribution
#
x = 175
loc = 167.64
scale = 8

prob = stats.norm.cdf(x, loc, scale)
print(prob)


# Probability Density Functions and Cumulative Distribution Function
#
#  Calculating the probability that the weather on a randomly selected
#   day will be between 18 - 25 degrees Celsius
#
#   Normal Distribution has a mean of 20 and a standard deviation of 3
mean = 20
sd = 2
temp_25 = stats.norm.cdf(25, mean, sd)
temp_18 = stats.norm.cdf(18, mean, sd)
print(temp_25 - temp_18)


#   Probability that the weather on a randomly selected day
#   will be greater than 24 degrees Celsius.
#
#
# # Checkpoint 2
temp_prob_2 = 1 - stats.norm.cdf(24, mean, sd)
print(temp_prob_2)