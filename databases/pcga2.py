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
    sex = form.getvalue("sex")
    status = form.getvalue("status")
    LC_history = form.getvalue("LC_history")
    LC_job = form.getvalue("LC_job")
    AB_exp = form.getvalue("AB_exp")
    
    MolecularSubtype = form.getlist("MolecularSubtype")
    DysplasiaGrade = form.getlist("DysplasiaGrade")
    TCGASubtype = form.getlist("TCGASubtype")
    AgeatBaseline = form.getlist("AgeatBaseline")
    #Location = form.getlist("Location")
    
    query = ""
    
    query1 = """SELECT * 
from pcga_annotation pa
inner join pcga_whole_slide pws on left(pws.Sample_id, 30) = LEFT(pa.Sample_id, 30) 
    """
    
    query2 = """SELECT * 
from pcga_annotation pa
right join pcga_geneset pg on pg.sample_id = pa.Sample_id
    """

    q1=q2=q3=q4=q5=q6=q7=q8=q9=q10=q11= ""
    
    l = []

    
    if sample_type == "Brush":
        q1 = "SampleType = 'Brush'"
        l.append(q1)
    
    elif sample_type == "Biopsy":
        q1 = "SampleType = 'Biopsy'"
        l.append(q1)

    if cohort_type == "Discovery":
        q2 = "Cohort = 'DiscoverySet'"
        l.append(q2)
    
    elif cohort_type == "Validation":
        q2 = "Cohort = 'ValidationSet'"
        l.append(q2)
        
    if sex == "Male":
        q11 = "Sex = 'Male'"
        l.append(q11)

    if sex == "Female":
        q11 = "Sex = 'Female'"
        l.append(q11)

    if status == "Current":
        q3 = "Genomic_Smoking_Status = 'Current'"
        l.append(q3)

    elif status == "Former":
        q3 = "Genomic_Smoking_Status = 'Former'"
        l.append(q3)
    
    if LC_history == "Yes":
        q4 = "Previous_LC_History = 'Y'"
        l.append(q4)

    elif LC_history == "No":
        q4 = "Previous_LC_History = 'N'"
        l.append(q4)
        
    if LC_job == "Yes":
        q5 = "HighRisk_LC_Job = 'Y'"
        l.append(q5)

    elif LC_job == "No":
        q5 = "HighRisk_LC_Job = 'N'"
        l.append(q5)

    if AB_exp == "Yes":
        q6 = "Asbestos_Exp = 'Y'"
        l.append(q6)

    elif AB_exp == "No":
        q6 = "Asbestos_Exp = 'N'"
        l.append(q6)
    
    if len(MolecularSubtype) > 0 :
        q7 = ""
        if len(MolecularSubtype) == 1 :
            q7 = "Molecular_Subtype = '" + MolecularSubtype[0] + "'"
        else :
            for i in MolecularSubtype[:-1]:
                q = "(Molecular_Subtype = '" + i + "'"+ " OR "
                q7 += q
            q = "Molecular_Subtype = '" + MolecularSubtype[-1] + "')"
            q7 += q
        l.append(q7)
    
    if len(DysplasiaGrade) > 0 :
        q8 = ""
        if len(DysplasiaGrade) == 1 :
            q8 = "Dysplasia_Grade = '"+DysplasiaGrade[0]+ "'"
        else :
            for i in DysplasiaGrade[:-1]:
                q = "(Dysplasia_Grade = '"+ i + "'" + " OR "
                q8 += q
            q = "Dysplasia_Grade = '"+ DysplasiaGrade[-1] + "')"
            q8 += q
        l.append(q8)

    if len(TCGASubtype) > 0 :
        q9 = ""
        if len(TCGASubtype) == 1 :
            q9 = "TCGA_Subtype = '" + TCGASubtype[0] + "'"
        else :
            for i in TCGASubtype[:-1]:
                q = "(TCGA_Subtype = '" + i + "'" + " OR "
                q9 += q
            q = "TCGA_Subtype = '" + TCGASubtype[-1] + "')"
            q9 += q
        l.append(q9)
    
    if len(AgeatBaseline) > 0 :
        q10 = ""
        if len(AgeatBaseline) == 1 :
            q10 = "Age_at_Baseline >= " + float(AgeatBaseline[0][:4]) + " AND Age_at_Baseline <= " + float(AgeatBaseline[0][5:])
        else :
            for i in AgeatBaseline[:-1]:
                q = "(Age_at_Baseline >= " + float(i[0][:4]) + " AND Age_at_Baseline <= " + float(i[0][5:])+" OR "
                q10 += q
            q = "Age_at_Baseline >= "+float(AgeatBaseline[-1][:4])+" AND Age_at_Baseline <= "+float(AgeatBaseline[-1][5:])+ ")"
            q10 += q
        l.append(q10)


    if len(l) == 1:
        query += "WHERE "
        query += l[0]
    
    elif len(l) > 1:
        query += "WHERE "
        for i in l[:-1]:
            query += i
            query += " AND "
        query += l[-1]
    
    query1 += query     
    
    query2 += query
    
    try: cur.execute(query1)
    
    
    except pymysql.Error as e:
        print(e,query1)
        
    try: cur.execute(query2)
    
    except pymysql.Error as e:
        print(e,query2)

    results = cur.fetchall()
    
    print(json.dumps(results))
        
    conn.close()
    
