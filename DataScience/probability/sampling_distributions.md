# Sampling Distributions

Collecting data for an entire population is usually impossible. 

Sampling is a way to collect information about a smaller subset of the larger population, followed by the calculation of statistics (such as mean or median) as an estimation for the population value of interest. 

## Calculating Mean of Sample 
1. Collect the values for a sample of a population <br>
2. Calculate the mean <br
3. Plot the Population Distribution and the Calculated Mean
4. Generate Sample based on randomized selection 
5. Find the mean of the sample. 
6. Plot the Histogram of the Sample Distribution and its Mean
```python
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


population = pd.read_csv("salmon_population.csv")
population = np.array(population.Salmon_Weight)
pop_mean = round(np.mean(population),3)

## Plotting the Population Distribution
sns.histplot(population, stat='density')
plt.axvline(pop_mean,color='r',linestyle='dashed')
plt.title(f"Population Mean: {pop_mean}")
plt.xlabel("Weight (lbs)")
plt.show()
plt.clf() # close this plot

samp_size = 10
# Generate our random sample below
sample = np.random.choice(np.array(population),
                          samp_size, replace = False)

### Define sample mean below
sample_mean = np.mean(sample)


### Uncomment the lines below to plot the sample data:
sns.histplot(sample, stat='density')
plt.axvline(sample_mean,color='r',linestyle='dashed')
plt.title(F"Sample Mean: {sample_mean}")
plt.xlabel("Weight (lbs)")
plt.show()
```
![](../img/img_23.png)

## Calculating Sample Variance
1. Collect Population
2. Define a sample size
3. Create random selection (the for loop!)
4. Plot the Sampling Distribution

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


population = pd.read_csv("cod_population.csv")
# Save transaction times to a separate numpy array
population = population['Cod_Weight']

sample_size = 50
sample_means = []

for i in range(500):
  samp = np.random.choice(population, sample_size, replace = False)
  # calculate mean here
  this_sample_mean = np.mean(samp)
  # append here
  sample_means.append(this_sample_mean)

sns.histplot(sample_means,stat='density')
plt.title("Sampling Distribution of the Mean")
plt.xlabel("Weight (lbs)")
plt.show()
```
Since the sample is randomized, we'll expect slightly different results (the sample_mean) for each execution. If we run X number of trials, we can calculate the expected/anticipated variance across the sample means.

## Central Limit Theorem
The CLT allows the specific description of the sampling distribution of the mean. 
- It states that the sampling distribution of the mean is "normally distributed" as long as the population isn't too skewed or the sample size is large enough. 
- Good rule of thumb is a sample size greater than 30 (regardless of what the distribution of the population is like)
- If the distribution of the population is normal, the sample size can be smaller than that. 


### CLT - Establishing that a sampling distribution will be normally distributed
Example:
1. Show a population distribution that is skewed (i.e. not normally distributed)
2. Checkpoint 2 shows the sampling distribution of the mean. 
3. (Set samp_size to 6 first, which still shows some skew)
4. (Set samp_size to 50 which shows the sampling distribution begin to normalize)
```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

cod_population = pd.read_csv("cod_population.csv")
# Save transaction times to a separate numpy array
population = cod_population['Cod_Weight']

## Checkpoint 1:
sns.histplot(population, stat = 'density' )
plt.title("Population Distribution")
plt.show()

sample_means = []

# Below is our sample size
samp_size = 6

for i in range(500):
    samp = np.random.choice(population, samp_size, replace = False)
    this_sample_mean = np.mean(samp)
    sample_means.append(this_sample_mean)

# Checkpoint 2
plt.clf() # this closes the previous plot
sns.histplot(sample_means, stat = 'density' )
plt.title("Sampling Distribution of the Mean")
plt.xlabel("Weight (lbs)")
plt.show()
```

![](../img/img_24.png)

### CLT - Describing normal distribution quantitatively
Normal distributions are described by their mean μ (mu) and standard deviation σ (sigma).

1. We take samples of size `n` from a population 
   1. that has true population mean `μ`
   2. and standard deviation `σ`
2. calculate sample mean `x`
3. Given that n is sufficiently large (n > 30), the sampling distribution of the means will be normally distributed w/
   1. mean `x` ~= population mean `μ`
   2. standard deviation is equal to the population standard deviation divided by the square root of the sample size

    ![](../img/img_25.png)


```python
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
import seaborn as sns


# Set the population mean & standard deviation:
population_mean = 10
population_std_dev = 10
# Set the sample size:
samp_size = 6

# Create the population
population = np.random.normal(population_mean, population_std_dev,
                              size = 100000)

# Simulate the samples and calculate the sampling distribution
sample_means = []
for i in range(500):
    samp = np.random.choice(population, samp_size, replace = False)
    sample_means.append(np.mean(samp))

mean_sampling_distribution = round(np.mean(sample_means),3)

# Plot the original population
sns.histplot(population, stat = 'density')
plt.title(f"Population Mean: {population_mean} ")
plt.xlabel("")
plt.show()
plt.clf()

## Plot the sampling distribution
sns.histplot(sample_means, stat='density')
# calculate the mean and SE for the probability distribution
mu = np.mean(population)
sigma = np.std(population)/(samp_size**.5)
# plot the normal distribution with mu=popmean,
# sd=sd(pop)/sqrt(samp_size) on top
x = np.linspace(mu - 3*sigma, mu + 3*sigma, 100)

plt.plot(x, stats.norm.pdf(x, mu, sigma), color='k', 
         label = 'normal PDF')
