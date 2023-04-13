# Binomial Distribution

## Parameters
- `n` = total number of events
- `p` = probability that the specific outcome we are looking for, will occur. 


    EX: If we flip a coin 10 times, n = 10, and p = .5

## Expected Value

The formula for expected value can be viewed as 

    E(x) = n * p


    For example, if we flip a coin 10 times, and we want to know 
    how many times it will turn up heads, the expected value is

        n * p = 10 * .5 = 5


NOTE: Sometimes, the expected value will be a fraction (even if that is impractical given pragmatic real world scenarios)
For example, if I changed n to 5, the expected value is 2.5. 

### Example 1
LaBron James has an 85% chance of making a given free throw. He takes 20 free throws. What is the expected value of free throws he'll make? 


```text
# n = 20
# p = .85

E(X) = n * p
     = 20 * .85
     = 17
```

### Example 2
Connor has a 98% chance of arriving early or on time to school. He goes to school for 180 days. What is the expected number of days he'll be late? 
NOTE: We're looking for the INVERSE of the provided probability. 

```text
# n = 180
# p = .02 
E(X) = n * p
     = 180 * .02
     = 3.6
```

---

## Variance

The variance of a single event is calculated as the product of the probability that success happens and the probability that it doesn't. 

    p * (1 - p)

Therefore, to calculate the variance for `n` number of events, we get the equation:

    Variance(# of Successful Events) 

        V(X) = n * p * (1 - p)

For our Coin flip example:
- n = 10 coin flips
- p = 0.5
- V(x) = 10 * .5 * (1 - .5) = 2.5

A better example, is a multiple choice quiz w/ 20 questions, each w/ 4 options
- n = 20
- p = 0.25
- V(X) = 20 * .25 * (1 - .25)
- = 5 * .75 = 3.75

### Example 1
Hoops Player takes 20 free throws, w/ an .85 percent chance of success. What is the variance?
```text
variance_baskets = 20 * .85 * (1 - .85)
print(variance_baskets)     

# Answer
# 2.55
```

### Example 2
