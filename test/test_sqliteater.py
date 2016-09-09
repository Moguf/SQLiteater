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


class TestMyTable(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass
    
    def test_createTable_with_different_length_lists(self):
        tablename = 'testtable'
        namelist = ['name','weight','hight','location']
        typelist = [str, int, float]
        self.assertRaises(Exception, sqliteater.MyTable, (tablename, namelist, typelist))

    def test_length_of_table_by_len_function(self):
        tablename = 'testtable'
        namelist = ['name','weight','hight','location']
        typelist = [str, int, float, str]
        tbl = sqliteater.MyTable(tablename, namelist, typelist)
        self.assertEqual(len(namelist), len(tbl))

    def test_empty_constraints(self):
        tablename = 'testtable'
        namelist = ['name','weight','hight','location']
        typelist = [str, int, float, str]
        tbl = sqliteater.MyTable(tablename, namelist, typelist)
        self.assertEqual(len(tbl.constraints), len(tbl))
        
        
    
class TestSQLiteater(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.datalist = [("Inu", 80, 170, "Tokyo"),
                        ("Neko", 50, 150, "Nagoya"),
                        ("Tanuki", 120, 200, "Sapporo"),
                        ("Taro", 130, 167.2, "Sapporo")]

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

    def test_select_all(self):
        self.tclass.openDB(self.dbname)
        tablename = 'selecttesttable'
        namelist = ['name','weight','hight','location']
        typelist = [str, int, float, str]
        self.assertTrue(self.tclass.createTable(tablename, namelist, typelist))
        for idata in self.datalist:
            self.tclass.insert(tablename, namelist, typelist, idata)
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

    def test_list2strParenthesis(self):
        self.assertEqual(" ('male', 'female', 1, 0.1 )", self.tclass.list2p(["male", "female", 1, 0.1]))

    def test_getNames(self):
        self.tclass.openDB(self.dbname)
        tablename = 'tablegettableinfo'
        namelist = ['name', 'weight', 'hight', 'location']
        typelist = [str, int, float, str]
        primary = ["PRIMARY KEY", '', '', '']
        self.tclass.createTable(tablename, namelist, typelist, primary)
        self.assertEqual(['name', 'weight', 'hight', 'location'], self.tclass.getColumnNames(tablename))
        self.tclass.close()

    def test_getRowData(self):
        self.tclass.openDB(self.dbname)
        tablename = 'tablegetRowData'
        namelist = ['name', 'weight', 'hight', 'location']
        typelist = [str, int, float, str]
        primary = ["PRIMARY KEY", '', '', '']
        self.tclass.createTable(tablename, namelist, typelist, primary)
        for idata in self.datalist:
            self.tclass.insert(tablename, namelist, typelist, idata)
        self.assertEqual([('Inu',), ('Neko',), ('Tanuki',), ('Taro',)], self.tclass.getRowData(tablename, 'name'))
        self.tclass.close()

    def test_getRowData_with_distinct(self):
        self.tclass.openDB(self.dbname)
        tablename = 'test_table'
        namelist = ['name', 'weight', 'hight', 'location']
        typelist = [str, int, float, str]
        primary = ["PRIMARY KEY", '', '', '']
        self.tclass.createTable(tablename, namelist, typelist, primary)
        for idata in self.datalist:
            self.tclass.insert(tablename, namelist, typelist, idata)
        self.assertEqual([('Tokyo',), ('Nagoya',), ('Sapporo',)],
                         self.tclass.getRowData(tablename, 'location', distinct=True))
        self.tclass.close()


        
if __name__ == '__main__':
    suite1 = unittest.TestLoader().loadTestsFromTestCase(TestMyTable)
    suite2 = unittest.TestLoader().loadTestsFromTestCase(TestSQLiteater)
    suite = unittest.TestSuite([suite1, suite2])
    unittest.TextTestRunner(verbosity=2).run(suite)
                                                        


