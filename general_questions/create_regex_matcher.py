'''Create a regex matcher with support '.', '?'. and * 
Don't worry about malformed regexes '''

import unittest

def util_match_ptrn(ptrn, test_string, ptrn_start_ind):
    '''
    print("test_str = {}".format(test_string))
    print("ptrn[ptrn_start_ind:] = {}".format(ptrn[ptrn_start_ind:]))
    '''
    if len(ptrn) == ptrn_start_ind:
        return len(test_string) == 0

    if len(test_string) == 0:
        if any([x for x in ptrn[ptrn_start_ind:] if len(x) != 2]):
                return False
    
    curr_char = ptrn[ptrn_start_ind]
    if len(curr_char) == 1:
        '''
        print("ptrn[ptrn_start_ind] = ({})".format(ptrn[ptrn_start_ind]))
        print("test_string[0] = ({})".format(test_string[0]))
        print("ptrn[ptrn_start_ind] == test_string[0]? {}".format(
            ptrn[ptrn_start_ind] == test_string[0]))
        '''
        #no wild card
        if len(test_string) == 0:
            return False
        if (curr_char != test_string[0]):
            if (curr_char != '.'):
                return False
            else:
                return util_match_ptrn(ptrn, test_string[1:], ptrn_start_ind + 1)
        else:
            return util_match_ptrn(ptrn, test_string[1:], ptrn_start_ind + 1)
    else:
        if curr_char[-1] == '?':
            if len(test_string) == 0:
                return util_match_ptrn(ptrn, test_string, ptrn_start_ind + 1)

            if (curr_char[0] != test_string[0]):
                if (curr_char[0] == '.'):
                    return util_match_ptrn(ptrn, test_string[1:], ptrn_start_ind + 1) or \
                        util_match_ptrn(ptrn, test_string, ptrn_start_ind + 1)
                else:
                    return util_match_ptrn(ptrn, test_string, ptrn_start_ind + 1)

            else:
                return util_match_ptrn(ptrn, test_string[1:], ptrn_start_ind + 1) or \
                    util_match_ptrn(ptrn, test_string, ptrn_start_ind + 1)
        else:
            if len(test_string) == 0:
                return util_match_ptrn(ptrn, test_string, ptrn_start_ind + 1)
            for i in range(len(test_string) + 1):
                if curr_char[0] == '.':
                    if  util_match_ptrn(ptrn, test_string[i:], ptrn_start_ind + 1):
                        return True
                    else:
                        continue
                else:
                    if (curr_char[0] * i) == test_string[:i]:
                        if  util_match_ptrn(ptrn, test_string[i:], ptrn_start_ind + 1):
                            return True
                        else:
                            continue

    return False

def tokenize_inp_pattern(ptrn):
    result = []
    i = 0
    while i < len(ptrn):
        if i!= len(ptrn) - 1 and ptrn[i+1] in ['?', '*']:
            result.append(ptrn[i:i+2])
            i += 2
        else:
            result.append(ptrn[i:i+1])
            i += 1

    i = 0
    new_result = []
    while i < len(result):
        tok = result[i]
        if len(tok) == 2 and tok[0] != '.' and tok[-1] == '*':
            new_result.append(tok)
            i += 1
            while i < len(result) and result[i][-1] in ['?', '*'] and result[i][0] == tok[0]:
                i +=1
        else:
            new_result.append(tok)
            i += 1
        

    return new_result

def make_get_regex_match(test_string, ptrn):
    test_ptrn = tokenize_inp_pattern(ptrn)
    return util_match_ptrn(test_ptrn, test_string, 0)

class Test_MatchPtrn(unittest.TestCase):

    def test_basic_functionality(self):
        self.assertTrue(util_match_ptrn(list('abcd'), 'abcd', 0))
        self.assertTrue(util_match_ptrn(list('a.cd'), 'abcd', 0))
        self.assertFalse(util_match_ptrn(list('a.xd'), 'abcd', 0))
        lst = ['a', '.', 'x?', 'c?', 'd']
        self.assertTrue(util_match_ptrn(lst, 'abcd', 0))
        lst = ['a', '.', 'c?', 'd']
        self.assertTrue(util_match_ptrn(lst, 'abcd', 0))
        lst = ['a', 'x?', 'x?', 'd']
        self.assertFalse(util_match_ptrn(lst, 'abcd', 0))
        lst = ['a?', 'b', 'c?', 'd?']
        self.assertTrue(util_match_ptrn(lst, 'abcd', 0))
        lst = ['a', 'b', 'g?', 'c', 'd', 'f?', 'x?']
        self.assertTrue(util_match_ptrn(lst, 'abcd', 0))
        lst = ['a*', 'b', 'c*', 'd*']
        self.assertTrue(util_match_ptrn(lst, 'abcd', 0))
        lst = ['c*', 'd*']
        self.assertTrue(util_match_ptrn(lst, 'cd', 0))
        lst = ['.*']
        self.assertTrue(util_match_ptrn(lst, 'cd', 0))
        lst = ['c?.*']
        self.assertTrue(util_match_ptrn(lst, 'cccccccc', 0))

    def test_tokenize(self):
        self.assertEqual(['a', 'b', 'c', 'c'], tokenize_inp_pattern('abcc'))
        self.assertEqual(['a', 'b', 'c*', 'c'], tokenize_inp_pattern('abc*c'))
        self.assertEqual(['a', 'b', 'c*', 'c', 'd*'], tokenize_inp_pattern('abc*cd*'))
        self.assertEqual(['a?', 'b', 'c*','c'], tokenize_inp_pattern('a?bc*c'))
        self.assertEqual(['a?', 'b', 'c*', 'c', 'd*'], tokenize_inp_pattern('a?bc*cd*'))
        self.assertEqual(['.*', 'c'], tokenize_inp_pattern('.*c'))
        self.assertEqual(['c*', 'c'], tokenize_inp_pattern('c*c*c*c'))
        self.assertEqual(['.*', '.', '.', 'a*'], tokenize_inp_pattern('.*..a*'))


    def test_actual_code(self):
        self.assertTrue(make_get_regex_match('abcd', 'abcd'))
        self.assertTrue(make_get_regex_match('abcd', 'a?bcd'))
        self.assertTrue(make_get_regex_match('ab', '.*b'))
        self.assertFalse(make_get_regex_match('ab', '.*c'))
        #"aaaaaaaaaaaaab"
        #"a*a*a*a*a*a*a*a*a*a*c"
        self.assertFalse(make_get_regex_match("aaaaaaaaaaaaab", 
            "a*a*a*a*a*a*a*a*a*a*c"))
        self.assertFalse(make_get_regex_match("a", "..a*"))
        self.assertFalse(make_get_regex_match("a", ".."))
        self.assertTrue(make_get_regex_match("a", "."))
        #"a" ".*..a*" --> False
        self.assertFalse(make_get_regex_match("a", ".*..a*"))
        #"acaabbaccbbacaabbbb" "a*.*b*.*a*aa*a*" --> False
        self.assertFalse(make_get_regex_match("acaabbaccbbacaabbbb", "a*.*b*.*a*aa*a*"))
            


if __name__ == '__main__':
    unittest.main()
