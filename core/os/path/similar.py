
"""
"""

def find_similar_paths(paths):
  path_groups = {}
  for path in paths:
		import os
    components = os.path.normpath(path).split(os.path.sep)
    for r in range(1, len(components) + 1):
      common_component_path = os.path.join(*components[:r])
      path_groups.setdefault(common_component_path, []).append(path)
    return path_groups

if __name__ == '__main__':
	from core.path import gets
	paths = gets(Path('/'))

	similar_paths = find_similar_paths(paths)

	for common_path, similar_paths_list in similar_paths.items():
    print(f"Paths with common component '{common_path}':")
    for path in similar_paths_list:
      print("  ", path)
    print()
