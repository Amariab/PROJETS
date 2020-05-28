#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 17:15:24 2020

@author: utilisateur
"""

import pandas as pd
import sqlalchemy
import pymysql

engine = sqlalchemy.create_engine("mysql+pymysql://root:simplon123@localhost/SIRENE")

link = '/home/utilisateur/Documents/PROJETS/OPENDATA/Niveau_08.xls'

df = pd.read_excel(link, skiprows=0, header=1)
print(df)

df.to_sql('Niveau_08', con = engine, if_exists='replace', index = False)






