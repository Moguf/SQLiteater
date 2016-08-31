import os
import sys
import pytest
import unittest

sys.path.append(os.path.abspath('../sqliteater'))
from sqliteater import SQLiteater

class TestSQLiteater(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tclass = SQLiteater()
        
    def test_createTable_with_lists(self):
        tablename = 'test.db'
        namelist = ['name','weight','hight','location']
        typelist = [str, int, float, str]
        self.tclass.createTable(tablename, namelist, typelist)


if __name__ == '__name__':
    pass