plt.title(f"Sampling Dist Mean: {mean_sampling_distribution}")
plt.xlabel("")
plt.show()
```
![](../img/img_26.png)


## Standard Error
(This is the second part of the CLT - `Central Limit Theorem`)
- The sampling distribution of the mean is normally distribution
- The standard deviation is equal to the population standard deviation (sigma), divided by the sample size (n)

![](../img/img_25.png)

The standard deviation of the sample distribution is also referred to as the `standard error of the estimate of the mean`
- In many cases, we can't know the population standard deviation, so we estimate the standard error by using the _sample_ standard deviation

![](../img/img_27.png)
NOTE:
- as sample size increases, the standard error will decrease
  - the mean stays the same.
- as the population standard deviation increases, the standard error will ALSO increase. 

### Example

```python
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
import seaborn as sns


# Set the population mean & standard deviation:
population_mean = 10
population_std_dev = 10
# Set the sample size:
samp_size = 6

# Create the population
population = np.random.normal(population_mean, population_std_dev,
                              size = 100000)

# Simulate the samples and calculate the sampling distribution
sample_means = []
for i in range(500):
    samp = np.random.choice(population, samp_size, replace = False)
    sample_means.append(np.mean(samp))

mean_sampling_distribution = round(np.mean(sample_means),3)

# Plot the original population
sns.histplot(population, stat = 'density')
plt.title(f"Population Mean: {population_mean} ")
plt.xlabel("")
plt.show()
plt.clf()

## Plot the sampling distribution
sns.histplot(sample_means, stat='density')
# calculate the mean and SE for the probability distribution
mu = np.mean(population)
sigma = np.std(population)/(samp_size**.5)
# plot the normal distribution with mu=popmean, 
# sd=sd(pop)/sqrt(samp_size) on top
x = np.linspace(mu - 3*sigma, mu + 3*sigma, 100)

plt.plot(x, stats.norm.pdf(x, mu, sigma), color='k', 
         label = 'normal PDF')
plt.title(f"Sampling Dist Mean: {mean_sampling_distribution}")
plt.xlabel("")
plt.show()
```

![](../img/img_28.png)

#### Task 1
Increase the sample size to 50 and compare the changes in the distribution
![](../img/img_29.png)
- As the sample size increases, the standard error decreases. 
- as the standard error decreases, the distribution gets taller and thinner.

#### Task 
Increase the standard deviation to 30
(keep the sample size @ 50)
![](../img/img_30.png)
- this increases the variance of the population distribution. 
- The result is that the sampling distribution mean appears flatter and thicker. 
  - (the standard error increases due to the larger numerator)


## Biased Estimators
Per CLT `Central Limit Theorem` 
- sampling mean distribution = population mean
- This is the case for SOME but not ALL sampling distributions. 

We can have a sampling distribution for ANY sample statistic
- mean
- median
- max/min
- variance
- many more!

`Unbiased Estimator`
- A statistic of a population parameter where the mean of the sampling distribution of the statistic is equal to the value of the statistic for the population. 

`Biased Estimator`
- A statistic of a population parameter where the mean of the sampling distibution of the statistic is NOT equal to the value of the statistic for the population. 
- EX: Maximum

### Example 1 - Variance
```python
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats


app_stat_text = "Maximum"
def app_statistic(x):
    return np.var(x)

### Below calculates the statistic for this population:
### You don't need to change anything below to pass the checkpoints
mean, std_dev = 50, 15
population = np.random.normal(mean, std_dev, 1000)

pop_statistic = round(app_statistic(population),2)

sns.histplot(population, stat = 'density')
plt.axvline(pop_statistic,color='r',linestyle='dashed')
plt.title(f"Population {app_stat_text}: {pop_statistic}")
plt.xlabel("")
plt.show()
plt.clf()

sample_stats = []
samp_size = 5
for i in range(500):
    samp = np.random.choice(population, samp_size, replace = False)
    this_sample_stat = app_statistic(samp)
    sample_stats.append(this_sample_stat)

sns.histplot(sample_stats, stat = 'density')
plt.title(f"Sampling Dist of the {app_stat_text} \nMean: {round(np.mean(sample_stats),2)}")
plt.axvline(np.mean(sample_stats),color='r',linestyle='dashed')
plt.xlabel(f"Sample {app_stat_text}")
plt.show()
plt.clf()

```
BIASED
![](../img/img_31.png)

### Change to mean
```python
def app_statistic(x):
    return np.mean(x)
```
UNBIASED
![](../img/img_32.png)

## Calculating Probabilities
Once we know the sampling distribution of the mean, we can also use it to estimate the probability of observing a particular range of sample means, given some information (either known or assumed) about the population. To do this, we can use the Cumulative Distribution Function, or (CDF) of the normal distribution.

Let’s work through this with our salmon fish example. Let’s say we are transporting the salmon and want to make sure the crate we carry the fish in will be strong enough to hold the weight.

Suppose we estimate that the salmon population has an average weight of 60 lbs with a standard deviation of 40 lbs.
- We have a crate that supports 750 lbs, and we want to be able to transport 10 fish at a time.
- We want to calculate the probability that the average weight of those 10 fish is less than or equal to 75 (750/10).

Using the CLT, 
- we first estimate that the mean weight of 10 randomly sampled salmon from this population is normally distributed with mean = 60 and standard error = (40^2)/10. 
- Then, we can use this probability distribution to calculate the probability that 10 randomly sampled fish will have a mean weight less than or equal to 75.

```python
x = 75
mean = 60
std_dev = 40
samp_size = 10
standard_error = std_dev / (samp_size**.5)
# remember that **.5 is raising to the power of one half, or taking the square root
 
stats.norm.cdf(x,mean,standard_error)
```

