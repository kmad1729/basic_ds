from count_inversions import get_inversion

f_name = 'inp.txt'

data = []

with open(f_name, 'r') as f:
    for l in f.readlines():
        if l.strip():
            data.append(int(l))

print("ans = : {}".format(get_inversion(data)))
