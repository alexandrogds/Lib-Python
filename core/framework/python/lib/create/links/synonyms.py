
"""
"""

def function(uri='.'):
	from path.recursive import get as paths
	for path in paths(uri):
		components = []
		while True:
			import os
			path, component = os.path.split(path)
			if component:
				components.insert(0, component)
			else:
				break
		from english.synonyms import get as synonyms
		for component in components:
			for i in range(len(component)):
				synonyms(component[i])

		combinations = []
		for r in range(1, len(components) + 1):
			from itertools import permutations
			combinations = permutations(components, len(components))
			combinations.extend(combinations)
		paths = [os.path.join(*combo) for combo in combinations]
