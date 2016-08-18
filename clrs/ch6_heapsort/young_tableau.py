'''Implement extract-min for a young's tableau 
Young tableau: Its an m X n matrix such that the entries of each row are 
sorted from left to right and each column are in sorted order from top to
bottom. Some of the entries may be infinity.
'''

LCL_INF = 2e9

def extract_min(yt):
    result = yt[0][0]
    yt[0][0] = LCL_INF
    min_young_tableaufy(yt, 0, 0)
    return result

def min_young_tableaufy(yt, r, c):
    m = len(yt)
    n = len(yt[0])
    assert (r < m and c < n)
    right_row, right_col = r, c + 1
    below_row, below_col = r + 1, c
    min_row, min_col = r, c

    if below_row < m and \
            yt[below_row][below_col] < yt[min_row][min_col]:
                min_row, min_col = below_row, below_col

    if right_col < n and \
            yt[right_row][right_col] < yt[min_row][min_col]:
                min_row, min_col = right_row, right_col

    if (min_row != r) or (min_col != c):
        yt[r][c], yt[min_row][min_col] = \
                yt[min_row][min_col], yt[r][c]
        min_young_tableaufy(yt, min_row, min_col)





import unittest

test_young_tableau = \
        [ [   2,    5,    8, LCL_INF],
          [   3,    9,   14, LCL_INF],
          [   4,   12,   16, LCL_INF],
          [ LCL_INF, LCL_INF, LCL_INF, LCL_INF],
        ]



