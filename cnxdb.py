# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: %(Boidi)s
"""
print('connection db')
#%% import 
import mysql.connector 
from mysql.connector import errorcode

#%%
def connection_bd():
    try:
        cnx = mysql.connector.connect(user='root',
                                      password= 'pascaline',
                                      host= '127.0.0.1',
                                      database='my_app')
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    return(cnx)