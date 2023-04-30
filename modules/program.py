import sys
from my_mod import test

if __name__ == '__main__':
    if len(sys.argv) == 2:
        test(sys.argv[1])
    else:
        print('Usage: modules filename')

test('test.txt')