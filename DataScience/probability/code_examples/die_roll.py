#!/usr/bin/env python3

import numpy as np

# dice
die_6 = range(1, 7)
die_12 = range(1, 13)

# num rolls
num_rolls = 10

# results
results_1 = np.random.choice(die_6, num_rolls, True)
results_2 = np.random.choice(die_12, num_rolls, True)

# display
print(results_1)
print(results_2)
