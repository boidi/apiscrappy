# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: %(Boidi)s
"""
print('reqSQL')
from cnxdb import connection_bd

def data_lab():
    cnx = connection_bd()
    cursor = cnx.cursor()
    query = "SELECT comment_id,contenu ,comment_label FROM users_comments where comment_label is  NOT NULL;"
    cursor.execute(query)
    data = cursor.fetchall()
    cnx.commit()
    print(data)
    cursor.close()
    cnx.close()
    return data
#print(data)

def reqcommentaires():
    cnx =  connection_bd()                        
    cursor = cnx.cursor()
    query_string = "SELECT comment_id,contenu FROM users_comments where comment_label is NULL;"
    cursor.execute(query_string)
    data = cursor.fetchall()
    cnx.commit() 
    cursor.close()
    cnx.close()
    return data

def modif_lbel(lab,idC):
    cnx = connection_bd()
    cursor=cnx.cursor()
    update_query='UPDATE users_comments SET comment_label = %s where comment_id = %s;'
    cursor.execute(update_query, (idC,lab))
    cnx.commit() 
    cursor.close()
    cnx.close()
# =============================================================================
# =============================================================================
# =============================================================================
# =============================================================================
# def ajout_comments(i, user_no):
#     cnx = connection_bd()
#     cursor=cnx.cursor()
#     insert_query="INSERT INTO users_comments (contenu, user_id, comment_date) VALUES( %s, %s, %s);"
#     cursor.execute(insert_query, [str(series.loc[i,'content']) , str(user_no) , str(series.loc[i,'date'])])
#     cnx.commit() 
#     cursor.close()
#     cnx.close()
#       
# =============================================================================
# =============================================================================
# =============================================================================
def recente_date():
    cnx = connection_bd()
    cursor = cnx.cursor()
    date_query = 'SELECT max(comment_date) FROM users_comments;'
    cursor.execute(date_query)
    #data_date = cursor.fetchall()
    cnx.commit() 
    cursor.close()
    cnx.close()
	 #return data_date
 
#%%
def select_data(pseudo):
    cnx = connection_bd()
    cursor = cnx.cursor()
    req = "SELECT idusers FROM users_data WHERE user_pseudo = %s;"
        #print(series.loc[i,'author'])
    cursor.execute(req, [pseudo])
    res = cursor.fetchall()
    cursor.close()
    cnx.close()
    return res

# =============================================================================
def insert_user(author):
    cnx = connection_bd()
    cursor = cnx.cursor()
    insert_query = "INSERT INTO users_data (user_pseudo) VALUES (%s);"
    cursor.execute(insert_query, [author])
    print(insert_query)
    cnx.commit()
    user_id = cursor.lastrowid
    cursor.close()
    cnx.close()
    return user_id

def insert_comment(content, user_no, dates):
    cnx = connection_bd()
    cursor = cnx.cursor()
    insert_query = "INSERT INTO users_comments (contenu, user_id, comment_date) VALUES ( %s, %s, %s);"
    print(insert_query)
    cursor.execute(insert_query, (content, user_no, dates))
    cnx.commit()
    cursor.close()
    cnx.close()