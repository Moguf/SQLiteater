import os
import sys
import pytest
import unittest

sys.path.append(os.path.abspath('./sqliteater'))
sys.path.append(os.path.abspath('../sqliteater'))
try:
    from sqliteater import sqliteater
except:
    import sqliteater
    
class TestSQLiteater(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass

    def setUp(self):
        self.dbname = 'test.db'
        self.tclass = sqliteater.SQLiteater()
        
    def test_createTable_with_lists(self):
        self.tclass.openDB(self.dbname)
        tablename = 'testtable'
        namelist = ['name','weight','hight','location']
        typelist = [str, int, float, str]
        self.assertTrue(self.tclass.createTable(tablename, namelist, typelist))
        self.tclass.close()
        
    def test_createTable_with_different_length_lists(self):
        self.tclass.openDB(self.dbname)
        tablename = 'testtable'
        namelist = ['name','weight','hight','location']
        typelist = [str, int, float]
        self.assertRaises(Exception, self.tclass.createTable, (tablename, namelist, typelist))
        self.tclass.close()

if __name__ == '__main__':
    unittest.main()
