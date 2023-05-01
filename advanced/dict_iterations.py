my_dict = {
  "Name": "Guido",
  "Age": 56,
  "BDFL": True,
  "Fuck": "You"
}

print(my_dict.keys())
print(my_dict.values())

for key in my_dict:
  print(key, my_dict[key])


# Print tuples in form of (key, value)
movies = {
  "Monty Python and the Holy Grail": "Great",
  "Monty Python's Life of Brian": "Good",
  "Monty Python's Meaning of Life": "Okay"
}
print(movies.items())

# [("Monty Python's Life of Brian", 'Good'), ("Monty Python's Meaning of Life", 'Okay'), ('Monty Python and the Holy
# Grail', 'Great')]
