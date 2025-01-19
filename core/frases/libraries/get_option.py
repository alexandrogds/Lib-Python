def f(a99):
	try:
		return int(input(a99))
	except:
		return f(a99)
get_option=f
