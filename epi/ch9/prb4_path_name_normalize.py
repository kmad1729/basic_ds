'''Normalize a path name and find the final path
e.g /ab/de/d/../.././../cd --> /cd

beware of invalid pathnames
/../ --> Exception
abc/../../ --> exception

'''
import unittest
from collections import deque

def normalize_path_names(pth):
    if pth == '':
        raise Exception("Empty path name is not valid")
    util_stack = ['/'] if pth[0] == '/' else []

    for directory in pth.split('/'):
        if directory == '.' or directory == '':
            continue
        elif directory == '..':
            if len(util_stack) == 0 or util_stack[-1] == '..':
                util_stack.append('..')
            else:
                if util_stack[-1] == '/':
                    raise Exception("Invalid path name")
                util_stack.pop()
        else:
            util_stack.append(directory)

    if util_stack[0] == '/':
        return '/'.join([''] + util_stack[1:])
    else:
        return '/'.join(util_stack)





class Test_path_name_normalize(unittest.TestCase):

    def test_basic_valid_cases(self):
        test_cases = {
                '/ab/de/d/../.././../cd':'/cd',
                'ab/cd/ef': 'ab/cd/ef',
                'ab':'ab',
                '/ab/cd':'/ab/cd',
                '/ab/..':'/',
                'ab/cd/..///':'ab',
                '//////':'/',
                '/./././//':'/',
                'ab/////..':'',
                'ab/cd/../../':'',
                'ab/cd/..///../':'',
                'ab/cd/..///../..':'..',
                '../':'..',
                '..':'..',
                }

        for tc, exp_out in test_cases.items():
            self.assertEqual(exp_out, normalize_path_names(tc),
                'expected "{e}" for path name "{p}"'.format(e=exp_out, p=tc))

    def test_invalid_cases(self):
        invalid_paths = [
                '',
                '/..',
                '/////..//',
                ]
        for pth in invalid_paths:
            print("checking path {p}".format(p=pth))
            self.assertRaises(Exception, normalize_path_names, pth)


if __name__ == '__main__':
    unittest.main()
