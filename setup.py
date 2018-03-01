#!/usr/bin/env python
import os
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup_args = {}
install_requires = ['param>=1.5.1', 'bokeh>=0.12.10']

setup_args.update(dict(
    name='parambokeh',
    version="0.2.2",
    install_requires = install_requires,
    url = 'https://github.com/ioam/parambokeh',
    description='ParamBokeh provides an easy way to generate a UI for param based classes in the notebook or on bokeh server.',
    long_description=open('README.rst').read() if os.path.isfile('README.rst') else 'Consult README.rst',
    author= "IOAM",
    author_email= "holoviews@gmail.com",
    maintainer= "IOAM",
    maintainer_email= "holoviews@gmail.com",
    platforms=['Windows', 'Mac OS X', 'Linux'],
    packages = ["parambokeh"],
    provides = ["parambokeh"],
))


if __name__=="__main__":
    if ('upload' in sys.argv) or ('sdist' in sys.argv):
        import parambokeh
        parambokeh.__version__.verify(setup_args['version'])

    setup(**setup_args)
