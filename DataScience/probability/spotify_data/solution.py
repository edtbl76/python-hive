#!/usr/bin/env python3

from utility import choose_statistic, population_distribution, sampling_distribution
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
import seaborn as sns

# Task 1: Load In Spotify Dataset
spotify_data = pd.read_csv('spotify_data.csv')

# Task 2: Preview the dataframe
print(spotify_data.head())

# Get the relevant column (tempo)
song_tempos = spotify_data['tempo']

# Set samplesize
sample_size = 30

# Plot Population Distribution
population_distribution(song_tempos)

# Plot Sampling Distribution of the Sample Mean
# with samples sizes of 30 songs
sampling_distribution(song_tempos, sample_size, "Mean")

# Plot Sampling Distribution of the Sample Minimum
# with sample size of 30 songs
sampling_distribution(song_tempos, sample_size, "Minimum")

# Plot Sampling Distribution of the Sample Variance         (BIASED)
# with sample size of 30 songs
sampling_distribution(song_tempos, sample_size, "Variance")

# Repeat previous check, but changing the Delta Degrees of Freedom (ddof = 1)
# This removes the bias from the previous estimator
sampling_distribution(song_tempos, sample_size, "Variance DDOF")

# calculate population mean and population standard deviation
population_mean = np.mean(song_tempos)
population_std = np.std(song_tempos)

# calculate the standard error
standard_error = population_std / sample_size**.5

# Calculate the probability that the sample mean of 30 selected songs
# is less than 140bpm
#   (less than means that we'll use Cumulative Density Function)
#
#   RESULT: 0.043003550159587636
#
print(stats.norm.cdf(140, population_mean, standard_error))

# Calculate the probability that the sample mean of 30 selected songs
# is GREATER than 150 bpm.
#   (We can use 1 - CDF)
#
#   RESULT: 0.2808802810182194
#
print(1 - stats.norm.cdf(150, population_mean, standard_error))

