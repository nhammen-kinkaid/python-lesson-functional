from functools import reduce

def my_square(x):
  return x*x

def my_sum(x, y):
  return x+y

my_list = [1, 2, 6, 9]
total = reduce(my_sum, my_list)
print(total)
print(reduce(my_sum, map(my_square, my_list)))
