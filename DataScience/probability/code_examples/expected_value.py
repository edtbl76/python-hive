#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats


def histogram_function(rand_vars):
    plt.hist(rand_vars, bins=np.arange(len(set(rand_vars))) - 0.5, edgecolor="black")
    plt.xticks(list(range(rand_vars.max())))
    plt.show()


# lambda 15, 1000 random draws
rand_variables = stats.poisson.rvs(15, size=1000)
print(rand_variables)
histogram_function(rand_variables)
