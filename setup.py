#!/usr/bin/env python3
# fileencoding:utf-8

from setuptools import setup
from setuptools.command.test import test as TestCommand

class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True
    def run_tests(self):
        import pytest
        pytest.main(self.test_args)

setup(name='SQLiteater',
      version='0.0.1',
      description='Python3 SQLite3 parser.',
      author='Mogu',
      author_email='kbu94984@gmail.com',
      url='https://github.com/moguf/',
      packages=['seater'],
      package_dir={'seater':'sqliteater'},
      tests_require=['pytest'],
      cmdclass={'test':PyTest},
    )
