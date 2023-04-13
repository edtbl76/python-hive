# Probability

A branch of math that allows us to quantify uncertainty. 

## Set Theory

Branch of math based around the concept of `sets`. In simple terms, a set is a collection of things. Sets follow two key rules. 
- Each element in a set is distinct
- the elements in a set are in no particular order. 


    A = {1,2,3,4,5}


### Subsets
Set A is a subset of set B if all of the elements in A exist within B

    A = {1,2,3}
    B = {1,2,3,4,5}

---

## Experiments and Sample Spaces

`Experiment`: something that produces observation(s) with some level of uncertainty

`Sample Point`: a single possible outcome of an experiment

`Sample Space`: the set of ALL possible sample points for an experiment.

`Event`: a specific outcome (or set of outcomes) of an experiment. 
- This is always a subset of the sample space. 


Example: Experiment w/ 2 Coin Flips:

    S = { HH, HT, TH, TT}

    The sample space includes 4 sample points. 

### Probability
If we run an experiment an infinite amount of times, the probability of each event is the proportion of times it occurs. 

![](../img/img.png)


### Law of Large Numbers
- As our total number of trials increases, the observed proportion of times each event occurs will converge to its true probability. (i.e. as the total number of trials approaches infinity)

---

## Rules of Probability

### Union
The `union` of 2 sets encompasses any element that exists in either one or both of them. 
- Usually represented as a `Venn diagram`

![](../img/img_1.png)


### Intersection
The `intersection` of 2 sets encompasses any element that exists in both of the sets. 
- This represents the concentric section of a `Venn diagram`

![](../img/img_2.png)


### Complement
The `complement` of a set consists of all possible outcomes outside of the set. 

Complement of A:
![](../img/img_3.png)


Complement of B:
![](../img/img_4.png)

--- 
## Independence/Dependence

`Independence` the characteristic of multiple events when the occurence of one event doesn't affect the probility of other events. 

`Dependence` is when the probability of one event depends on the outcome some other event. 

## Mutually Exclusive
![](../img/img_5.png)
Two events are considered `mutually exclusive` if they can't occur at the same time. 

---

## ADDITION RULE

### Non Mutually Exclusive
![](../img/img_6.png)

For non-mutually exclusive events, trying to find the probability of one or both is defined as the probability of the `union` of each sample set .

The calculation subtracts the intersection of A and B, because it is reflected twice. 


### Mutually Exclusive. 
In a mutually Exclusive scenario, the sample sets have no overlap (and therefore no `intersection`), simplifying the equation.

![](../img/img_7.png)


---

## Conditional Probability

This is used to calculate the probability that a pair of dependent events will both occur. Put another way, it measures the probability of one event happening given that another one has already occurred. 
- "given" is denoted w/ a vertical line.


    EXAMPLE:

        P( Event2 | Event1 )

        Given Event1, then Event2


### Independent Events

    P(A | B) = P (A)
    P(B | A) = P (B)


---

## Multiplication Rule

For 2 events, A and B, we want to calculate the probability of A and B occurring simultaneously. 
- NOTE for `mutually exclusive` events we know this is 0%. 

### General Formula / Dependent Events

    P (A and B) = P(A) * P (B | A)

![](../img/img_8.png)

Tree Diagram 
- way to visualize all possible outcomes of a pair of events
    - each branch represents a specific set of events
    - the probabilities the terminal branches (all possible sets of outcomes) sum to one.
    - we multiply across branches (using multiplication rule) to calc the probability that each branch (set of outcomes) will occur.

## Independent Events

Since `P (B | A) = P (B)` is true for independent events, 

then the probability of 2 events occurring simultaneously (Per the multiplication rule) is


    P(A and B) = P(A) * P(B)


## Bayes' Theorem
![](../img/img_9.png)

EXAMPLE: 
- Imagine you are a patient that tested positive for a specific malady. 
- You might want to know the actual probability that you HAVE that malady given that you tested positive. (i.e. there is some possible failure rate)
  

    P( Malady | Tested Positive)
    

To calculate this, we use the `Bayes' Theorem`
  

    APPLYING THE THEOREM:

      P (M | TP) = { P(TP | M) * P (M) } / P (TP)


  
  
    

  
