#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
<<<<<<< HEAD
    a = len(tuple_a)
    b = len(tuple_b)
    sums = ((tuple_a[0] if a > 0 else 0) + (tuple_b[0] if b > 0 else 0),
            (tuple_a[1] if a > 1 else 0) + (tuple_b[1] if b > 1 else 0))
    return sums
=======
   a = len(tuple_a)
   b = len(tuple_b)
   sums = ((tuple_a[0] if a > 0 else 0) + (tuple_b[0] if b > 0 else 0),
           (tuple_a[1] if a > 1 else 0) + (tuple_b[1] if b > 1 else 0))
   return sums
>>>>>>> 744636b70e43c31a5f5367e095e6498725d6b6f4
# tuple_a += (0, 0)
# tuple_b += (0, 0)
# return (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
