

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

# def gen_demo():
#     yield "first statement"
#     yield "second statement"
#     yield "third statement"


# gen = gen_demo()
# print(next(gen))
# print(next(gen))
# print(next(gen))

# Range Function Using Generators//////////////////////////////////////////////

 
# def mera_range(start, end):
#     for i in range(start, end):
#         yield i

# gen = mera_range(15, 26)
# for i in gen:
#     print(i)

# Generator Expression//////////////////////////////////////////////////////
# import sys
# gen = (i**2 for i in range(1,10000))
# # for i in gen:
# #     print(i)
# size = sys.getsizeof(gen)
# print(size)

# Representing Infinite Stream/////////////////////////////////////////////

# def all_even():
#     n=0
#     while True:
#         yield n
#         n +=2
#         even_num_gen = all_even()
#         next(even_num_gen)

