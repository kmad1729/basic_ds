
def _get_sign_indices(inp):
    signs = ['*', '-', '+']
    result = []
    for idx,c in enumerate(inp):
        if c in signs:
            result.append(idx)
    return result

def compute_diff_ways(inp):
    sign_indices = _get_sign_indices(inp)
    if len(sign_indices) <= 1:
        return [eval(inp)]
    idx = 0
    curr_result = []
    while idx < len(sign_indices):
        before = compute_diff_ways(inp[:sign_indices[idx]])
        after = compute_diff_ways(inp[(sign_indices[idx] + 1):])
        for b in before:
            for a in after:
                curr_result.append(eval(
                    str(b) + inp[sign_indices[idx]] + str(a)))
        idx += 1
    return curr_result


print(compute_diff_ways('2-1'))
print(compute_diff_ways('2'))
print(compute_diff_ways('2-1-1'))
print(compute_diff_ways("2*3-4*5"))
print(compute_diff_ways("2+4*3-4*5"))

