'''Given a string of n characters s[0...n), which we believe is a corrupted
text in which all punctuation is vanished. e.g "itwasthebestoftimes"
How do you reconstruct the document using a dictionary of valid words

Dictionary -> {"i", "it", "was", "the", "best"}
1) Give an algo that determines whether s can be reconstitueted as a sequence of valid words.
Eg:
    "i" -> True
    "it" -> True
    "itw" -> False
    "itwa" -> False
    "itwas" -> True
    "itwasthebestoftimes" -> True
'''

import unittest


def is_valid_word(s):
    words = {"i", "it", "was", "the", "best", "of", "times",
            "bed", "bath","and","beyond", "be"}
    return s in words


def is_s_valid_word_seq(s):
    l_s = list(s)
    util_arr = [False] * (len(l_s) + 1)
    util_arr[0] = True
    for i in range(len(l_s) + 1):
        for j in range(i+1):
            if util_arr[j-1]:
                if is_valid_word(''.join(s[j-1:i])):
                    util_arr[i] = True
                    break
    return util_arr[-1]


class Test_is_s_valid_seq(unittest.TestCase):

    def test_1(self):
        test_cases = {
                "i" : True,
                "it" : True,
                "itw" : False,
                "itwa" : False,
                "itwas" : True,
                "itwasthebestoftimes" : True,
                "iti":True,
                "wasbesti":True,
                "bedbathandbeyond":True,
                "bedbathandbe":True,
                }
        for i in test_cases:
            self.assertEqual(is_s_valid_word_seq(i), test_cases[i], 
                    "({s}) expected to be valid? {e}".format(s=i, e=test_cases[i]))


if __name__ == '__main__':
    unittest.main()



