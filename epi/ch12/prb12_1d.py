'search if a word has prefix p in a sorted list of words'


import unittest

def get_if_prefix_exists(wrd_list, p):
    l, u = 0, len(wrd_list) - 1
    while l <= u:
        m = l + (u - l) // 2
        mid_word = wrd_list[m]
        if len(mid_word) >= len(p):
            if mid_word.startswith(p):
                return m
            else:
                if p < mid_word:
                    u = m - 1
                else:
                    l = m + 1
        else:
            if p[:len(mid_word)] < mid_word:
                u = m - 1
            else:
                l = m + 1

    return -1



class Test_GetIfPrefixExists(unittest.TestCase):

    def test_basic_functionality(self):
        wrd_list = ["abate", "abhor", "abhorrent", "apple", "application", "aqueuous",
                "aquine", "arise", "art", "articulate", "astute", "asymptotic",
                "azure", "axe"]

        positive_words = ["art", "ar", "articulate", "app", "ab", "asy", "ast"]
        for w in positive_words:
            result = get_if_prefix_exists(wrd_list, w)
            print("prefix {} exists in word {}".format(w, wrd_list[result]))
            self.assertTrue(result != -1)

        negative_words = ["arthur", "arm", "apall", "ask"]

        for w in negative_words:
            result = get_if_prefix_exists(wrd_list, w)
            print("prefix exists at {}".format(result))
            self.assertTrue(result == -1)

    def test_all_inp_list_same(self):
        lst = ["apple"] * 10
        self.assertTrue(get_if_prefix_exists(lst, "app") != -1)
        self.assertTrue(get_if_prefix_exists(lst, "apc") == -1)

if __name__ == '__main__':
    unittest.main()
