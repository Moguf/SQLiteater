
import os
import sqlite3

class SQLiteater(object):
    def __init__(self):
        self.typedict = { str: 'text', int: 'integer', float: 'real' }

    def createTable(self, tablename, namelist, typelist):
        self._checkLength(namelist, typelist)
        instruction = 'create table {} '.format(tablename)
        _datas = ''
        for i, eles in enumerate(zip(namelist, typelist)):
            if len(namelist)-1 == i:
                _data = '{} {}'.format(eles[0], self.typedict[eles[1]])
                _datas += _data
                break
            _data = '{} {}, '.format(eles[0], self.typedict[eles[1]])
            _datas += _data
        self.c.execute(instruction)
        return instruction

    
    def _checkLength(self, list1, list2):
        if len(list1) != len(list2):
            raise Exception('Length of list1 != Length of list2.')
        return True
    
    def openTable(self):
        pass
    
    def openDb(self, dbpath):
        conn = sqlite3.connect(dbpath)
        self.c = conn.cursor()

    def readTable(self):
        pass

    def insert(self):
        pass

    def raw(self, command):
        self.c.execute(command)
