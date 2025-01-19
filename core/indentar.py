
"""
"""

def f(*args, **wargs):
    if len(wargs) != 0: print('Pass uri by args'); raise NotImplemented
    from core.path.recursive import get_paths_of_all_files_recursive_ls as files
    files = files()
    for file in files:
        content = ''
        with open(file) as f:
            space = None
            for line in f:
                if line[0] == ' ':
                    space = 1
                elif line[0] == '\t':
                    space = 0
                if space == 1:
                    count = 0
                    for c in line:
                        if c == ' ':
                            count += 1
                        else:
                            break
                        if c == 4:
                            content += '\t'
                            c = 0
        with open(file, 'w') as f: f.write(content)