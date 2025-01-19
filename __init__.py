
"""
"""

import os; import sys; import ctypes
from . import get_int
get_int = get_int.function
sys.setrecursionlimit(ctypes.CDLL(get_int()).max())

from . import load_env

from . import framework
framework = framework.function

from . import version
version = version.function

from . import ls
ls = ls.function

from . import ext
ext = ext.function
get_ext_lib = ext

from . import search_files_and_subfolders
search_files_and_subfolders = search_files_and_subfolders.function

from . import get_all_files_and_folders_recursive
get_all_files_and_folders_recursive = get_all_files_and_folders_recursive.function

from . import get_all_subfiles
get_all_subfiles = get_all_subfiles.function

from . import get_all_files_and_folders_recursive_ls
get_all_files_and_folders_recursive_ls = get_all_files_and_folders_recursive_ls.function

from . import process_gets_files_and_foldes_of_ls_command
process_gets_files_and_foldes_of_ls_command = process_gets_files_and_foldes_of_ls_command.function

from . import get_paths_relative_of_files_recursive
get_paths_relative_of_files_recursive = get_paths_relative_of_files_recursive.function

from . import convert_paths_to_case_sensitive_names
convert_paths_to_case_sensitive_names = convert_paths_to_case_sensitive_names.function

from . import generate_components_laravel_of_views
generate_components_laravel_of_views = generate_components_laravel_of_views.function

from . import ls_recursive_of_files_python
ls_recursive_of_files_python = ls_recursive_of_files_python.function

from . import process_get_paths_of_files_of_ls_command
process_get_paths_of_files_of_ls_command = process_get_paths_of_files_of_ls_command.function

from . import get_paths_of_all_files_recursive_ls
get_paths_of_all_files_recursive_ls = get_paths_of_all_files_recursive_ls.function

from . import get_name_of_import_blade_laravel
get_name_of_import_blade_laravel = get_name_of_import_blade_laravel.function

from . import transcode_call_component_blade_file_hierarchy_to_class_component
transcode_call_component_blade_file_hierarchy_to_class_component = transcode_call_component_blade_file_hierarchy_to_class_component.function

from . import get_paths_of_files_recursive
get_paths_of_files_recursive = get_paths_of_files_recursive.function

from . import web_crawler
web_crawler = web_crawler.web_crawler

from . import count_files_recursive
count_files_recursive = count_files_recursive.function

from . import count_keys_in_files_recursive
count_keys_in_files_recursive = count_keys_in_files_recursive.function

from . import map
map = map.f
from . import indentar
indentar = indentar.f