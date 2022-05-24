
import cgitb
cgitb.enable()

#the next line gives us a convenient way to insert values into strings
from string import Template 



#retrieve form data from the web server
form = cgi.FieldStorage()

#test to see if there was any query string
if (form):
    #get individual values from the form data
    #use getvalue when there is only one instance of the key in the query string
    name = form.getvalue("name")       
    dept = form.getvalue("department")

    #use getlist when there are multiple instances of the key in the query string (as produced by checkboxes)
    lang = form.getlist("language") 
    
    #convert list to a comma separated string
    lang_list = ",".join(lang)
	
	restaurant = form.getvalue("restaurant")
    #send back the new html
    
    #create a template for the html
    #substitions will be made between ${} 
    html_template = Template(
    """
    <html>
        <head>
            <title>My program's response</title>
        </head>
        <body>
            <p>
            Hi ${name}! <br>
            Your department is ${dept}. <br>
            Your favorite programming languages are ${lang_list} <br>
            Your favorite restaurant is ${restaurant}<br>
            </p>
        </body>
    </html>    
    """
    )
    
    #next line is always required as first part of html output
    print("Content-type: text/html\n")
    
    #print the html
    #note within the safe_substitute method, in each pair x=y, 
    #the first word (x) is from the ${} in the template 
    #and the second word (y) is a variable in the program that should fill in that space
    print(html_template.safe_substitute(name=name, dept=dept, lang_list=lang_list, restaurant=restaurant))
    
    
else:
    #no form data
    html_template = Template(
    """
    <html>
        <head>
            <title>My program's response</title>
        </head>
        <body>
            <p>
            You didn't send any data!
            </p>
        </body>
    </html> 
    """
    )
    
    #next line is always required as first part of html output
    print("Content-type: text/html\n")
    
    #print the html
    #nothing to substitute here
    print(html_template.safe_substitute())
