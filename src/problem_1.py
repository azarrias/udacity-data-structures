from collections import OrderedDict

class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        self.capacity = capacity
        self.data = OrderedDict()

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent. 
        if key in self.data:
            self.data.move_to_end(key)
            return self.data[key]
        else:
            return -1

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item. 
        if key not in self.data and len(self.data) >= self.capacity:
            self.data.popitem(last = False)
        self.data[key] = value
        self.data.move_to_end(key)

def eval_test(test_number, expected_output_str, actual_output_str):
    print("")
    print("TEST CASE " + str(test_number))
    print("===========")
    print("- expected output:")
    print(expected_output_str)
    print("- actual output:")
    print(actual_output_str)
    print("")

# test case 1
our_cache = LRU_Cache(5)
our_cache.set(1, "a")
our_cache.set(2, "b")
our_cache.set(3, "c")
our_cache.set(4, "d")
our_cache.set(5, "e") 
our_cache.set(4, "z") 
result = our_cache.get(1)
eval_test(1, "a", result)

# test case 2
our_cache = LRU_Cache(3)
our_cache.set(1, 10)
our_cache.set(2, 20)
our_cache.set(3, 30)
our_cache.set(4, 40)
result = our_cache.get(1)
eval_test(2, "-1", result)

# test case 3
our_cache = LRU_Cache(3)
our_cache.set(1, 10)
our_cache.set(2, 20)
our_cache.set(3, 30)
our_cache.get(1)
our_cache.set(4, 40)
result = our_cache.get(2)
eval_test(3, "-1", result)