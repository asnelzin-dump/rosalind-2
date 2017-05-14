import re
import sys


def find(genome, pattern):
    return [m.start() for m in re.finditer('(?=' + pattern + ')', genome)]


def main():
    pattern = input()
    try:
        f = open(sys.argv[1], 'r')
        try:
            genome = f.readline()[:-1]
        finally:
            f.close()
    except IOError:
        print("Error: Can't find file or read data")
    print(' '.join(str(i) for i in find(genome, pattern)))


if __name__ == '__main__':
    main()