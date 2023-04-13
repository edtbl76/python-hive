from isa import ISA
from memory import Memory, MainMemory

if __name__ == "__main__":
    cache_arch = ISA()
    # Write your code below
    cache_arch.set_memory(MainMemory())

    # Architecture runs the instructions
    cache_arch.read_instructions("ex2_instructions")

    # This outputs the memory data and code execution time
    exec_time = cache_arch.get_exec_time()
    if exec_time > 0:
        print(f"OUTPUT STRING: {cache_arch.output}")
        print(f"EXECUTION TIME: {exec_time:.2f} nanoseconds")

# EXPECTED OUTPUT:
#
# ISA memory: Main Memory
# lb r0 r1 - Main Memory read: M
# lb r0 r1 - Main Memory read: i
# lb r0 r1 - Main Memory read: s
# lb r0 r1 - Main Memory read: s
# lb r0 r1 - Main Memory read: i
# lb r0 r1 - Main Memory read: s
# lb r0 r1 - Main Memory read: s
# lb r0 r1 - Main Memory read: i
# lb r0 r1 - Main Memory read: p
# lb r0 r1 - Main Memory read: p
# lb r0 r1 - Main Memory read: i
# OUTPUT STRING: Mississippi
# EXECUTION TIME: 334.40 nanoseconds
# This example executed in main memory and it took 334ns
