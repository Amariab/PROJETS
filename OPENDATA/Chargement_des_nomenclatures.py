# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 10:01:20 2020

@author: rafik
"""


import pandas as pd, sqlalchemy


engine = sqlalchemy.create_engine(
        'mysql+pymysql://user:mdp@localhost:3306')


nom_col_emboite = ['activitePrincipaleEtablissement', 'niv4', 'niv3', 'niv2', 'niv1']
nom_col_niv1 =['niv1', 'libelle1']

############################# 2008 ##################################◘


data = pd.read_excel('naf2008_5_niveaux.xls',
                     index_col=None, header=None, names=nom_col_emboite,
                     skiprows=1, dtype=str)

data.to_sql('niv_enb_2008', con=engine, if_exists='append', index =False,
                     schema = 'siren')


data = data = pd.read_excel('naf2008_liste_n1.xls',
                     index_col=None, header=None, names=nom_col_niv1,
                     skiprows=[0, 1, 2], dtype=str)

data.to_sql('niv1_2008', con=engine, if_exists='replace', index =False,
                     schema = 'siren')


############################# 2003 ##################################◘


data = pd.read_excel('naf2003_n1-5.xls',
                     index_col=None, header=None,
                     names=nom_col_emboite, skiprows=[0, 1], dtype=str)

data.to_sql('niv_enb_2003', con=engine, if_exists='append', index =False,
                     schema = 'siren')


data = data = pd.read_excel('naf2003_liste_n1.xls',
                     index_col=None, header=None, names=nom_col_niv1,
                     skiprows=[0, 1], dtype=str)

data.to_sql('niv1_2003', con=engine, if_exists='replace', index =False,
                     schema = 'siren')


############################# 1993 ##################################◘


data = pd.read_excel('naf1993_5_niveaux.xls',
                     index_col=None, header=None,
                     names=nom_col_emboite, skiprows=[0, 1], dtype=str)

data.to_sql('niv_enb_1993', con=engine, if_exists='append', index =False,
                     schema = 'siren')


data = data = pd.read_excel('naf1993_liste_n1.xls',
                     index_col=None, header=None, names=nom_col_niv1,
                     skiprows=[0, 1], dtype=str)

data.to_sql('niv1_1993', con=engine, if_exists='replace', index =False,
                     schema = 'siren')



############################# 1973 ##################################◘

nom_col = ['niv1', 'niv2', 'niv3', 'activitePrincipaleEtablissement',
           'libelle1', 'libelle2', 'libelle3', 'libelle4']



data = pd.read_excel('NAP 1973_1993.xls',
                     index_col=None, header=None,
                     names=nom_col, skiprows=1, dtype=str)

data.to_sql('niv_enb_1973', con=engine, if_exists='append', index =False,
                     schema = 'siren')