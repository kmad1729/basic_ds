'wap to check if sum exists in a list'

from __future__ import print_function
import argparse
import logging

logger = logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(message)s')

def check_sum_exists(s, tgt_sum):
    '''check for a tgt_sum of 2 unique elements in set s
    if such a tgt_sum exists, return the pair of elements, None otherwise
    '''
    result = None

    for elem in s:
        complement = tgt_sum - elem
        if complement != elem and (complement in s):
            result = (elem, complement)
            break

    return result


def count_tgt_sums_for_range(s, tgt_sum_min, tgt_sum_max):
    '''Count the number of tgt_sums in set s for a range of target_sums
    [tgt_sum_min, tgt_sum_max] inclusive
    '''

    logger = logging.getLogger('__main__')
    logger.debug('computing the number of target sums between {t_min} and {t_max}'.format(
        t_min = tgt_sum_min, t_max= tgt_sum_max))
    result = 0
    for i in range(tgt_sum_min, tgt_sum_max + 1):
        if check_sum_exists(s, i):
            result += 1

    return result


def build_inp_set_from_file(fname):
    '''build s set from a given input file with each line a number
    '''
    result = set()
    with open(fname, 'r') as f:
        for l in f:
            result.add(int(l))
    return result


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='count the number of tgt sums in'
            ' a given input file between a range of target_sums specified (inclusive)')
    parser.add_argument('f', help='file name')
    parser.add_argument('t_min', help='minimum target sum', type=int)
    parser.add_argument('t_max', help='maximum target sum', type=int)

    args = parser.parse_args()

    logger = logging.getLogger('__main__')
    logger.debug('started reading from input file {f}'.format(f=args.f))
    s = build_inp_set_from_file(args.f)
    logger.debug('build the set from the input file')
    print("number of target sums in file between target sums {t_min} and {t_max} "
        "in the file = {sol}".format(t_min=args.t_min, t_max=args.t_max,
            sol= count_tgt_sums_for_range(s, args.t_min, args.t_max)))
        



