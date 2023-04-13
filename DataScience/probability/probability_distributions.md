# Probability Distributions

## Random Variables

A `random variable` is, in its simplest form, a function. In probability, we often use random variables to represent random events
- must be numeric (quantitative rather than qualitative)

### Discrete Random Variables
- A random variable with a countable number of possible values
  - rolling a (normal) die
  - common when observing "counting" events. 
  - limited to "whole numbers"

### Continuous Random Variables
- uncountable. 
  - measurement values
  - "we can always be more precise"
    - meters, centimeters, millimeters. 

---

## Probability Mass Function (PMF)

Type of probability distribution that defines the probability of observing a particular value of a `discrete random variable`.
- EX: It can be used to calculate probability of rolling a 3 on an X sided die. 

There are certain kinds of `random variables` (and associated `PMF`s) that are relevant for many different kinds of problems.These commonly used probability distributions have `names` and `parameters` that make them reusable/adaptable for different situations.

  EX: `Binomial Distribution` can be used to count the number of random variables in a coin flip. 
  - `n` = number of trials
  - `p` = probability of success in each trial. 
    - probability of the specific expected outcome (heads or tails)


For 10 coin flips, the graph would look like this: 

![](../img/img_10.png)


###  PMF Over a Range

![](../img/img_11.png)

NOTE: For large ranges, this results in a lot of repetitive code. 

There is an easier way...
![](../img/img_12.png)

We know that the sum of the probabilities for all possible values is equal to 1. 
- For 10 coin flips this means that 
  - p (0) + P(1) + P(2) + P(3) + P(4) + P(5) + P(6) + P(7) + P(8) = 1
  - In the example, the range we want to calculate is 0 - 8
  - So, P(0-8) + P(9-10) = 1
  -  P(0-8) = 1 - P(9-10)

---

## Cumulative Distribution Function (CDF)

The CDF for a `discrete random variable` can be derived from the `Probability Mass Function`.
- However, instead of the probability of observing a **_specific value_**, the CDF gives the probability of observing a **_specific value or LESS_**

- The value of a CDF at a given value is equal to the sum of the probabilities lower than it, w/ a value of 1 for the largest possible number. 
  - (Remember, the probabilities for all possible values in a given probability distribution add up to 1)

CDF are constantly increasing, so for 2 different numbers that the random variable could take on, the value of the function will always be greater for the larger number. 
This is represented mathematically as:

![](../img/img_13.png)

### CDF at PMF over a Range
For 10 fair coin flips the CDF(2 heads) is the equivalent of the PMF(0 - 2 heads)
- The CDF is simpler, because it requires a single calculation rather than three (or more if the range is larger).



![](../img/img_14.png)

The top graph represents the PMF. The bottom is the CDF, where each y-axis value is the sum of the probabilities <= to it in the PMF. 

We can use the CDF to calculate the probability of a specific range, by taking the difference between 2 values from the CDF
- Ex, to find the probability of observing 3 - 6 heads, we can take the probability of
  - <= 6 and subtract the probability of <= 2. 
  
![](../img/img_15.png)

---

## Probability Density Functions

- `discrete random variables` relate to `probability mass functions`
- `continuous random variables` relate to `probability density functions`


In a PDF, the highlighted area represents the probability of observing a value within the highlighted range.
- we can't calculate the probability at a single point, because the area of the curve underneath a single point is always zero. 
![](../img/img_16.png)

- The area under the curve can be calculated using the `cumulative distribution function` for the given probability distribution. 
  - `normal distribution`
    - the parameters for a normal distribution are the `mean` abd `standard deviation`
    - Normal(mean, standard deviation)


### Mean
The mean or average is calculated by adding up all observed values divided by the total number of values. 

### Standard Deviation
The standard deviation is a measure of the amount of variation or dispersion of a set values. This can also be defined as the degree of scatter of the data points relative to the mean. This describes how the values are spread across the data sample  


### Probability Density Functions and Cumulative Distribution Function
- The difference of two overlapping ranges can be used to calculate that a random selection will be within a range of values for continuous distributions. 
- This is _essentially_ the same process as calculating the probability of a range of values for discrete distributions. 
![](../img/img_17.png)


- The total area under the curve is equal to 1
  - this allows us to calculate the probability of observing something GREATER than a value
  - 1 - the probability of observing something less than a value = the probability of observing something greater than that value. 
![](../img/img_18.png)

