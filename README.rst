.. -*- mode: rst -*-

SQLiteater
==========

Python3 SQLite3 parser.

Requirements
------------

- python3 >= 3.5.1


RECOMMEND
---------

Install virtualenv. (RECOMMEND:for protecting your Home environment.)

.. code-block:: bash

  python3 -m pip install -U pip setuptools
  python3 -m pip install virtualenv
  # or
  pip3 install virtualenv
  

activate virtualenv

.. code-block:: bash

  virtualenv -p python3 venv
  source venv/bin/activate
  # Removing virtual environment
  # (venv) deactivate 


Set Up
------

.. code-block:: bash
                
   python3 -m pip install -r requirements.txt
   # or
   pip3 install -r requirements.txt


build & install
---------------

.. code-block:: bash

   cd SQLiteater
   python3 setup.py build
   python3 setup.py install

   
Example
-------

Create Table
^^^^^^^^^^^^

.. code-block:: python

   from sqliteater import SQLiteater
   
   path2db = 'test.db'
   tmp = SQliteater(path2db)
   tablename = 'mytable'
   namelist = ['name', 'weight', 'hight', 'location']
   typelist = [str, int, float, str]
   primary = ["PRIMARY KEY", '', '', '']
   tmp.createTable(tablename, namelist, typelist, primary)
   tmp.close()
   
