from isa import ISA
from memory import Memory, MainMemory


class Cache(Memory):
    def __init__(self):
        super().__init__(name="Cache", access_time=0.5)

        # Cache Blocks are populated
        # This means that we'll have cache hits.
        self.data = [
            {"tag": 0, "data": "M"},
            {"tag": 1, "data": "i"},
            {"tag": 2, "data": "s"},
            {"tag": 3, "data": "p"},
        ]

    # This is a new method that didn't exist in previous
    # examples.
    def read(self, address):
        super().read()
        data = None
        # Write your code below
        entry = self.get_entry(address)
        if entry is not None:
            data = entry["data"]
        return data

    # Returns entry on cache hit
    # Returns None on cache miss
    def get_entry(self, address):
        for entry in self.data:
            if entry["tag"] == address:
                print(f"HIT: ", end="")
                return entry

        print(f"MISS", end="")
        return None

    def get_exec_time(self):
        return self.exec_time


if __name__ == "__main__":
    cache_arch = ISA()
    cache_arch.set_memory(Cache())

    # Architecture runs the instructions
    cache_arch.read_instructions("ex4_instructions")

    # This outputs the memory data and code execution time
    exec_time = cache_arch.get_exec_time()
    if exec_time > 0:
        print(f"OUTPUT STRING: {cache_arch.output}")
        print(f"EXECUTION TIME: {exec_time:.2f} nanoseconds")


# OUTPUT

# ISA memory: Cache
# lb r0 r1 - Cache read: HIT: M
# lb r0 r1 - Cache read: HIT: i
# lb r0 r1 - Cache read: HIT: s
# lb r0 r1 - Cache read: HIT: s
# lb r0 r1 - Cache read: HIT: i
# lb r0 r1 - Cache read: HIT: s
# lb r0 r1 - Cache read: HIT: s
# lb r0 r1 - Cache read: HIT: i
# lb r0 r1 - Cache read: HIT: p
# lb r0 r1 - Cache read: HIT: p
# lb r0 r1 - Cache read: HIT: i
# OUTPUT STRING: Mississippi
# EXECUTION TIME: 9.90 nanoseconds

# Now that the cache can be read from, we get HIT instead of NO DATA
# AND we return the value.
# Execution time is 10 NANOseconds, which is much faster.

