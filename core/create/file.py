
"""
"""

def function(filename):
    from os import getcwd
    with open(getcwd()+filename) as f:
        from os import path
        from core import create_all_file
        create_all_file(f, filename, path.splitext(filename)[1])
