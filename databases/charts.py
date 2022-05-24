#!/usr/bin/python3
import cgi
import pymysql
import cgitb
cgitb.enable()

conn = pymysql.connect(host='bioed.bu.edu',
    user= 'ajzheng',
    password= 'KPgkmns89!',
    db= 'miRNA',
    port = 4253) 
    
cur = conn.cursor()

query = """ 
Select miRNA.name, count(*)
From miRNA.targets join miRNA.miRNA on miRNA.mid = targets.mid
group by miRNA.name
"""

cur.execute(query)
results = cur.fetchall()

plot_data = [['miRNAs','Targets']]

for row in results:
    plot_data.append([row[0],row[1]])

conn.close()

html_template = """
<html>
    <head>

        <script type="text/javascript" src="https://www.gstatic.com/charts/loader.js"></script>
        <script type="text/javascript">
        
            google.charts.load("current", {packages:["corechart"]});
            google.charts.setOnLoadCallback(drawChart);
            function drawChart() {

                // Create the data table and store it in variable "data".
                var data = google.visualization.arrayToDataTable(%s);

                // Set chart options
                var options = {'title':'Number of miRNAs versus the number of genes they target'
                              };

                var chart = new google.visualization.Histogram(document.getElementById('chart_div'));
                
                // Draw the chart with the data and options previously defined
                chart.draw(data, options);
            }
        </script>
    </head>

    <body>
    <!--Div that will hold the pie chart-->
        <div id="chart_div"></div>
    </body>
</html>
"""%(plot_data)
print("Content-type: text/html\n")
print(html_template)

