#!/usr/bin/env python3

import pymysql
import cgi
import cgitb
import json

cgitb.enable()


print("Content-type: text/html\n")

form = cgi.FieldStorage()

if (form):
    conn = pymysql.connect(host='bioed.bu.edu',
        user= 'Group_H',
        password= "Group_H",
        db= 'Group_H',
        port = 4253) 
    
    cur = conn.cursor()
    
    sample_type = form.getvalue("sampletype")
    cohort_type = form.getvalue("cohorttype")
    status = form.getvalue("status")
    LC_history = form.getvalue("LC_history")
    LC_job = form.getvalue("LC_job")
    AB_exp = form.getvalue("AB_exp")
    
    
    if sampletype == "pcga":
    
        query1 = """SELECT * 
        from pcga_annotation pa
        inner join pcga_whole_slide pws on left(pws.Sample_id, 30) = LEFT(pa.Sample_id, 30)"""
        
        try: cur.execute(query1)
        
        except pymysql.Error as e:
            print(e,query1)

        results = cur.fetchall()
        
        html_template = """
        <html>
            <head>
                <title></title>
            </head>
            <body>
                <p>
                %s
                </p>
            </body>
        </html> 
        """%(results)
        
        print(html_template)
        #print(json.dumps(results))

    
    elif sample_type == "tcga":
        
        query2 = """SELECT * 
        from TCGA_annotation ta 
        inner join TCGA_whole_slide tws on left(tws.Sample_id, 30) = LEFT(ta.Sample_id, 30)"""
        
        
        try: cur.execute(query2)
        
        except pymysql.Error as e:
            print(e,query2)

        results = cur.fetchall()

    	print(json.dumps(results))
    
    conn.close()
    
    
    
