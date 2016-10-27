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

def get_edit_distance(s1, s2, alpha_gap = 1):
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

    return similarity_table[-1][-1]

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

if __name__ == "__main__":
    unittest.main()
