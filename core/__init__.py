
"""
"""

from argparse import Namespace
import getpass
import os

from . import getcwd
getcwd = getcwd.function

from . import load_env
#load_env = load_env.function

from core.create import file
Create = Namespace()
Create.file = file

from core.create import all_file
create_all_file = all_file

from core.create.file import batch
create_file_batch = batch

import platform
system = platform.system().lower()
windows = 'windows'

from . import indentar
indentar = indentar.f

from meta import implements
implements = implements.f