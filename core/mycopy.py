
"""
tem um import do python chamado copy
"""

import shutil
def function(origin, final):
    if origin is list:
        for item in origin:
            import os
            final = os.path.join(final, os.path.basename(item))
            shutil.copy(item, final)
    elif origin is not list:
        raise NotImplemented
    else:
        raise NotImplemented