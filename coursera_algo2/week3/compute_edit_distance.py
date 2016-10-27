'''Given 2 strings of size m and n, compute the similarity measure
between them. E.g. For words SUNNY, SNOWY edit distance = 3
S U N N Y
S N O W Y
- * * * -

For words,  SUNNY, SUNNY edit distance = 0
S U N N Y
S U N N Y

'''

import unittest
from collections import deque

def _get_similarity_table(s1, s2, alpha_gap=1):
    m = len(s1)
    n = len(s2)

    similarity_table = [ [None] * (n + 1) for i in range(m + 1)]
    for i in range(m+1):
        similarity_table[i][0] = i * alpha_gap
    for i in range(n + 1):
        similarity_table[0][i] = i * alpha_gap

    for i in range(1, m+1):
        for j in range(1, n+1):
            x = s1[i-1]
            y = s2[j-1]
            diff_x_y = 1 if x != y else 0
            similarity_table[i][j] = min(
                    diff_x_y + similarity_table[i-1][j-1],
                    alpha_gap + similarity_table[i-1][j],
                    alpha_gap + similarity_table[i][j-1])
    return similarity_table

def get_edit_distance(s1, s2, alpha_gap=1):
    return _get_similarity_table(s1,s2)[-1][-1]

def get_difference_string(s1, s2, alpha_gap=1):
    '''For s1 and s2 compute the diff string. E.g
    For s1="SUNNY", s2="SUNNY" -> ["S","U","N","N","Y"]
    For s1="SUNNY", s2="SNOWY" -> ["S", ("U","N"), ("N","O"),("N","W"),"Y"]
    For s1="DOG", s2="FOG" -> [("D","F"), "O", "G"]
    For s1="OG", s2="FOG" -> [("_", "F"),"O","G"]
    '''

    sim_table = _get_similarity_table(s1,s2,alpha_gap)
    m = len(s1)
    n = len(s2)
    i = m
    j = n
    result = deque()

    while i > 0 or j > 0:
        if i == 0:
            result.appendleft(('_', s2[j-1]))
            j -= 1
        elif j == 0:
            result.appendleft((s1[i-1], '_'))
            i -= 1
        else:
            x = s1[i-1]
            y = s2[j-1]
            if x == y:
                result.appendleft(x)
                i -= 1
                j -= 1
            else:
                if sim_table[i][j] == 1 + sim_table[i-1][j-1]:
                    result.appendleft((x,y))
                    i -= 1
                    j -= 1
                elif sim_table[i][j] == alpha_gap + sim_table[i-1][j]:
                    result.appendleft((x, '_'))
                    i -= 1
                elif sim_table[i][j] == alpha_gap + sim_table[i][j-1]:
                    result.appendleft(('_',y))
                    j -= 1
    return result

                    



class Test_compute_edit_distance(unittest.TestCase):
    def test_same_string(self):
        s1 = "SUNNY"
        s2 = "SUNNY"
        self.assertEqual(0, get_edit_distance(s1, s2))

    def test_similar_string(self):
        s2 = "SNOWY"
        s1 = "SUNNY"
        self.assertEqual(3, get_edit_distance(s1, s2))

    def test_similar_string1(self):
        s2 = "DOG"
        s1 = "FOG"
        self.assertEqual(1, get_edit_distance(s1, s2))
    def test_similar_string2(self):
        s2 = "DOG"
        s1 = "OG"
        self.assertEqual(1, get_edit_distance(s1, s2))

class Test_get_diff_string(unittest.TestCase):

    def test_same_string(self):
        s1 = "DOG"
        s2 = "DOG"
        exp_result = deque(["D", "O", "G"])
        self.assertEqual(exp_result, get_difference_string(s1, s2))

    def test_one_diff_letter(self):
        s1 = "DOG"
        s2 = "FOG"
        exp_result = deque([("D", "F"), "O", "G"])
        self.assertEqual(exp_result, get_difference_string(s1, s2))

    def test_one_letter_missing(self):
        s1 = "DOG"
        s2 = "OG"
        exp_result = deque([("D", "_"), "O", "G"])
        self.assertEqual(exp_result, get_difference_string(s1, s2))

    def test_one_letter_missing1(self):
        s1 = "OG"
        s2 = "DOG"
        exp_result = deque([("_", "D"), "O", "G"])
        self.assertEqual(exp_result, get_difference_string(s1, s2))

if __name__ == "__main__":
    unittest.main()
