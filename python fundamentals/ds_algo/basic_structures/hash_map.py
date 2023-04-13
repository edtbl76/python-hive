class HashMap:
    def __init__(self, array_size):
        self.array_size = array_size
        self.array = [None for element in range(self.array_size)]

    def hash(self, key, count_collisions=0):
        # break down key into list of bytes
        key_bytes = key.encode()

        # hash the bytes
        hash_code = sum(key_bytes)

        return hash_code + count_collisions

    def compressor(self, hash_code):

        return hash_code % self.array_size

    def assign(self, key, value):
        array_index = self.compressor(self.hash(key))
        current_array_value = self.array[array_index]

        # Case 1: Current Value is None
        if current_array_value is None:
            self.array[array_index] = [key, value]
            return

        # Case 2 : Same Key
        if current_array_value[0] == key:
            self.array[array_index] = [key, value]

        # Case 3: Different Key
        number_collisions = 1
        while current_array_value[0] != key:
            new_hash_code = self.hash(key, number_collisions)
            new_array_index = self.compressor(new_hash_code)
            current_array_value = self.array[new_array_index]
            # No Key
            if current_array_value is None:
                self.array[new_array_index] = [key, value]
                return
            # Same Key
            if current_array_value[0] == key:
                self.array[new_array_index] = [key, value]
                return

            number_collisions += 1
        return

    def retrieve(self, key):
        array_index = self.compressor(self.hash(key))
        possible_return_value = self.array[array_index]

        # Case 1: No Key
        if possible_return_value is None:
            return None

        # Case 2: Same Key
        if possible_return_value[0] == key:
            return possible_return_value[1]

        # Case 3: Different Key
        retrieval_collisions = 1
        while possible_return_value[0] != key:
            new_hash_code = self.hash(key, retrieval_collisions)
            retrieving_array_index = self.compressor(new_hash_code)
            possible_return_value = self.array[retrieving_array_index]

            if possible_return_value is None:
                return None

            if possible_return_value[0] == key:
                return possible_return_value[1]

            retrieval_collisions += 1
        return


# Driver Code
hash_map = HashMap(20)

hash_map.assign("gneiss", "metamorphic")
print(hash_map.retrieve("gneiss"))
