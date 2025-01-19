
"""
"""

from core.synonyms import *


def map(*args, **wargs):
    """
    """
    if len(wargs) != 0: print('Pass uri by args'); raise NotImplemented
    from core.get.all import get_all_files_and_folders_recursive as files
    files = files()
    for file in files:
        from core.os.path import split
        import os
        base_name, ext = os.path.splitext(file)
        xff = split(base_name)
        all = []
        for xfe in xff:
            _ = 0
            aux = ''
            parts = []
            for c in xfe:
                if c == '_':
                    parts += [aux + f'.{ext}', portuguese.get(aux) + f'.{ext}', english.get(aux) + f'.{ext}']
                    aux = ''
                else:
                    aux += c
            from itertools import permutations
            all += [permutations(parts)]
        contents = []
        with open(file) as f:
            contents += [f.read()]
    if len(all) != len(contents):
        raise RuntimeError
    return all, contents