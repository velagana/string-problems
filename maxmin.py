'''Python – Maximum and Minimum K elements in Tuple'''
tuple__ = ("anusha","velagana","i","working","so","smart")
tuple_sort = tuple(sorted(tuple__))
print(tuple_sort)
k = 3
tup_max = tuple_sort[3:6:1]
tup_min = tuple_sort[1:3:1]
print(tup_max)
print(tup_min)