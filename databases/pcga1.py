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
    
    
    query = """SELECT * 
    from pcga_annotation pa
    inner join pcga_whole_slide pws on left(pws.Sample_id, 30) = LEFT(pa.Sample_id, 30)"""
        
    q1=q2=q3=q4=q5=q6 = ""

    
    if sample_type == "Brush":
        q1 = "SampleType == Brush"
        l.append(q1)
    
    elif sample_type == "Biopsy":
        q1 = "SampleType == Biopsy"
        l.append(q1)

    if cohort_type == "Discovery":
        q2 = "Cohort == DiscoverySet"
        l.append(q2)
    
    elif cohort_type == "Validation":
        q2 = "Cohort == ValidationSet"
        l.append(q2)

    if status == "Current":
        q3 = "Genomic_Smoking_Status == Current"
        l.append(q3)

    elif status == "Former":
        q3 = "Genomic_Smoking_Status == Former"
        l.append(q3)
    
    if LC_history == "Yes":
        q4 = "Previous_LC_History == Y"
        l.append(q4)

    elif LC_history == "No":
        q4 = "Previous_LC_History == N"
        l.append(q4)
        
    if LC_job == "Yes":
        q5 = "HighRisk_LC_Job == Y"
        l.append(q5)

    elif LC_job == "No":
        q5 = "HighRisk_LC_Job == N"
        l.append(q5)

    if AB_exp == "Yes":
        q6 = "Asbestos_Exp == Y"
        l.append(q6)

    elif AB_exp == "No":
        q6 = "Asbestos_Exp == N"
        l.append(q6)

    if len(l) == 1:
        query += "WHERE"
        query += l[0]
    
    elif len(l) > 1:
        query += "WHERE"
        for i in l[:-1]:
            query += i
            query += "AND"
        query += l[-1]
            
    try: cur.execute(query1)
    
    except pymysql.Error as e:
        print(e,query1)

    results = cur.fetchall()
    
    #print(json.dumps(results))
    print(query1)
    conn.close()





