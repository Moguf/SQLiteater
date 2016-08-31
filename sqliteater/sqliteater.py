import os
import sqlite3

class SQLiteater(object):
    def __init__(self):
        self.typedict = { str: 'text', int: 'integer', float: 'real' }

    def createTable(self, tablename, namelist, typelist, constraints=[]):
        self._checkLength(namelist, typelist)
        if not constraints:
            constraints = ["" for i in namelist]
        self._checkLength(namelist, constraints)
        instruction = 'create table {} '.format(tablename)
        _datas = '('
        for i, eles in enumerate(zip(namelist, typelist)):
            if len(namelist)-1 == i:
                _data = '{} {}'.format(eles[0], self.typedict[eles[1]])
                _datas += _data
                break
            _data = '{} {}, '.format(eles[0], self.typedict[eles[1]])
            _datas += _data
        _datas += ')'
        print(instruction + _datas)
        self.c.execute(instruction + _datas)
        self.conn.commit()
        return instruction

    def _checkLength(self, list1, list2):
        if len(list1) != len(list2):
            raise Exception('Length of list1 != Length of list2.')
        return True
    
    def openTable(self):
        pass
    
    def openDB(self, dbpath):
        self.conn = sqlite3.connect(dbpath)
        self.c = self.conn.cursor()

    def readTable(self):
        pass

    def insert(self):
        pass

    def raw(self, command):
        self.c.execute(command)

    def close(self):
        self.c.close()
    
    
