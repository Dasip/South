import sys
import argparse
from mygeocoder import get_coordinates as get_core


def CreateParser():
    parser = argparse.ArgumentParser()
    parser.add_argument('arg', nargs='*', default=['no args'])
    
    return parser


if __name__ == '__main__':
    parser = CreateParser()
    namespace = parser.parse_args(sys.argv[1:])
    a = ''.join(namespace.arg).split(',')
    a = list(map(lambda x: [x, get_core(x)[1]], a))
    a.sort(key=lambda x: x[1])
    print(a[0][0])
