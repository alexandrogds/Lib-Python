
"""
"""

def function(*args, **wargs):
	"""wargs[path, mode(commits,issues,commits == issues),issues=tag]"""
	from core import map_wargs, commits_title, issues
	map_wargs(**wargs)
	if mode != COMMIT_EQUALS_ISSUES:
		raise NotImplementedError
	commits = commits_title(path=project, grep="#[0-9]* ")
	issues = issues(path=project, label=issues, status='closed')
	eval(mode)
	if len(_0.split('\n')) != len(_1.split('\n')):
		raise NotImplementedError
	return _0

COMMIT_EQUALS_ISSUES = 'commits == issues'