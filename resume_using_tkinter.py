from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox

mainpage = Tk()
mainpage.geometry('2000x1000')
mainpage.title('Register Form')
mainpage.config(bg='pink')

def addData():
    username = name.get()
    linked = link.get()
    pl = place.get()
    mail = mailid.get()
    phone = phno.get()
    gn = ""
    if gender.get()==1:
        gn = "Male"
    elif gender.get()==2:
        gn = "Female"
    else:
        gn = "Transgender"

    skill = skills.get()
    obj = tx.get(1.0,END)
    degree = deg.get()
    year = yop.get()
    proj = project.get()
    intern = internship.get()
    ach = achieve.get()
    li=[username,mail,phone,linked,pl,gn,skill,obj,degree,year,proj,intern,ach]

    for a in li:
        if a=="":
            messagebox.showerror("Error","Please Enter All the Fields")
            break            
    else:
        fname = 'C:\\Users\\Pavithra devi\\OneDrive\\Desktop\\python\\github\\{}.doc'.format(username)
        fi = open(fname,'w')
        fi.write("  RESUME ")
        fi.write("\n\nOBJECTIVE ")
        fi.write("\n"+obj)
        fi.write("\n\nPERSONAL DETAILS")
        fi.write("\nNAME            : "+username)
        fi.write("\nEMAIL           : "+mail)
        fi.write("\nPHONE           : "+phone)
        fi.write("\nGENDER          : "+gn)
        fi.write("\nLINKED IN URL   : "+linked)
        fi.write("\nPLACE           : "+pl)
        fi.write("\n\nEDUCATION DETAILS")
        fi.write("\nDEGREE          : "+degree)
        fi.write("\nYEAR OF PASSING : "+year)
        fi.write("\nSKILLS          : "+skill)
        fi.write("\nINTERNSHIP      : "+intern)
        fi.write("\nPROJECT         : "+proj)
        fi.write("\nACHIVEMENTS     : "+ach)
        fi.close()
        messagebox.showinfo("SUCCESS","SUCCESSFULLY CREATED A RESUME");

def clearData():
    name.delete(0,END)
    mailid.delete(0,END)
    phno.delete(0,END)
    link.delete(0,END)
    place.delete(0,END)
    deg.delete(0,END)
    phno.delete(0,END)
    yop.delete(0,END)
    project.delete(0,END)
    internship.delete(0,END)
    tx.delete(1.0,END)
    gender.set(None)
    achieve.delete(0,END)
    skills.delete(0,END)

gender = IntVar()

title = Label(mainpage,text='RESUME MAKER',font=('Times New Roman',20,'bold'),bg='#7F1C77',fg='white')
title.place(x=10,y=20,width=1250,height=30)

resLabel = Label(mainpage,text='PERSONEL DETAILS ',font=14,bg='#F3B25A')
resLabel.place(x=70,y=70)

nameLabel = Label(mainpage,text='Name  ',font=14,bg='pink')
nameLabel.place(x=10,y=110)

name = Entry(mainpage,font=14)
name.place(x=200,y=110)

mailLabel = Label(mainpage,text='Mail id  ',font=14,bg='pink')
mailLabel.place(x=10,y=160)

mailid = Entry(mainpage,font=14)
mailid.place(x=200,y=160)

phoneLabel = Label(mainpage,text='Phone number ',font=14,bg='pink')
phoneLabel.place(x=10,y=210)

phno = Entry(mainpage,font=14)
phno.place(x=200,y=210)

linkLabel = Label(mainpage,text='Linkedin Profile  ',font=14,bg='pink')
linkLabel.place(x=10,y=260)

link = Entry(mainpage,font=14)
link.place(x=200,y=260)

placeLabel = Label(mainpage,text='Place',font=14,bg='pink')
placeLabel.place(x=10,y=310)

place = Entry(mainpage,font=14)
place.place(x=200,y=310)

genderLabel = Label(mainpage,text='Select Gender ',font=14,bg='pink')
genderLabel.place(x=10,y=360)

rb1 = Radiobutton(mainpage,text='Male',font=14,bg='pink',variable=gender,value=1)
rb1.place(x=200,y=360)

rb2 = Radiobutton(mainpage,text='Female',font=14,bg='pink',variable=gender,value=2)
rb2.place(x=200,y=390)

rb3 = Radiobutton(mainpage,text='Transgender',font=14,bg='pink',variable=gender,value=3)
rb3.place(x=200,y=420)

skillsLabel = Label(mainpage,text='Skills ',font=14,bg='pink')
skillsLabel.place(x=10,y=470)

skills = Combobox(mainpage,values=['Python','Java','C','C++','Django'])
skills.place(x=200,y=470)

objLabel = Label(mainpage,text='OBJECTIVE',font=14,bg='#F3B25A')
objLabel.place(x=900,y=70)

tx = Text(mainpage,)
tx.place(x=800,y=110,width=440,height=100)

expLabel = Label(mainpage,text='EDUCATION ',font=14,bg='#F3B25A')
expLabel.place(x=900,y=230)

degreeLabel = Label(mainpage,text='Name of the degree  ',font=14,bg='pink')
degreeLabel.place(x=800,y=280)

deg = Entry(mainpage,font=14)
deg.place(x=1000,y=280)

yopLabel = Label(mainpage,text='Year of Passing  ',font=14,bg='pink')
yopLabel.place(x=800,y=330)

yop = Entry(mainpage,font=14)
yop.place(x=1000,y=330)

projectLabel = Label(mainpage,text='Projects ',font=14,bg='pink')
projectLabel.place(x=800,y=380)

project = Entry(mainpage,font=14)
project.place(x=1000,y=380)

eduLabel = Label(mainpage,text='EXPERIENCE ',font=14,bg='#F3B25A')
eduLabel.place(x=900,y=430)

internLabel = Label(mainpage,text='Internship details   ',font=14,bg='pink')
internLabel.place(x=800,y=470)

internship = Entry(mainpage,font=14)
internship.place(x=1000,y=470)

achLabel = Label(mainpage,text='Achievements  ',font=14,bg='pink')
achLabel.place(x=800,y=520)

achieve = Entry(mainpage,font=14)
achieve.place(x=1000,y=520)





sub = Button(mainpage,text='SUBMIT',font=15,bg='#AFEC87',activebackground='#F3B73E',command=addData)
sub.place(x=500,y=600,width=100)

clear = Button(mainpage,text='CLEAR',font=15,bg='#AFEC87',activebackground='#F3B73E',command=clearData)
clear.place(x=650,y=600,width=100)

sb = Scrollbar(mainpage,)
sb.pack(side=RIGHT,fill=Y)

mainpage.mainloop()
