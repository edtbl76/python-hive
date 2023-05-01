pi = 3.14159

option = input("Select (C)ircle or (T)riangle")

area = 0
if option.lower() == 'c':
  radius = float(input("Enter radius: "))
  area = pi * (radius ** 2)
elif option.lower() == 't':
  base = float(input("Enter base: "))
  height = float(input("Enter height: "))
  area = 0.5 * base * height
else:
  print("Invalid Option")

print(str(area))