import os
import sys
import argparse
from py2so import compile_py

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('-f', '--from-path', action='store_const', const='from-path', dest='from-path')
    from_path = parser.parse_args()
    print(from_path)
