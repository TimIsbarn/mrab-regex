#!/usr/bin/env python
from setuptools import setup, Extension
from os.path import join

with open('README.rst', encoding='utf-8') as file:
    long_description = file.read()

setup(
    name='regex',
    version='2024.5.5',
    description='Alternative regular expression module, to replace re.',
    long_description=long_description,
    long_description_content_type='text/x-rst',
    author='Matthew Barnett',
    author_email='regex@mrabarnett.plus.com',
    url='https://github.com/mrabarnett/mrab-regex',
    license='Apache Software License',

    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Topic :: Scientific/Engineering :: Information Analysis',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Text Processing',
        'Topic :: Text Processing :: General',
    ],
    python_requires='>=3.8',

    package_dir={'regex': 'regex_3'},
    py_modules=['regex.__init__', 'regex.regex', 'regex._regex_core',
     'regex.test_regex'],
    ext_modules=[Extension('regex._regex', [join('regex_3', '_regex.c'),
      join('regex_3', '_regex_unicode.c')])],
)
