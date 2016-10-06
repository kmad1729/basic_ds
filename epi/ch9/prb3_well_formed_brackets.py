'''A string over the characters "{,},(,),[,]" is said to be well-formed if the
different types of brackets match in the CORRECT ORDER.
W.A.P that tests if a string is well-formed
E.g. 
(()) <- well-formed
([{}{}{}])() <- well-formed
({ <- not well-formed
[([[)]]] <- not well-formed
'''

import unittest

def is_well_formed(inp_str):
    util_stack = []
    for c in iter(inp_str):
        if c in ['}', ')', ']']:
            if len(util_stack) == 0:
                return False
            if c == '}' and util_stack[-1] != '{':
                return False
            elif c == ')' and util_stack[-1] != '(':
                return False
            elif c == ']' and util_stack[-1] != '[':
                return False
            else:
                util_stack.pop()
        else:
            util_stack.append(c)

    return len(util_stack) == 0

class Test_well_formedness(unittest.TestCase):
    def test_basic(self):
        test_cases = {
                '(())': True,
                '([{}{}{}])()': True,
                '({' : False,
                '[([[)]]]' : False,
                '[[([[]])][]]' : True,
                '[((){[[]{}]}){}{}]': True,
                }

        for inp_str, expected in test_cases.items():
            self.assertEquals(expected, is_well_formed(inp_str),
                    'expected {e} did not match function output "{s}"'.format(
                        e=expected, s=inp_str))


if __name__ == '__main__':
    unittest.main()

