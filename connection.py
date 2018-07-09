# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: %(Boidi)s
"""
print()
import re
#import scrapy
import pandas as pd
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen
import dateparser
from datetime import date
import datetime as dt
#from scrapy.crawler import CrawlerProcess
#%%


# =============================================================================
# app = Flask(__name__)
# =============================================================================
page ='https://fr.trustpilot.com/review/www.tripadvisor.fr'
client = page.split(".")
client = client[3]
raw_getter = urlopen(page).read().decode('utf-8')
soup_getter = bs(raw_getter, 'lxml')
comments= []
authors =[]
dates = []
for data in soup_getter.findAll('section', {'class': "content-section__review-info"}):
    comments.append(data.find('p',{'class':'review-info__body__text'}).text.replace('\n','').replace('\t','').replace('\"','').strip(' '))
    dates.append(data.find('time').attrs['datetime']) # recupere le format date dans la balise time 
             
for data in soup_getter.findAll('div', {'class': "consumer-info__details"}):
    authors.append(data.find('h3',{'class':'consumer-info__details__name'}).text.replace('\n','').replace('\'','').strip(' '))

tab_comment=pd.DataFrame({'author' : authors, 'content' : comments, 'date':dates})
tab_comment['dates']= pd.to_datetime(tab_comment['date']).dt.date
# =============================================================================
# print('unicode',tab_comment['content'].iloc[2])
# =============================================================================
#tab_comment

#%%
from cnxdb import connection_bd
#import mysql.connector 
#conn = mysql.connector.connect(host="localhost",user="root",password="pascaline", database="my_app")
conn = connection_bd()
#
#%%
def ajout_data(series):
    conn = connection_bd()
    cursor = conn.cursor()

    for i in range(len(series)):
        query = "SELECT idusers FROM users WHERE user_pseudo ='"
        query += " " + series.loc[i,'author'] + "';"
        print(query)
        cursor.execute(query)
        res = cursor.fetchall()
        print(res)
        if len(res) != 1:
            add_utilisateur = "INSERT INTO users (user_pseudo) VALUES ('"+ series.loc[i,'author'] +"');"
            print(add_utilisateur)
            cursor.execute(add_utilisateur) 
            user_no = cursor.lastrowid
        else:
            user_no = cursor
      
        #format_date = dt.datetime.strptime(str(series.loc[i,'date']), '%d/%m/%Y').strftime('%y-%m-%d')
        add_commentaire = 'INSERT INTO users_comments (contenu, user_id, comment_date) VALUES( "'+series.loc[i,'content']+'", '+str(user_no)+', "'+str(series.loc[i,'dates'])+'");'
    #add_commentaire = 'INSERT INTO users_comments (contenu, user_id, comment_date) VALUES ( "'+str(series.loc[i,'content'])+'", '+str(user_no)+', "'+str(format_date)+'");'

        print(add_commentaire)
        cursor.execute(add_commentaire) 
        conn.commit() 
    # Make sure data is committed to the database

    cursor.close()
    conn.close() 
ajout_data(tab_comment)