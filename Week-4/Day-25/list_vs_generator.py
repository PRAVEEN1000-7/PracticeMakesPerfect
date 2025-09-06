# Q : Compare generator vs list performance with large data.

# List vs Generator

# List:
# - Stores all values in memory
# - Faster (pre-computed)
# - Uses more memory

# Generator:
# - Produces values one by one (lazy)
# - Slower (computes on the fly)
# - Very memory efficient


import sys

list_num = [ i for i in range(100_00_000)]
print("List size :",sys.getsizeof(list_num)) # ~85 MB

gen_num = ( i for i in range(100_00_000))
print("Generator size :",sys.getsizeof(gen_num)) # ~200 bytes