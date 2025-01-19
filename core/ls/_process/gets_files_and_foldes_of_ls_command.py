
"""
"""

def function(*args, **wargs):
    """
    """
    folder = None
    r = []
    for line in args[0].split('\n'):
        if line.strip() == '':
            continue
        if line[0] == '/':
            folder = line
            r += [folder[:-1]]
        else:
            import os
            r += [os.path.join(folder[:-1], line[:])]
    return r
