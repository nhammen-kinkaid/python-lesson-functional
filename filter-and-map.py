def is_int(x):
  return type(x) == int

def square(x):
  return x*x

my_list = [1, 2, 3.1, "4", "five", 6, 20]
only_ints = filter(is_int, my_list)
print(only_ints)
print(map(square, only_ints))
