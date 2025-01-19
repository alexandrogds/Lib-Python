
"""
"""

def f():
    from platform import system
    if system().lower() == 'windows':
        return True
