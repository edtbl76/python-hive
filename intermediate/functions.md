# Functions

## Lambda Function
Aka `anonymous function` is a one line shorthand for a function. 

```python
# Function
def add_two(my_input):
  return my_input + 2

# Lambda
add_two = lambda my_input: my_input + 2
```

### If/Else Format For Lambda
```python
lambda arguments : (return value if condition is True) 
    if (condition) else (return value if condition is False)
```

## Higher-Order Function

### Functions as First Class Objects
First Class Objects can be:
- stored as variables
- passed as arguments to a function
- returned by a function
- stored in data structures (lists, dicts, etc.)

### Higher-Order Function
Higher-Order Functions operate on other functions via arguments or via return values. This means that higher functions do one/both of the following:
- accept a function as an argument
- have a return value that is a function


#### Functions as arguments

```python
def total_bill(func, value):
  total = func(value)
  return total

def add_tax(total):
    tax = total * 0.06
    new_total = total + tax
    return new_total

def add_tip(total):
    tip = total * .2
    new_total = total + tip
    return new_total

total_bill(add_tax, 100)    # 106.0
total_bill(add_tip, 100)    # 120.0
```
#### Functions as arguments - Iteration

This is the long way, but it starts to get onerous if we need to add functionality. New loops, more iterations, and the code begins to look like spaghetti.
```python
bills = [115, 120, 42]
 
new_bills = []
 
for i in range(len(bills)):
  total = add_tax(bills[i])
  new_bills.append("Total amount owed is $" + "{:.2f}"
                   .format(total) + ". Thank you! :)")
 
print(new_bills)
```

Better, we can adjust our total_bills function that operates against a list that was passed in as an argument
```python
def total_bills(func, list):
  # This list will store all the new bill values
  new_bills = []
 
  # This loop will iterate through our bills
  for i in range(len(list)):
 
    # Here we apply the function to each element of the list!
    total = func(list[i])
    new_bills.append("Total amount owed is $" + "{:.2f}"
                     .format(total) + ". Thank you! :)")
 
  return new_bills


bills = [115, 120, 42]

#
# By refactoring total_bills to be a higher order function
# we allow it to take various other functional capabilities
# with minimal effort (and high abstraction)
#
bills_w_tax = total_bills(add_tax, bills)
bills_w_tip = total_bills(add_tip, bills)

print(bills_w_tax)
print(bills_w_tip)
```

#### Functions as Return Values 


Description of example
- First we have a function that defines a nested function that takes 2 numeric arguments (**length and width**) and returns the volume given the input height.
- outside of the function in the main body, we instantiate a variable `box_volume_height15` which calls the local function w/ the parameter '15'
    - the return value is a FUNCTION!
- Lastly we print the variable, passing in 2 params (3 and 2).
  - the return value is... a FUNCTION :)

```
def make_box_volume_function(height):
    def volume(length, width):
        return length*width*height
 
    return volume
 
box_volume_height15 = make_box_volume_function(15)
 
print(box_volume_height15(3,2))
```

---

## Built-In Higher Order Functions


### <u>map()</u>
```python
returned_map_object = map(function, iterable)
```

When called,  
- `map()` applies the passed function to each element in the iterable and returns a `map` object. 
- the `map` object holds the results from applying the first-order function to each element of the passed interable
- _Usually_ we'll convert the map into a list to enabe view and further use.

```python
def double(x):
 return x*2
 
int_list = [3, 6, 9]
 
doubled = map(double, int_list)

# Less Useful
print(doubled)          # OUTPUT: <map at 0x7f1ca0f58090>

# More Useful
print(list(doubled))    # OUTPUT: [6, 12, 18]
```

#### Lamdba's Revenge
Higher-Order functions work very well w/ lambda syntax. 
- lambdas are anonymous, so we don't need to define a new named function for `map()` if the function isn't going to be used anywhere else. 

```python
doubled = map(lambda input: input*2, int_list)
 
print(list(doubled))  # OUTPUT: [6, 12, 18]
```

Example
```python
grade_list = [3.5, 3.7, 2.6, 95, 87]

# use map and lambda if/else to make sure all of the
# grades are on the 100 point scale (some are from a 4
# point scale)
grades_100scale = map(lambda grade : grade if (grade > 4) 
                                else grade *25, grade_list)

print(list(grades_100scale))
```


### <u>filter()</u>
`filter()` has the same format as `map()`, however rather than taking a collection of input values and modifying them based on the passed in function, 
- filter takes in a function that returns a boolean as its first argument. 
- it only retains those elements for which the passed in function remains true. 

EXAMPLE 1
- `filter()` takes in `M_names` as our comparator function, and `names` as the collection of values to be evaluated. 
- the `filter()` function iterates through the list, passing those values to the lambda's logic. 
- In this case, the values only return true if the first character of the string is a non-case specific 'm'. 
- When we print the list-ified output of the `filter()`, this will reflect
  - `['margarita', 'Masako', 'Maki']`

```python
names = ["margarita", "Linda", "Masako", "Maki", "Angela"]
 
M_names = filter(lambda name: name[0] == "M" or name[0] == "m", names) 
 
print(list(M_names))
```


EXAMPLE 2
- Given a list w/ duplicated elements where one has been entered as a string and one as a number, we want to filter out the non-string entries.
```python
books = [["Burgess", 1985],
 ["Orwell", "Nineteen Eighty-four"],
  ["Murakami", "1Q85"],
   ["Orwell", 1984],
    ["Burgess", "Nineteen Eighty-five"],
     ["Murakami", 1985]]

string_titles = filter(lambda book : type(book[1]) == str , books)
print(list(string_titles))  

# [['Orwell', 'Nineteen Eighty-four'], ['Murakami', '1Q85'], 
# ['Burgess', 'Nineteen Eighty-five']]
```


### <u>reduce()</u>
`reduce()` has some differences from the previous higher-order builtins
- `reduce()` is NOT always avaiable like `map()` and `filter()`, it must be imported from `functools` to be used. 
- map() returns a map object, filter() returns a filter object, but `reduce()` returns... a single value. 
  - (this is ultimately the purpose of the function)


Reduce is a great way to take a bunch of numbers and accumulate them or multiply them.
- this is also great for fan-in logic when we need to merge the output of many streams into a single result. 

#### Example 1
- reduce takes a function and collection just like the previous higher-order builtins
- we've created a lambda that takes two inputs and multiplies them together
- reduce applies the lambda logic to the first 2 elements of the list
- afterwards, reduce applies the logic to the result of the previous calculation and the next element in the list. 
  - 3 * 6 = 18
  - 18 * 9 = 162
  - 162 * 18 = 1944
- once we reach the end of the collection, we return the calculated value.
```python
from functools import reduce
int_list = [3,6,9,12]

reduced_int_list = reduce(lambda x,y: x*y, int_list)
print(reduced_int_list)
```

#### Example 2 - Concat
```python
from functools import reduce
letters = ['r', 'e', 'd', 'u', 'c', 'e']

word = reduce(lambda a, b: a + b, letters)
print(word)
```