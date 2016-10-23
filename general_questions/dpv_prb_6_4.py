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


def is_s_valid_word_seq(s):
    return True


class Test_is_s_valid_seq(unittest.TestCase):

    def test_1(self):
        test_cases = {
                "i" : True,
                "it" : True,
                "itw" : False,
                "itwa" : False,
                "itwas" : True,
                "itwasthebestoftimes" : True,
                }
        for i in test_cases:
            self.assertEquals(is_s_valid_word_seq(i), test_cases[i])


if __name__ == '__main__':
    unittest.main()



