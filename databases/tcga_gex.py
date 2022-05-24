#!/usr/bin/env python3

import pymysql
import cgi
import cgitb
import json
import pandas as pd

cgitb.enable()

# QUERIES
gex_query = """
select sample_id, gene, logCPM
from tcga_filtered_geneset
where sample_id in (%s)
"""

form = cgi.FieldStorage()

print("Content-type: text/html\n")

if form:
    samples = form.getvalue("samples")
    samples = samples.split()

    try:
        connection = pymysql.connect(
            host ='bioed.bu.edu',
            user = 'Group_H',
            password = 'Group_H',
            db = 'Group_H',
            port=4253
        )
    except pymysql.Error as e:
        print(e)

    cursor = connection.cursor()

    format_strings = ','.join(['%s'] * len(samples))

    try:
        cursor.execute(gex_query % format_strings, tuple(samples))
    except pymysql.Error as e:
        print(e, gex_query)

    results = cursor.fetchall()

    connection.close()

    matrix = pd.DataFrame(results)
    matrix = matrix[matrix[1] != "?"]
    matrix = matrix[[0,1,2]].pivot_table(index=0, columns=1, values=2)
    matrix = matrix.transpose().reset_index()   
    matrix.set_index(matrix.columns[0], inplace=True)
    matrix.index.name = None
    matrix = matrix.to_json(orient="columns")
    
    print(json.dumps(matrix))