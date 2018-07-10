# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: %(Boidi)s
"""
from cnxdb import connection_bd

def data_lab():
    cnx = connection_bd()
    cursor = cnx.cursor()
    query = "SELECT comment_id,contenu, comment_label FROM users_comments where comment_label is  NOT NULL;"
    cursor.execute(query)
    data = cursor.fetchall()
    cnx.commit()
    print(data)
    cursor.close()
    cnx.close()
    return data

	
def reqcommentaires():
    cnx =  connection_bd()                        
    cursor = cnx.cursor()
    query_string = "SELECT comment_id, contenu FROM users_comments where comment_label is NULL;"
    cursor.execute(query_string)
    data = cursor.fetchall()
    cnx.commit() 
    cursor.close()
    cnx.close()
    return data

	
def modif_lbel(lab,idC):
    cnx = connection_bd()
    cursor = cnx.cursor()
    update_query = 'UPDATE users_comments SET comment_label = %s where comment_id = %s;'
    cursor.execute(update_query, (idC,  lab))
    cnx.commit() 
    cursor.close()
    cnx.close()

	
def recente_date():
    cnx = connection_bd()
    cursor = cnx.cursor()
    date_query = 'SELECT max(comment_date) FROM users_comments;'
    cursor.execute(date_query)
	data = cursor.fetchall()
    cnx.commit() 
    cursor.close()
    cnx.close()
	return data