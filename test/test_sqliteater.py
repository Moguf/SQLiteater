import os
import sys
import pytest
import unittest
from subprocess import check_output

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
        
    @classmethod
    def tearDownClass(cls):
        cmd = 'rm test.db'
        check_output(cmd, shell=True)
        
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

    def test_select_all(self):
        self.tclass.openDB(self.dbname)
        tablename = 'testtable'
        self.tclass.selectAll(tablename)
        self.tclass.close()

    def test_createTable_with_primary_keys(self):
        self.tclass.openDB(self.dbname)
        tablename = 'tablewithpraimary'
        namelist = ['name', 'weight', 'hight', 'location']
        typelist = [str, int, float, str]
        primary = ["PRIMARY KEY", '', '', '']
        self.assertTrue(self.tclass.createTable(tablename, namelist, typelist, primary))
        self.tclass.close()
        
        
if __name__ == '__main__':
    unittest.main()
