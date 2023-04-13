# Mine

letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

def unique_english_letters(word):
  used_letters = []
  count = 0
  for letter in word:
    if letter not in used_letters and letter in letters:
      count += 1
      used_letters.append(letter)
  return count

# Theirs

def unique_english_letters(word):
  uniques = 0
  for letter in letters:
    if letter in word:
      uniques += 1
  return uniques
