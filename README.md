# Py2so

## 说明


## 用法

```bash
usage: py2so [-h] -F FROM-PATH -T TO-PATH [-f FILE-NAME]
             [-e EXCLUDE-LIST [EXCLUDE-LIST ...]] [-c DEL-C] [-p DEL-PY]

Process some integers.

optional arguments:
  -h, --help            show this help message and exit
  -F FROM-PATH, --from-path FROM-PATH
                        The directory to be compiled.
  -T TO-PATH, --to_path TO-PATH
                        Compile the output directory.
  -f FILE-NAME, --file-name FILE-NAME
                        The name of the script to be compiled. The script must
                        be in the directory that will be compiled.
  -e EXCLUDE-LIST [EXCLUDE-LIST ...], --exclude-list EXCLUDE-LIST [EXCLUDE-LIST ...]
                        Scripts that do not participate in compilation.
  -c DEL-C, --del-c DEL-C
                        Whether to delete the generated c file. Default: Yes.
  -p DEL-PY, --del-py DEL-PY
                        Whether to delete the file ending with py. Default:
                        Yes.
```