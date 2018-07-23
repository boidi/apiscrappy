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
from requete import *
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
tab_comment['date']= pd.to_datetime(tab_comment['date']).dt.date

#print(tab_comment)

#%%
from cnxdb import connection_bd
conn = connection_bd()
#
#%%
def ajout_data(series):
    conn = connection_bd()
    cursor = conn.cursor()

    for i in range(len(series)):
        
        req = "SELECT idusers FROM users_data WHERE user_pseudo = %s;"
        #user_no = select_data(str(series.loc[i,'author']))

        cursor.execute(req, [series.loc[i,'author']])
        res = cursor.fetchall()
        print("RES", res) 
# =============================================================================
# =============================================================================
        if len(res) != 1:
            add_utilisateur = "INSERT INTO users_data (user_pseudo) VALUES (%s);"
            print(add_utilisateur)
            cursor.execute(add_utilisateur, [str(series.loc[i,'author'])]) 
            #user_no = insert_user(str(series.loc[i,'author']))
            #print("INSERT USERDATA", user_no)
        else:
            
            user_no = cursor
           # print("ELSE", user_no)
            #insert_comment(str(series.loc[i,'content']), str(user_no), str(series.loc[i,'dates'])) 
            add_commentaire = "INSERT INTO users_comments (contenu, user_id, comment_date) VALUES( %s, %s, %s);"
            print(add_commentaire)
            cursor.execute(add_commentaire, [str(series.loc[i,'content']) , str(user_no) , str(series.loc[i,'date'])])
            conn.commit() 
          
# =============================================================================
    
    cursor.close()
    conn.close() 
ajout_data(tab_comment)