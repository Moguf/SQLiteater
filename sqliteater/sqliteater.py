
import os
import sqlite3

class SQLiteater(object):
    def __init__(self):
        pass

    def createTable(self, tablename, namelist, typelist):
        for i, j in zip(namelisto, typelist):
            print(i,j)
        

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
        c.execute(command)
