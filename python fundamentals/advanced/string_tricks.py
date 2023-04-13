def reverse(text):
  result = ""
  for char in text:
    result = char + result
  return result


vowels = "aeiouAEIOU"
def anti_vowel(text):
  result = ""
  for char in text:
    if char not in vowels:
      result += char
  return result



score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
         "x": 8, "z": 10}

def scrabble_score(word):
  points = 0
  for char in word:
    points += score[char.lower()]
  return points


def censor(text, word):
    words = text.split()
    result = ''
    stars = '*' * len(word)
    count = 0
    for i in words:
        if i == word:
            words[count] = stars
        count += 1
    result = ' '.join(words)

    return result


print
censor("this hack is wack hack", "hack")