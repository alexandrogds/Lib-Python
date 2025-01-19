
"""
"""

def f(*args, **wargs):
    """
    """
    if len(wargs) != 0: print('Pass uri by args'); raise NotImplemented
    from core.ls import get_paths_of_all_files_recursive_ls as ls
    from core.ls._process import get_last_dirfiles as xff
    return xff(ls(*args, **wargs))