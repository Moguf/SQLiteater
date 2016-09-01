import os
import sqlite3

class SQLiteater(object):
    def __init__(self):
        self.dbpath = ''
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

    def checkDB(self):
        pass
    
    def openDB(self, dbpath):
        self.dbpath = dbpath
        self.conn = sqlite3.connect(dbpath)
        self.c = self.conn.cursor()

    def readTable(self):
        pass

    def addColumn(self):
        """
        alter table add column
        """
        pass

    def renameTable(self):
        """
        alter table rename
        """
        pass

    def deleteTable(self, tablename):
        """
        Drop table tablename
        """
        pass

    def createView(self):
        """
        CREATE [TEMP] VIEW view_name AS SELECT query_statement
        """
        pass

    def createIndex(self):
        """
        CREATE [UNIQUE] INDEX index_name ON table_name ( column_name [, ...] );
        CREATE INDEX idx_employees_name ON employees ( name );
        DROP INDEX index_name;
        """
        pass
    
    def insert(self):
        """
        INSERT INTO table_name (column_name [, ...]) VALUES (new_value [, ...]);
        INSERT INTO parts ( name, stock, status ) VALUES ( 'Widget', 17, 'IN STOCK' );
        INSERT INTO table_name VALUES (new_value [, ...]);
        INSERT INTO table_name (column_name, [...]) SELECT query_statement;
        """
        pass

    def update(self):
        """
        UPDATE table_name SET column_name=new_value [, ...] WHERE expression
        UPDATE parts SET price = 4.25, stock = 75 WHERE part_id = 454;
        """
        pass
    
    def delete(self):
        """
        DELETE FROM table_name WHERE expression;
        DELETE FROM parts WHERE part_id >= 43 AND part_id <= 246;
        """
        pass
    
    def select(self):
        """
        SELECT output_list FROM input_table WHERE row_filter;
        """
        pass
    def selectAll(self, table=''):
        """
        SELECT * FROM table;
        """
        self.c.execute('select * FROM ' + table)

    def showAlltables(self):
        pass
        
    def raw(self, command):
        self.c.execute(command)

    def close(self):
        self.c.close()
    
    
