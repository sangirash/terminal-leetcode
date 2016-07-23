import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

requirements = ['urwid', 'requests', 'bs4']

setup(
    name = "terminal-leetcode",
    version = "0.0.1",
    author = "Liyun Xiu",
    author_email = "chishui2@gmail.com",
    description = ("An demonstration of how to create, document, and publish "
                                   "to the cheese shop a5 pypi.org."),
    license = "MIT",
    keywords = "leetcode terminal urwid",
    url = "https://github.com/chishui/terminal-leetcode",
    packages=['leetcode'],
    long_description=read('README.md'),
    install_requires=requirements,
    entry_points={'console_scripts': ['leetcode=leetcode.__main__:main']},
    #classifiers=[
        #"Operating System :: MacOS :: MacOS X",
        #"Operating System :: POSIX",
        #"Natural Language :: English",
        #"Programming Language :: Python :: 2.7",
        #"Development Status :: 2 - Pre-Alpha",
        #"Environment :: Console :: Curses",
        #"Topic :: Utilities",
        #"Topic :: Terminals",
        #"License :: OSI Approved :: MIT License",
    #],
)