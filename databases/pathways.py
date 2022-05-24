#!/usr/bin/python3

import os
import pymysql
from getpass import getpass
pswd = getpass()

conn = pymysql.connect(host='bioed.bu.edu',
    user= 'ajzheng',
    password= pswd,
    db= 'Group_H',
    port = 4253,
    local_infile=1) 
    
cur = conn.cursor()

directory = "Patchfeatures"

for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
        

    query1 = "DROP TABLE IF EXISTS %s ;"%(filename[:-12])

    query2 = """
    CREATE TABLE %s (
        V1 int,
        V2 int,
        V3 int,
        V4 int,
        V5 int,
        V6 int,
        V7 int,
        V8 int,
        V9 int,
        V10 int,
        V11 int,
        V12 int,
        V13 int,
        V14 int,
        V15 int,
        V16 int,
        V17 int,
        V18 int,
        V19 int,
        V20 int,
        V21 int,
        V22 int,
        V23 int,
        V24 int,
        V25 int,
        V26 int,
        V27 int,
        V28 int,
        V29 int,
        V30 int,
        V31 int,
        V32 int,
        V33 int,
        V34 int,
        V35 int,
        V36 int,
        V37 int,
        V38 int,
        V39 int,
        V40 int,
        V41 int,
        V42 int,
        V43 int,
        V44 int,
        V45 int,
        V46 int,
        V47 int,
        V48 int,
        V49 int,
        V50 int
        )engine=innodb;
    """%(filename[:-12])
    
    query3 = "LOAD DATA LOCAL INFILE %s INTO TABLE %s;"%(filename, filename[:-12])
    
    try:
        cur.execute(query1)
    except pymysql.Error as e:
        print(e, query1)
    
    try:
        cur.execute(query2)
    except pymysql.Error as e:
        print(e, query2)
        
    try:
        cur.execute(query3)
    except pymysql.Error as e:
        print(e, query3)



conn.commit()


conn.close()
