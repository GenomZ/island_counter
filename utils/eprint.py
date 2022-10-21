import sys


def eprint_and_quit(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)
    sys.exit()
