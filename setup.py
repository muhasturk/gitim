from setuptools import setup, find_packages
try:
    from itertools import imap, ifilter
except ImportError:
    imap = map
    ifilter = filter
from os import path
from ast import parse

if __name__ == '__main__':
    package_name = 'gitim'

    get_vals = lambda var0, var1: imap(lambda buf: next(imap(lambda e: e.value.s, parse(buf).body)),
                                       ifilter(lambda line: line.startswith(var0) or line.startswith(var1), f))

    with open('gitim.py') as f:
        __author__, __version__ = get_vals('__version__', '__author__')

    setup(
        name=package_name,
        author=__author__,
        version=__version__,
        license='MIT',
        install_requires=['pygithub'],
        py_modules=['gitim']
    )
