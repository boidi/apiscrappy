# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: %(Boidi)s
"""


from cnxdb import connection_bd
conn = connection_bd()
cursor = conn.cursor()
add_utilisateur = 'INSERT INTO users_data (user_pseudo) VALUES (%s);'

cursor.execute(add_utilisateur, ['lolulou'])
conn.commit()
cursor.close()
conn.close()