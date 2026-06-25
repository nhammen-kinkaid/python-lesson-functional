my_list = [1, 2, 3.1, "4", "five", 6, 20]
only_ints = list(filter(lambda x: type(x)==int, my_list))
print(only_ints)
print(map(lambda z: z*z, only_ints))
print(reduce(lambda x,y: x+y, map(lambda z: z*z, only_ints)))
