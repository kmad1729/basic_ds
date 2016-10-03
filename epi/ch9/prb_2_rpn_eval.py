'''write a program that takes an arithematic expression in RPN and
returns the number that the expression evaluates to
'''

import unittest

OPERATORS=['+','*','/','-']
def rpn_eval(expression):
    utils_stack = []
    for c in expression.split(','):
        if c in OPERATORS:
            a = utils_stack.pop()
            b = utils_stack.pop()
            output = eval(a + c + b)
            utils_stack.append(str(output))
        else:
            utils_stack.append(c)
    assert len(utils_stack) == 1
    return utils_stack.pop()




class Test_RPN_Eval(unittest.TestCase):
    def test_basic(self):
        test_cases = {
                '2,3,*':'6',
                '3,4,+,2,*,1,+':'15',
                '-641,6,/,28,/':'-4',
                }

        for expression, result in test_cases.items():
            self.assertEquals(result, rpn_eval(expression),
                    '{e} did not evaluate to {a}'.format(e=expression,
                        a=result))

if __name__ == '__main__':
    unittest.main()
