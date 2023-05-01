 We’ve been opening these files with this with block so far, but it seems 
  a little weird that we can only use our file variable in the indented 
  block. Why is that? The with keyword invokes something called a context 
  manager for the file that we’re calling open() on. This context manager 
  takes care of opening the file when we call open() and then closing the 
  file after we leave the indented block.

 Why is closing the file so complicated? Well, most other aspects of our 
  code deal with things that Python itself controls. All the variables you 
  create: integers, lists, dictionaries — these are all Python objects, 
  and Python knows how to clean them up when it’s done with them. Since 
  your files exist outside your Python script, we need to tell Python when 
  we’re done with them so that it can close the connection to that file. 
  Leaving a file connection open unnecessarily can affect performance or 
  impact other programs on your computer that might be trying to access 
  that file.

The with syntax replaces older ways to access files where you need to call 
.close() on the file object manually. We can still open up a file and 
append to it with the old syntax, as long as we remember to close the file 
connection afterwards.

```python
with open("text.txt", "w") as textfile:
  textfile.write("Success!")

## Checking For Closure
with open("text.txt", "w") as my_file:
  my_file.write("Booger")

if my_file.closed:
  my_file.close()

print(my_file.closed)
```