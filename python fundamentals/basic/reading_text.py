# Whole File
with open('welcome.txt') as text_file:
    text_data = text_file.read()
print(text_data)

# Read lines
with open('how_many_lines.txt') as lines_doc:
    for line in lines_doc.readlines():
        print(line)

# Read line
with open('just_the_first.txt') as first_line_doc:
    first_line = first_line_doc.readline()
    print(first_line)

# Write
with open('bad_bands.txt', 'w') as bad_bands_doc:
  bad_bands_doc.write('Oasis')

# Append
with open('cool_dogs.txt', 'a') as cool_dogs_file:
  cool_dogs_file.write("Air Buddy")

