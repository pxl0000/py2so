import os
import sys
import argparse
from py2so import compile_py

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('-F', '--from-path',
                        type=str,
                        metavar='FROM-PATH',
                        help='The directory to be compiled.',
                        dest='from_path',
                        required=True)
    parser.add_argument('-T', '--to_path',
                        type=str,
                        metavar='TO-PATH',
                        help='Compile the output directory.',
                        dest='to_path',
                        required=True)
    parser.add_argument('-f', '--file-name',
                        type=str,
                        metavar='FILE-NAME',
                        help='The name of the script to be compiled. The script must be in the directory that will be compiled.',
                        dest='file_name',
                        default='',
                        required=False)
    parser.add_argument('-e', '--exclude-list',
                        type=list,
                        metavar='EXCLUDE-LIST',
                        help='Scripts that do not participate in compilation.',
                        nargs='+',
                        dest='exclude_list',
                        default=[],
                        required=False)
    parser.add_argument('-c', '--del-c',
                        type=bool,
                        metavar='DEL-C',
                        help='Whether to delete the generated c file. Default: Yes.',
                        dest='del_c',
                        default=True,
                        required=False)
    parser.add_argument('-p', '--del-py',
                        type=bool,
                        metavar='DEL-PY',
                        help='Whether to delete the file ending with py. Default: Yes.',
                        dest='del_py',
                        default=True,
                        required=False)
    args = parser.parse_args()
    compile_py(from_path=args.from_path,
               to_path=args.to_path,
               file_name=args.file_name,
               exclude_list=args.exclude_list,
               del_c=args.del_c,
               del_py=args.del_py)
