def is_int(x):
  absolute = abs(x)
  rounded = round(absolute)
  return absolute - rounded == 0

print is_int(10)
print is_int(10.5)


def digit_sum(n):
  total = 0
  for char in str(n):
    total += int(char)
  return total

def factorial(n):
  if n <= 1:
    return n
  return n * factorial(n - 1)


def is_prime(x):
    if x < 2:
        return False
    else:
        for n in range(2, x-1):
            if x % n == 0:
                return False
        return True

print is_prime(13)
print is_prime(10)

def count(sequence, item):
  total = 0
  for element in sequence:
    if item == element:
      total += 1
  return total

def purify(numbers):
  return [num for num in numbers if num % 2 == 0]

def remove_duplicates(collection):
  result = []
  for element in collection:
    if element not in result:
      result.append(element)
  return result

def median(collection):
  collection.sort()
  middle = len(collection) // 2
  if len(collection) % 2 != 0:
    return collection[middle]
  else:
    return float(collection[middle] + collection[middle + 1]) / 2




