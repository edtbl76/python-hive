from isa import ISA
from memory import Memory, MainMemory


class Cache(Memory):
    def __init__(self):
        # Write your code below
        super().__init__(name="Cache", access_time=0.5)

        # self.data represents 4 empty cache blocks
        self.data = [
            {"tag": None, "data": ""},
            {"tag": None, "data": ""},
            {"tag": None, "data": ""},
            {"tag": None, "data": ""}
        ]

    # Returns the cache total execution time
    def get_exec_time(self):
        return self.exec_time


if __name__ == "__main__":
    cache_arch = ISA()
    # Change the code below
    cache_arch.set_memory(Cache())

    # Architecture runs the instructions
    cache_arch.read_instructions("ex3_instructions")

    # This outputs the memory data and code execution time
    exec_time = cache_arch.get_exec_time()
    if exec_time > 0:
        print(f"OUTPUT STRING: {cache_arch.output}")
        print(f"EXECUTION TIME: {exec_time:.2f} seconds")


# EXPECTED OUTPUT:

# ISA memory: Cache
# lb r0 r1- NO DATA
# lb r0 r1 - Cache read: - NO DATA
# lb r0 r1 - Cache read: - NO DATA
# lb r0 r1 - Cache read: - NO DATA
# lb r0 r1 - Cache read: - NO DATA
# lb r0 r1 - Cache read: - NO DATA
# lb r0 r1 - Cache read: - NO DATA
# lb r0 r1 - Cache read: - NO DATA
# lb r0 r1 - Cache read: - NO DATA
# lb r0 r1 - Cache read: - NO DATA
# lb r0 r1 - Cache read: - NO DATA
# OUTPUT STRING:
# EXECUTION TIME: 9.90 seconds
# Notice this took ~10 seconds!
# We also got NO DATA!!!!
# WHY?????
# - Becauses there is currently no way to read data from teh cache.
