import os
import time
import shutil
import platform
import copy
from distutils.core import setup
from Cython.Build import cythonize

DEFAULT_EXCLUDE_LIST = ['.idea', '.git', '.DS_Store', '.gitignore', '__pycache__']


def __py2so(from_path: str,
            to_path: str,
            file_name: str = '',
            exclude_list: list = None,
            del_c: bool = False,
            del_py: bool = True):
    """
    Py to so
    :param from_path:
    :param to_path:
    :param file_name:
    :param exclude_list:
    :param del_c:
    :param del_py:
    :return:
    """
    from_abs_path = os.path.join(os.path.abspath(from_path))
    print('From abs path is {}'.format(from_abs_path))
    to_abs_path = os.path.join(os.path.abspath(to_path))
    print('To abs path is {}'.format(to_abs_path))

    if not os.path.isdir(from_abs_path):
        raise ValueError('{} is not directory.'.format(from_abs_path))
    if not os.path.isdir(to_abs_path):
        os.makedirs(to_abs_path)

    if to_abs_path == from_abs_path:
        to_abs_path += '_compile'
        print('To abs path is {}'.format(to_abs_path))
        if not os.path.exists(to_abs_path):
            os.makedirs(to_abs_path)
        else:
            print('The file already exists.')

    from_file = os.path.join(from_abs_path, file_name)
    print('From file is {}'.format(from_file))
    to_file = os.path.join(to_abs_path, file_name)
    print('To file is {}'.format(to_file))

    if os.path.isfile(from_file):
        shutil.copyfile(from_file, to_file)

        ext = os.path.splitext(to_file)[1]

        if del_c and ext in ['.c']:
            os.remove(to_file)
        elif del_py and ext in ['.pyx', '.pyo']:
            os.remove(to_file)
        elif to_file not in exclude_list and os.path.splitext(to_file)[1] not in ('.pyc', '.pyx'):
            if os.path.splitext(to_file)[1] in ('.py', '.pyx') and not file_name.startswith('__'):
                script_args = ["build_ext",
                               "-b", os.path.abspath(os.path.dirname(to_file)),
                               "-t", os.path.abspath(os.path.dirname(to_file))]
                if platform.system().lower() == 'darwin':
                    script_args.append('-p')
                    script_args.append('macosx-10.14-x86_64')

                print('script args is {}'.format(script_args))
                setup(ext_modules=cythonize([to_file],
                                            compiler_directives={
                                                'language_level': 3
                                            }),
                      script_args=script_args)
                os.remove(to_file)
                os.remove(os.path.join(to_file, os.path.splitext(to_file)[0] + '.c'))
        return from_abs_path, to_abs_path
    else:
        from_abs_path = from_file
        to_abs_path = to_file

        if not os.path.exists(to_abs_path):
            os.makedirs(to_abs_path)
        else:
            print('The file already exists.')

        for fname in os.listdir(from_abs_path):
            print('fname is {}'.format(fname))
            __py2so(from_abs_path, to_abs_path, fname, exclude_list, del_c, del_py)

        return from_abs_path, to_abs_path


def __del_temp_dir(temp_dir: str,
                   del_list: list = []):
    """
    Delete redundant files
    :param temp_dir:
    :param del_list:
    :return:
    """
    temp_dir = os.path.abspath(temp_dir)
    print(temp_dir)
    for root, dirs, files in os.walk(temp_dir):
        print('root is {}'.format(root))
        print('dirs is {}'.format(dirs))
        print('files is {}'.format(files))
        for del_dir in list(set(del_list).intersection(set(dirs))):
            shutil.rmtree(os.path.join(root, del_dir))
        for del_file in list(set(del_list).intersection(set(files))):
            os.remove(del_file)


def compile_py(from_path,
               to_path,
               file_name='',
               exclude_list=[],
               del_c=False,
               del_py=True):
    """
    Compile
    :param from_path:
    :param to_path:
    :param file_name:
    :param exclude_list:
    :param del_c:
    :param del_py:
    :return:
    """
    start_time = time.time()
    from_abs_path, to_abs_path = __py2so(from_path, to_path, file_name, exclude_list, del_c, del_py)
    del_list = [os.path.split(os.environ['HOME'])[0][1:]]
    del_list.extend(DEFAULT_EXCLUDE_LIST)
    __del_temp_dir(to_abs_path, del_list)
    print("complete! time:", time.time() - start_time, 's')
