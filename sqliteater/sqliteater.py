import os
import sqlite3


class MyTable(object):
    def __init__(self, tablename, namelist, typelist=[], constraints=[]):
        self.typedict = { str: 'text', int: 'integer', float: 'real' }
        self.tablename = tablename
        self.namelist = namelist
        self.typelist = typelist
        self.constraints = constraints
        
        self._formatConstraints(constraints)
        self._formatTypelist(typelist)
        self._checkLength()

    def _formatTypelist(self, typelist):
        if typelist == []:
            self.typelist = ["" for i in self.namelist]
        else:
            self.typelist = [self.typedict[ele] for ele in typelist]
        return self.typelist

    def _formatConstraints(self, constraints):
        if self.constraints == []:
            self.constraints = ["" for i in self.namelist]
        else:
            self.constraints = constraints
        return self.constraints
            
    def _checkLength(self):
        # check len(namelist) == len(typelist) == len(constraints).
        if not (len(self.namelist) == len(self.typelist) or \
                len(self.typelist) == len(self.constraints)):
            msg = 'Error: len(namelist), len(typelist), len(constraints) are not the same length. '
            raise Exception(msg)
        
    def __str__(self):
        return '<This table is {}.>'.format(self.tablename)

    def __len__(self):
        return len(self.namelist)

    def show(self):
        print(self.tablename)

            
class SQLiteater(object):
    """ This class provides an easy way to access sqlite3."""
    def __init__(self):
        self.dbpath = ''
        self.mytables = {}

    def createTable(self, tablename, namelist, typelist, constraints=[]):
        """ 
        createTable
        ~~~~~~~~~~~
        
        :tablename:        Given a Table name.
        :namelist:         Given a name list.    ex) [date, firstname, lastname]
        :typelist:         Given a type list.    ex) [int, str, str]
        :constraints:      Given a primary list. ex) [UNIQUE, CHECK (expression), PRIMARY KEY, DEFAULT, NOT NULL]
        
        This methods create a teble in sqlite3 database. You should run this method after running self.openDB.
        
        """
        self.mytables = {tablename: MyTable(tablename, namelist, typelist, constraints)}
        tbl = self.mytables[tablename]
        instruction = 'create table {} '.format(tablename)
        _datas = '('
        for i in range(len(tbl)):
            if len(tbl)-1 == i:
                _data = '{} {} {}'.format(tbl.namelist[i], tbl.typelist[i], tbl.constraints[i])
                _datas += _data
                break
            _data = '{} {} {}, '.format(tbl.namelist[i], tbl.typelist[i], tbl.constraints[i])
            _datas += _data
        _datas += ')'
        # create an instraction.
        
        #print("COMMAND: ", instruction + _datas)
        self.crsr.execute(instruction + _datas)
        self.conn.commit()
        
        return instruction

    def openTable(self):
        pass

    def checkDB(self):
        pass
    
    def openDB(self, dbpath):
        self.dbpath = dbpath
        self.conn = sqlite3.connect(dbpath)
        self.crsr = self.conn.cursor()

    def readTable(self):
        pass

    def addColumn(self):
        """
        alter table add column
        """
        pass

    def renameTable(self):
        """
        alter table rename, add column and rename.
        """
        pass

    def deleteTable(self, tablename):
        """
        DROP TABLE TABLENAME;
        """
        pass

    def createView(self):
        """
        CREATE [TEMP] VIEW view_name AS SELECT query_statement
        
        """
        pass

    def deleteView(self):
        """
        DROP VIEW view_name;
        """
        pass

    def createIndex(self):
        """
        CREATE [UNIQUE] INDEX index_name ON table_name ( column_name [, ...] );
        CREATE INDEX idx_employees_name ON employees ( name );
        """
        pass

    def deleteIndex(self):
        """
        DROP INDEX index_name;
        """
        pass
    
    def insert(self, tablename, namelist, typelist, datalist):
        """
        INSERT INTO table_name (column_name [, ...]) VALUES (new_value [, ...]);
        INSERT INTO parts ( name, stock, status ) VALUES ( 'Widget', 17, 'IN STOCK' );
        INSERT INTO table_name VALUES (new_value [, ...]);
        INSERT INTO table_name (column_name, [...]) SELECT query_statement;
        """
        tbl = MyTable(tablename, namelist, typelist)
        instruction = 'insert into ' + tablename + self.list2p(tbl.namelist) + \
                      ' values ' + self.list2p(datalist)
        self.crsr.execute(instruction)
        self.conn.commit()

    def list2p(self, inlist):
        """ 
        change list to paranthesis string. 
        ex) ['name', 1.0 , "hello"] => "('name', 1.0, 'hello') "
        """
        ignorelist = ['text', 'real', 'integer']
        out = ' ('
        for i, ele in enumerate(inlist):
            if isinstance(ele, str):
                if ele in ignorelist:
                    out += "{}".format(ele)
                else:
                    out += "'{}'".format(ele)
            else:
                out += '{}'.format(ele)
            if i != len(inlist) - 1:
                out += ', '
            else:
                out += ' )'
        return out
        
    
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

    def getColumnNames(self, tablename):
        """
        get table information and retarn them as list format.
        """
        cursor = self.conn.execute('select * from ' + tablename)
        return [des[0] for des in cursor.description]

    def getRowData(self, tablename, column_name):
        '''
        '''
        self.crsr.execute('SELECT ' + column_name + ' FROM ' + tablename)
        return self.crsr.fetchall()
        
        
        
    def select(self):
        """
        SELECT output_list FROM input_table WHERE row_filter;
        
        SELECT [DISTINCT] select_heading 
        FROM source_tables
        WHERE filter_expression 
        GROUP BY grouping_expressions
        HAVING filter_expression 
        ORDER BY ordering_expressions 
        LIMIT count
        OFFSET count
        """
        pass

    def selectAll(self, tablename=''):
        """
        SELECT * FROM table;
        """
        self.crsr.execute('SELECT * FROM ' + tablename)
        for row in self.crsr:
            print(">>", row)
        return None

    def showAlltables(self):
        pass
        
    def raw(self, command):
        self.crsr.execute(command)

    def close(self):
        self.crsr.close()
    
