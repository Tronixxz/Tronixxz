

# import sys

# # Example objects
# string = "Hello, world!"


# # Get the size of each object
# size_string = sys.getsizeof(string)


# # Print the sizes
# print("Size of string:", size_string, "bytes")

# dujikospl
# import sys
# l = [1, 2, 3, 4, 5]
# size = sys.getsizeof(l)
# print(size)

# import sys
# l = [x for x in range(100)]
# # for i in l:
# #     print(i**2)
# size = sys.getsizeof(l)
# print(size)

# Iterator Example//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# import sys
# x = range(10000000000)
# # for i in x:
# #     print(i**2)
# size = sys.getsizeof(x)
# print(size)

# Python generator example///////////////////////////////////////////////////

def gen_demo():
    yield "first statement"
    yield "second statement"
    yield "third statement"


gen = gen_demo()
print(next(gen))
print(next(gen))
print(next(gen))

