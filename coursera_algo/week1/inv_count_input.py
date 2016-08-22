from count_inversions import get_inversion
import pickle
import os

f_name = 'inp.txt'

data = []

with open(f_name, 'r') as f:
    for l in f.readlines():
        if l.strip():
            data.append(int(l))

ans = get_inversion(data)
assert ans == 2407905288
print("ans = : {}".format(ans))
