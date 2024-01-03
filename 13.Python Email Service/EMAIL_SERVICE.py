import email
from re import A
import pandas as pd
import smtplib
import numpy as np      
from openpyxl import load_workbook
from openpyxl.utils.cell import get_column_letter
import sqlite3
import requests

def start(): #mian starting fucntion 
    choice=input("""do you want to add type "add" or remove email from subscription list type "remove" or  to send out Email type  "Email out" :""").lower() #ask use for input input
    if choice == "email out":
        emailbot()
    elif choice=="add":  #sorts throught option if user types add it will take user to funtion where it will add user to subscription list
        emailadd()  #lead to funtion where user can add eamil ,name , set password for account to subscription list 
    elif choice=="remove": #sorts throught option if user types remove it will take user to funtion where it will remove user to subscription list
        emailrem()    #lead to funtion where user can remove eamil ,name , set password for account to subscription list 
    else: #if none of earlier option can be used if will just send user to start of program
        start()

def emailrem():
    email=str(input("Enter your email assosiated with with email subusbsription:")) # takes users email
    conect=sqlite3.connect("data.db")# connects to databse
    c=conect.cursor()# connects to databse
    c.execute("DELETE FROM customerF WHERE emails=?", (email,))# deletes email from databse wiuth thier name and ervything to databse
    conect.commit()# commits to databse
    conect.close()# clsoes connectition  to databse
    restart() # goes to fution that will eatither restart funtion or end funtion

def emailadd(): # this function will add user to subscription list so when email go out they get email
    firstname=input("Enter your for name:")# takes users first  name
    lastname=input("Enter your surname:")# takes users last nme
    email=input("Enter your email address:")# takes users email
    conect=sqlite3.connect("data.db")# connects to databse
    c=conect.cursor()# connects to databse
    r=c.execute("""SELECT emails FROM customerF""")# looks if email is in   databse
    data = c.fetchall()# fetches inforamtion
    listt=tuple(i[0] for i in data) #makes into list that cdoe can use
    if email in listt: #if email exist it will go restart funtion 
        print("your email address in use for our email newslater subscription service")
        restart()
    if email not in listt:#if email deso not exist it will add meail name and to databse 
        add(firstname,lastname,email) # add funtion
    else:#it goes to rest fution 
        print("sorry a probelm has ocuured pls try again")
        restart()

def add(firstname,lastname,email): #funtion adds email to datbse
    conect=sqlite3.connect("data.db") #connet to databse 
    c=conect.cursor() #connet to databse 
    c.execute("INSERT INTO customerF (first_name,last_name,emails,) VALUES (?,?,?)",(firstname,lastname,email)) # insert data to databse
    conect.commit()# commits dat to database
    conect.close()#clsoese conection   to database
    restart() #it goes to rest fution 

def emailbot():
    
    your_name = "talha" # login info for gmail
    your_email = "noreplyresit@gmail.com"  # login info for gmail
    your_password = "aQW8m7WcKTK*NpA4m-@D_$#AT8rE7MSS9m*NS?7wv?_Bbd-GEnu3MrABqY+@23FXeA" # login info for gmail

    server = smtplib.SMTP_SSL('smtp.gmail.com', 465) # connects to email server
    server.ehlo()# connects to email server
    server.login(your_email, your_password)# connects to email server

    conect=sqlite3.connect("data.db") #connect to databse
    c=conect.cursor()#connect to databse
    datafirstname=c.execute("""SELECT first_name FROM customerF""") #finds  first names of  people
    data_firstname = c.fetchall() #fethces   first names of  people
    list_firstname=tuple(i[0] for i in data_firstname) # makes list of FIRST name that code can use

    datalastname=c.execute("""SELECT last_name FROM customerF""") #finds  last names of  people
    data_lastname = c.fetchall()#fethces   last names of  people
    list_lastname=tuple(i[0] for i in data_lastname)# makes list of FIRST name that code can use

    dataemail=c.execute("""SELECT emails FROM customerF""")#finds  email of  people
    data_email = c.fetchall()#fethces   emails of  people
    list_email=tuple(i[0] for i in data_email)# makes list of emails that code can use
    max=list_email

    # BBC news api 
    main = " https://newsapi.org/v1/articles?source=bbc-news&sortBy=top&apiKey=be79bb67b07f469ab415e2aef0aeb9e0" #help connect to api
    # fetching data in json format 
    open_page = requests.get(main).json() 
    # getting all articles in a string article 
    article = open_page["articles"] 
    # empty list which will  
    # contain all trending news 
    content = []   
    for art in article: 
        content.append(art["title"]) 
        
    for i in range(len(content)): 
        # festches and sorts out all trending news 
        result=(i + 1, content[i])
        result = "\n".join(f'({index} {item!r}' for index, item in enumerate(content, start=1))
        result=result.replace("(","").center(50)

    for i in range(len(max)):
        fullname=list_firstname[i]+" "+list_lastname[i]  #combines  first anme and last name   for specifc user in order stored 
        lastemail=list_email[i] #stores  email  for specifc user in order stored 
        #formats how  email will look wen send out 
        fullemail=(f"From:{your_name} <{your_email}>\nTo:{fullname}<{lastemail}>\n Subject: BBC News\n\ntodays news\n+{result}")
    
        try: # trys to send out email to email
            server.sendmail(your_email, [lastemail], fullemail)
            print('Email to {} successfully sent!\n\n'.format(email))
        except Exception as e: # trys to send out email to email if it does not wrok tells it did not work specific user 
            print('Email to {} could not be sent :( because {}\n\n'.format(lastemail, str(e)))
    server.close

def restart(): # ths iis reatrt function 
    choice=input("do you want to go to Main menu then type 1 or if you wish to quit porgram type 2 ") #gives uer option top start program all over or end it 
    if choice=="1":
        start()# takes to satrt of funtion
    if choice =="2":
        exit() # takes to funtio that ends program

def exit(): #ends porgram
    print("Thank you for using our serveices")
    
start()

