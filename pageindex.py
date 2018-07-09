# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: %(Boidi)s
"""
#print(_doc_)
from flask import Flask
from mysql.connector import errorcode
from flask import render_template,request, redirect
from gevent.wsgi import WSGIServer
import pandas as pd
from requete import *

#import mysql.connector 

    

# =============================================================================



# =============================================================================
app = Flask(__name__)
@app.route('/commentaires',methods=['GET', 'POST'])
def select_comment():
    data = reqcommentaires()
    return render_template('pageClient.html',data=data)


    
# =============================================================================
# =============================================================================
@app.route('/commentaires/positif/<id_com>', methods=['POST'])
def update_labpositif(id_com):
      if request.method =='POST':
          modif_lbel(id_com, 1)
          return redirect('/commentaires')
  
 
# =============================================================================
@app.route('/commentaires/negatif/<id_com>',methods=['POST'])
def update_labnegatif(id_com):
    if request.method =='POST': #and request.form == ['positif']:
        modif_lbel(id_com, 0)
        return redirect('/commentaires')
# =============================================================================
@app.route('/label',methods=['GET'])
def selectdata_lab():
    res = data_lab()
    return render_template('labels.html',data=res)
# =============================================================================
#%%
app.run(debug = False)