"""
"""
def function(*args, **wargs):
  """
  """
  from get_all_files_recursive_ls import function as get_all_files_recursive_ls
  _ = get_all_files_recursive_ls(*args, **wargs)
  for i in range(len(_)):
    _[i] = _[i].replace(args[0], '')
    if _[i][0] == '/':
      _[i] = _[i][1:]
  return _