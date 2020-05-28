#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 16:20:51 2020

@author: utilisateur
"""
 
import pandas as pd
import pymysql
import time

import sqlalchemy
engine = sqlalchemy.create_engine("mysql+pymysql://root:simplon123@localhost/SIRENE")

def importcsv(link, table, date):
    print("Lecture des données")
    start_time = time.time()
    csize = 50000
    df = pd.read_csv(link, compression = 'zip', chunksize = csize, parse_dates = date)
    print("Données lues")
    i = csize
    for chunk in df:
        chunk.to_sql(table, con = engine, if_exists='append', index = False)
        i += csize
        print(i)
    return print("Temps d execution : %s secondes ---" % (time.time() - start_time))

importcsv('https://www.data.gouv.fr/fr/datasets/r/09af65ff-c1c6-40bb-bfcb-b80f7ac93b72', 'Historique_table', ['dateFin', 'dateDebut'])

# trouvé sur le bureau SIRENE

