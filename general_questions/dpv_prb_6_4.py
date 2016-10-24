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
from collections import deque


def is_valid_word(s):
    words = {"i", "a", "it", "was", "the", "best", "of", "times",
            "bed", "bath","and","beyond", "be", "tree", "about", "atrocious",
            "at",}
    return s in words


def _get_word_markers(s):
    l_s = list(s)
    util_arr = [False] * (len(l_s) + 1)
    util_arr[0] = True
    for i in range(len(util_arr)):
        for j in range(1, i+1):
            if util_arr[j-1]:
                if is_valid_word(''.join(l_s[j-1:i])):
                    util_arr[i] = True
                    break
    return util_arr

def get_word_tokens(s):
    result_words = deque()
    util_arr = _get_word_markers(s)
    markers = deque([len(util_arr)-1])
    for i in range(len(util_arr)-2, -1, -1):
        if util_arr[i]:
            if is_valid_word(s[i:markers[0]]):
                    markers.appendleft(i)

    while True:
        first = markers.popleft()
        if len(markers) == 0:
            break
        result_words.append(s[first:markers[0]])
    return result_words
    

def is_s_valid_word_seq(s):
    return _get_word_markers(s)[-1]


class Test_is_s_valid_seq(unittest.TestCase):

    def test_1(self):
        test_cases = {
                "i" : True,
                "j" : False,
                "it" : True,
                "itw" : False,
                "itwa" : False,
                "itwas" : True,
                "itwasthebestoftimes" : True,
                "iti":True,
                "wasbesti":True,
                "bedbathandbeyond":True,
                "bedbathandbe":True,
                "atrocious":True,
                "about":True,
                "a":True,
                "at":True,
                "atbed":True,
                }
        for i in test_cases:
            self.assertEqual(is_s_valid_word_seq(i), test_cases[i], 
                    "({s}) expected to be valid? {e}".format(s=i, e=test_cases[i]))

class Test_get_word_tokens(unittest.TestCase):
    def test_1(self):
        test_cases = {
                "i" : deque(['i']),
                "it" : deque(['it']),
                "atree" : deque(['a', 'tree']),
                "about" : deque(['about']),
                "atrocious" : deque(['atrocious']),
                "itwas" : deque(['it','was']),
                "itwasthebestoftimes" : deque(['it','was','the','best','of','times']),
                "iti": deque(['it','i']),
                "wasbesti": deque(['was','best','i']),
                "bedbathandbeyond": deque(['bed','bath','and','beyond']),
                "bedbathandbe": deque(['bed','bath','and','be']),
                "atbed":deque(['at','bed']),
                "atbe":deque(["at",'be']),
                "ati":deque(["at",'i']),
                }
        for i in test_cases:
            self.assertEqual(get_word_tokens(i), test_cases[i], 
                    "({s}) words was expected to be -> {e}".format(s=i, e=test_cases[i]))


if __name__ == '__main__':
    unittest.main()



