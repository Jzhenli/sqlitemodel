#!/usr/bin/env python

import sys
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

if sys.version_info < (2, 6):
    raise NotImplementedError("Sorry, you need at least Python 2.6 or Python 3.2+ to use sqlitemodel.")

import sqlitemodel

setup(name='sqlitemodel',
      version=sqlitemodel.__version__,
      description='Wrapper for the sqlite3 database that enables you to create models you can easily query, save and update.',
      long_description='py-sqlite-model is a database wrapper for the sqlite3 database that enables you to create models you can easily query, save and update.',
      author='Rene Tanczos',
      author_email='gravmatt@gmail.com',
      url='https://github.com/gravmatt/sqlitemodel',
      py_modules=['sqlitemodel'],
      scripts=['sqlitemodel.py'],
      license='MIT',
      platforms='any',
      classifiers=['Intended Audience :: Developers',
                   'License :: OSI Approved :: MIT License',
                   'Programming Language :: Python :: 2.5',
                   'Programming Language :: Python :: 2.6',
                   'Programming Language :: Python :: 2.7',
                   'Programming Language :: Python :: 3',
                   'Programming Language :: Python :: 3.2',
                   'Programming Language :: Python :: 3.3',
                   ],
      )
