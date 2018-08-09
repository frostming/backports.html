"""
Setup.py file
"""
import os
from setuptools import setup, find_packages

AUTHOR = 'Frost Ming'
EMAIL = 'mianghong@gmail.com'
URL = 'https://github.com/frostming/backports.html'

NAME = 'backports.html'
VERSION = '1.0.0'

here = os.path.dirname(__file__)
readme = open(os.path.join(here, 'README.md')).read()


setup(
    name=NAME,
    version=VERSION,
    description='Backport of Python 3.4+\'s html module',
    long_description=readme,
    long_description_content_type='text/markdown',
    author=AUTHOR,
    author_email=EMAIL,
    url=URL,
    license='MIT',
    packages=find_packages(exclude=('tests',)),
    test_suite='tests',
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
    ],
)
