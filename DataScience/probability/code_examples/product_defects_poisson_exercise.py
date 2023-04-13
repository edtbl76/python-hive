#!/usr/bin/env python3

import scipy.stats as stats
import numpy as np

# Task Group 1 ###
# Task 1:
#
#   number of defects on a given day follows the Poisson
#   distribution w/ the rate parameter (lambda, lam) equal to 7
#
#   Poisson distribution is special because the rate parameter represents
#   the expected value of the distribution.(In this case, 7 defects per day)
#
lam = 7

# Task 2:
#
#   Calculate the probability of observing exactly lam events on a given day.
#
#   (Use Probability Mass Function)
#
#   OUTPUT: 0.14900277967433773
#
print(stats.poisson.pmf(lam, lam))

# Task 3:
#
#  Calculate the probability of observing a "good day"
#
#
#
print(stats.poisson.cdf(2, lam))

## Task 4:
print(1 - (stats.poisson.cdf(9, lam)))

### Task Group 2 ###
## Task 5:
year_defects = stats.poisson.rvs(lam, size = 365)

## Task 6:
print(year_defects[0:21])

## Task 7:
print(lam * 365)

## Task 8:
print(sum(year_defects))

## Task 9:
print(np.mean(year_defects))

## Task 10:
print(max(year_defects))

## Task 11:
print(1 - stats.poisson.cdf(16, lam))


### Extra Bonus ###
# Task 12
print(stats.poisson.ppf(.9, lam))

# Task 13
print(sum(year_defects >= 10.0)/len(year_defects))