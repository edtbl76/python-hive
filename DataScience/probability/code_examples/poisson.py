#!/usr/bin/env python3

import scipy.stats as stats

##
#   Calculating Probabilities (Poisson) , Probability Mass Function
##


# Checkpoint 1
#
# Given a Call Center
#   and we expect the number of calls between 9 AM and 10 AM
#   to be 15 calls. What is the probability that we will actually see
#   exactly 15 calls?
#

# probability value (what we are calculating)
p = 15

# expected value (what is expected)
x = 15
prob_15 = stats.poisson.pmf(p, x)
print(prob_15)

# Checkpoint
# calculate prob_7_to_9
prob_7_to_9 = stats.poisson.pmf(7, 15) + stats.poisson.pmf(8, 15)  + stats.poisson.pmf(9, 15)

# print prob_7_to_9
print(prob_7_to_9)


##
#   Calculating Probabilities of a Range using Poisson
##


# Checkpoint 1
#
#   CDF can find the probability of observing more than x (20) values where 15
#   is the expected value in a given range, by subtracting the CDF from 1 (which represents the area under
#   a continuous random variable)
#
#
prob_more_than_20 = 1 - stats.poisson.cdf(20, 15)
print(prob_more_than_20)

# Checkpoint 2
#
#   CDF can be used to find the probability of observing between two values, by subtracting the CDF at 1 less  the
#       smaller value from the larger value.
#       (in our example observing between 17 and 21, we would subtract CDF at 16 from CDF at 21
#
prob_17_to_21 = stats.poisson.cdf(21, 15) - stats.poisson.cdf(16, 15)
print(prob_17_to_21)

