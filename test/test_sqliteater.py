import os
import sys
import pytest
import unittest

sys.path.append(os.path.abspath('./sqliteater'))
sys.path.append(os.path.abspath('../sqliteater'))

import sqliteater

class TestSQLiteater(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tclass = sqliteater.SQLiteater()
        
    def test_createTable_with_lists(self):
        tablename = 'test.db'
        namelist = ['name','weight','hight','location']
        typelist = [str, int, float, str]
        self.assertTrue(self.tclass.createTable(tablename, namelist, typelist))

    def test_createTable_with_different_length_lists(self):
        tablename = 'test.db'
        namelist = ['name','weight','hight','location']
        typelist = [str, int, float]
        self.assertRaises(Exception, self.tclass.createTable, (tablename, namelist, typelist))
        

if __name__ == '__main__':
    unittest.main()