---
## Poisson Distribution
Used to describe the # of times a certain event occurs within a fixed time or space interval.
- i.e. describes the no. of cars that past through a specific intersection between X and Y time on a given day. 

It can also be defined as a way to calculate the number of occurences given an expected rate. 


- Defined by the rate parameter, symbolized by the Greek letter lambda ƛ
- This represents the expected value (or the average value) of the distribution. 


EXAMPLE: 
If expected no. of customers between 1pm and 2pm is 7, we would set the parameter for the Poisson distribution to 7, making the `Probability Mass Function` for the Poisson(7) distribution as follows. 

![](../img/img_19.png)


### Calculating
Since the Poisson distribution is a discrete probability distribution, it can be described by a 
- PMF (Probability Mass Function) and 
- CDF (Cumulative Distribution Function)

(Calculation is no different)


### Expectation of Poisson Distribution
"What does the **expected value** mean? "

![](../img/img_20.png)

The tallest bar represents the value w/ the highest probability of occurring. 
- This doesn't mean that we will make 10 sales
- This means, that _on average_ across all weeks, we expect our average to equal roughly 10 sales per week.



```python
#
#   This code takes a sample of 1000 random values
#   from a Poisson Distribution w/ the expected value of 10.
#
import scipy.stats as stats
 
# generate random variable
# stats.poisson.rvs(lambda, size = num_values)
rvs = stats.poisson.rvs(10, size = 1000)
```

The resulting histogram:
![](../img/img_21.png)

- observations range from 2 - 20
- the peaks are at 9 and 10.

If we take the average of the 1000 random samples:
```python
print(rvs.mean())
```

The result is 10.009

### Spread of Poisson Distribution
Probability distributions have calculable variance

`Variance` is a way of measuring the spread/dispersion of values and probabilities in a distribution. 

For the Poisson distribution, variance is just the value of the λ (lambda)  
- this means that the expected value is equivalent to variance in Poisson distributions.
- this also means that as the expected value increases, the number of possible values the distribution can take on would also increase. 

2 Examples:
- λ = 3
- λ = 15

NOTE: The height in the second distribution is lower, because there are more possible values in the distribution. It also has an increased distribution.
![](../img/img_22.png)

#### Variance Calculation
```python
import scipy.stats as stats
import numpy as np

rand_vars = stats.poisson.rvs(4, size = 1000)
print(np.var(rand_vars))

# 3.864559
```

Another way to view the increase in possible values is to take the range of a sample. (the min/max values in a set).
```python
import scipy.stats as stats
 
#
#   generate 1000 random variables from a Poisson
#   distribution w/ λ = 4 
#
rand_vars = stats.poisson.rvs(4, size = 1000)

# Print the min/max values of the distribution
print(min(rand_vars), max(rand_vars))
```
- min = 0
- max = 12

If we increase the value of the lamba, the min/max will also change
- if lambda is increased to 10
  - min = 1
  - max = 22


---
## Properties of Expectation and Variance

### Properties of Expectation

1.)  The expected value of 2 independent random variables is the sum of each expected value separately. 
  

    E(X + Y) = E(X) + E(Y)

  For example, if we wanted to count the total # of heads between 10 fair quarter flips and 6 fair nickel flips, the expected value combined would be 5 heads (quarters) and 3 heads(nickels) resulting in 8 overall. 


2.) Multiplying a random variable by a constant `a` changes the expected value to be `a
 times the expected value of the random variable. 

  
    E(aX) = a *  E(X)

  For example, for a test that was given and graded w/ an average grade of 78 out of 100 points... if the teacher curves the grade by adding 2 points to everyone's grade, the average would now be 80 points
  

### Properties of Variance

1.) Increasing the values in a distribution by a constant `a` does NOT change the variance. 

    Var(X + a) = Var(X)

This is because the variance of a constant is 0 (there is no range for a single number). 
- Adding a constant to a random variable doesn't add any additional variance. 
- Applying this to the example of the test grades above, although the expected value (average) of the test scores changes, the spread and dispersion (variance) of the test scores stays the same. 

2.) Scaling the values of a random variable by a constant `a` scales the variance by the constant scquared. 

  
    Var(aX) = a^2 * Var(X)

For example, if we wanted to calculate the number of heads from 10 fair coin flips run 4 times (40 total coin flips), the variance would be multiplied 4^2 times the original variance.

3.) The variance of the sum of 2 random variables is the sum of the individual Variances. 

    Var(X + Y) = Var(X) + Var(Y)

This principle ONLY holds if the X and Y are independent random variables.

