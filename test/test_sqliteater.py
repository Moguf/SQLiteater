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
        cls.namelist = ['name', 'weight', 'hight', 'location']
        cls.typelist = [str, int, float, str]
        cls.primary = ["PRIMARY KEY", '', '', '']

    def setUp(self):
        self.dbname = 'test.db'
        self.tclass = sqliteater.SQLiteater()
        
    @classmethod
    def tearDownClass(cls):
        cmd = 'rm test.db'
        check_output(cmd, shell=True)

    def _createTable(self, cls, tblname):
        cls.openDB(self.dbname)
        cls.createTable(tblname, self.namelist, self.typelist, self.primary)
        return cls

    def _insertData(self, cls, tblname):
        for idata in self.datalist:
            cls.insert(tblname, self.namelist, self.typelist, idata)
        
    def test_createTable_with_lists(self):
        self.tclass.openDB(self.dbname)
        tablename = 'testtable'
        self.assertTrue(self.tclass.createTable(tablename, self.namelist, self.typelist))
        self.tclass.close()

    def test_select_all(self):
        self.tclass.openDB(self.dbname)
        tablename = 'selecttesttable'
        self.assertTrue(self.tclass.createTable(tablename, self.namelist, self.typelist))
        self._insertData(self.tclass, tablename)
        self.assertEqual(self.datalist, self.tclass.selectAll(tablename))
        self.tclass.close()

    def test_createTable_with_primary_keys(self):
        self.tclass.openDB(self.dbname)
        tablename = 'ctwpktable'
        self.assertTrue(self.tclass.createTable(tablename, self.namelist, self.typelist, self.primary))
        self.tclass.close()

    def test_list2strParenthesis(self):
        self.assertEqual(" ('male', 'female', 1, 0.1 )", self.tclass.list2p(["male", "female", 1, 0.1]))

    def test_getNames(self):
        tablename = 'gntable'
        self._createTable(self.tclass, tablename)
        self.assertEqual(['name', 'weight', 'hight', 'location'], self.tclass.getColumnNames(tablename))
        self.tclass.close()

    def test_getRowData(self):
        tablename = 'gtdtable'
        self._createTable(self.tclass, tablename)
        self._insertData(self.tclass, tablename)
        self.assertEqual([('Inu',), ('Neko',), ('Tanuki',), ('Taro',)], self.tclass.getRowData(tablename, 'name'))
        self.tclass.close()

    def test_getRowData_with_distinct(self):
        tablename = 'gtdtablewd'
        self._createTable(self.tclass, tablename)
        self._insertData(self.tclass, tablename)
        self.assertEqual([('Tokyo',), ('Nagoya',), ('Sapporo',)],
                         self.tclass.getRowData(tablename, 'location', distinct=True))
        self.tclass.close()

    def test_select_with_names(self):
        tablename = 'wntable'
        self._createTable(self.tclass, tablename)
        self._insertData(self.tclass, tablename)
        self.assertEqual([('Inu',), ('Neko',), ('Tanuki',), ('Taro',)], self.tclass.select(tablename, 'name'))
        self.assertEqual([('Tokyo',), ('Nagoya',), ('Sapporo',), ('Sapporo',)], self.tclass.select(tablename, 'location'))
        self.assertEqual([(80,), (50,), (120,), (130,)], self.tclass.select(tablename, 'weight'))
        self.assertEqual([(170.0,), (150.0,), (200.0,), (167.2,)], self.tclass.select(tablename, 'hight'))

    def test_select_with_row_filter(self):
        tablename = 'wrftable'
        self._createTable(self.tclass, tablename)
        self._insertData(self.tclass, tablename)
        self.assertEqual([(120,), (130,)], self.tclass.select(tablename, 'weight', where='weight > 100'))
        
        
if __name__ == '__main__':
    suite1 = unittest.TestLoader().loadTestsFromTestCase(TestMyTable)
    suite2 = unittest.TestLoader().loadTestsFromTestCase(TestSQLiteater)
    suite = unittest.TestSuite([suite1, suite2])
    unittest.TextTestRunner(verbosity=2).run(suite)
                                                        


