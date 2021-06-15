from tkinter import*
from tkinter import ttk
import tkinter.messagebox

window=Tk()
#Declaring Window Title
window.title("Employee Registration Form")
#Declaring window size
window.geometry('700x500')
#Declaring Window Color
window.configure(background= "lightblue");

label1 = Label(window,text = "Employee Registration Form", font=("bold",20)).grid(row=0,column=2)
Firstname = Label(window ,text = "First Name",width=20,font=("bold",10)).grid(row=1,column=1)
Lastname = Label(window ,text = "Last Name",width=20,font=("bold",10)).grid(row=2,column=1)
Email = Label(window ,text = "Email id",width=20,font=("bold",10)).grid(row=3,column=1)
Mobile = Label(window ,text = "Contact Number",width=20,font=("bold",10)).grid(row=4,column=1)
Employee_id = Label(window ,text = "Employee id",width=20,font=("bold",10)).grid(row=5,column=1)
Passport_No = Label(window ,text = "Passport Number",width=20,font=("bold",10)).grid(row=6,column=1)
Gender = Label(window ,text = "Gender",width=20,font=("bold",10)).grid(row=7,column=1)
var = IntVar()
Radiobutton(window,text = "Male",padx = 30, variable=var, value=1).grid(row=7,column=2)
Radiobutton(window,text = "Female",padx = 20, variable=var, value=2).grid(row=7,column=3)                                                                                  
Monthly_income = Label(window ,text = "Monthly income",width=20,font=("bold",10)).grid(row=8,column=1)
Country = Label(window ,text = "Country",width=20,font=("bold",10)).grid(row=9,column=1)
list1=['Australia','China','Canada','France','India','Italy','U.S.A','U.K']
c=StringVar()
droplist=OptionMenu(window,c,*list1)
droplist.config(width=15)
c.set('select your country')
droplist.grid(row=9,column=2)                                                                                  
Address = Label(window ,text = "Address",width=20,font=("bold",10)).grid(row=10,column=1)
var1=IntVar()
Checkbutton(window,text="Accept Terms and Condition", variable=var1).grid(row=11,column=2)                                                                                
                                                                                  

Firstname1 = Entry(window).grid(row=1,column=2)
Lastname1 = Entry(window).grid(row=2,column=2)
Email1 = Entry(window).grid(row=3,column=2)
Mobile1 = Entry(window).grid(row=4,column=2)
Employee_id1 = Entry(window).grid(row=5,column=2)
Passport_No1 = Entry(window).grid(row=6,column=2)
Monthly_income1 = Entry(window).grid(row=8,column=2)
Address1 = Entry(window).grid(row=10,column=2)
                                                                        
def onClick():
    tkinter.messagebox.showinfo("Welcome", "Yor Details Submitted  Successfully !")

Button(window,text="Submit", command=onClick,width=20,bg='red',fg='white').grid(row=13,column=2)
window.mainloop()
