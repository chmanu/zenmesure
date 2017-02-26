#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Zenity import *

# Création de l'IHM
obj = Zenity()
# Connexion à la BDD
conn = psycopg2.connect("dbname=postgres user=chmanu")
cur = conn.cursor()

choix_req=obj.list(('ID', 'Description'), [1, 'Filtrer selon l\'ID', 2, 'Filtrer selon la date de mesure'], title='Requête ?')

if (choix_req=='1'):
        # Requête 1
        cur.execute("SELECT * FROM mesure where id = %s;",obj.entry(text='ID ?') )
        l_result = []
        for row in cur:
            l_result.append(row[0])
            l_result.append(row[1])
            l_result.append(row[2])
        print(obj.list(('id', 'date', 'valeur'), l_result, checklist=False, text='Résultat'))
        
elif (choix_req=='2'):
        # Requête 2
        d1=obj.calendar(title='date min', text='Choisissez la borne inférieure')
        d2=obj.calendar(title='date max', text='Choisissez la borne supérieure')
        cur.execute("SELECT * FROM mesure where qd >= %s and qd <= %s;",[d1,d2])
        l_result = []
        for row in cur:
            l_result.append(row[0])
            l_result.append(row[1])
            l_result.append(row[2])
        print(obj.list(('id', 'date', 'valeur'), l_result, checklist=False, text='Résultat'))
else:
        print("Requête inconnue")
        
cur.close()
conn.close()
