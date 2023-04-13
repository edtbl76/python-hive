- `isa.py:` implements a simple architecture including registers and a 
reference to the next level of memory in the hierarchy. The module also defines few memory access commands and allows for the reading of instructions from a file.
- `code.txt` is a group of instructions that the architecture will run for 
each exercise.
- `memory.py` defines the different memory types included in the architecture.
To start there is a generic memory class Memory() which the Register() and MainMemory() classes inherit from. The distinctive features of each memory type are the data size and the access time.
- `app.py` is the file you will use to configure the architecture and output 
important information regarding the memory access process.
- `cache.py` is where you will implement the cache. It is currently empty.