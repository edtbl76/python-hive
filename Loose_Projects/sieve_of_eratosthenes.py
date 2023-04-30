def sieve_of_eratosthenes(limit):
  true_indices = []

  # handle edge cases
  if (limit <= 1):
    return true_indices

  # create the output list
  output = [True] * (limit+1)

  # mark 0 and 1 as non-prime
  output[0] = False
  output[1] = False

  # iterate up to the square root of the limit
  for i in range(2, limit+1):
    if (output[i] == True):
      j = i*2
      # mark all multiples of i as non-prime
      while j <= limit:
        output[j] = False
        j += i

  # remove non-prime numbers
  output_with_indices = list(enumerate(output))
  true_indices = [index for (index,value) in output_with_indices if value == True]
  return true_indices


primes = sieve_of_eratosthenes(13)
print(primes) # should return [2, 3, 5, 7, 11, 13]