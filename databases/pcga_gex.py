#!/usr/bin/env python3

import pymysql
import cgi
import cgitb
import json
import pandas as pd

cgitb.enable()

# QUERIES
gex_query = """
select sample_id, gene, value, module
from pcga_geneset
where sample_id in (%s)
"""

form = cgi.FieldStorage()

print("Content-type: text/html\n")

if form:
    samples = form.getvalue("samples")
    samples = samples.split()
    modules = []
    if form.getvalue("bx_lightgreen") == 'true':
        modules.append("bx_lightgreen")
    if form.getvalue("bx_purple") == 'true':
        modules.append("bx_purple")
    if form.getvalue("bx_black") == 'true':
        modules.append("bx_black")
    if form.getvalue("bx_lightyellow") == 'true':
        modules.append("bx_lightyellow")
    if form.getvalue("bx_blue") == 'true':
        modules.append("bx_blue")
    if form.getvalue("bx_royalblue") == 'true':
        modules.append("bx_royalblue")
    if form.getvalue("bx_magenta") == 'true':
        modules.append("bx_magenta")
    if form.getvalue("bx_darkgrey") == 'true':
        modules.append("bx_darkgrey")
    if form.getvalue("bx_darkgreen") == 'true':
        modules.append("bx_darkgreen")

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
    matrix = matrix[matrix[3].isin(modules)]
    matrix = matrix[[0,1,2]].pivot(index=1, columns=0)[2].reset_index()
    matrix.set_index(matrix.columns[0], inplace=True)
    matrix.index.name = None
    matrix = matrix.to_json(orient="columns")
    
    print(json.dumps(matrix))

