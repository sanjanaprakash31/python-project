from tkinter import *
from PIL import Image, ImageTk
import smtplib
import tkinter.messagebox
import mysql.connector
import numpy as  np
import matplotlib.pyplot as plt



db = mysql.connector.connect(user='root', password='',host='127.0.0.1',database='pharmacy')
                                                       #host=Ip of server


win1 = Tk()
win1.geometry("1000x1000")
win1.title("Online Pharmacy")
img1 = Image.open("D:/myDocs/Sem 4 docs/Pharmacy/pic.jpg")
pic = ImageTk.PhotoImage(img1)
la = Label(image=pic)
la.pack()

class MyException(Exception):
    def __init__(self,msg):
        self.msg = msg
    def __str__(self):
        return self.msg


def regpage():

    def exp():
        try:
            if (entry1.get() == "" ):
                raise MyException("You have not entered your Name")
            if (entry2.get() == ""):
                raise MyException("You have not entered your Address")
            if (entry3.get() == ""):
                raise MyException("You have not entered the Username")
            if (entry4.get() == ""):
                raise MyException("You have not entered the id")
            if (entry5.get() == ""):
                raise MyException("You have not entered the password")
        except MyException as args:
            tkinter.messagebox.showinfo("Error", args)
        else :
            mail_verification()


    def regs():
        

        tkinter.messagebox.showinfo("Online Pharmacy", "Registeration sucessfull")
        window.destroy()

    def exit1():
        window.destroy()

    def send_mail():
        server = smtplib.SMTP_SSL("smtp.gmail.com",465)
        server.login("pharmacy1805@gmail.com","21052001@s")
        server.sendmail("pharmacy1805@gmail.com",
                        ""+entry4.get()+"",
                        "Hello "+entry1.get()+", \nYour email id:- "+entry4.get()+" has been registered successfully")
        server.quit()
        add()

    def mail_verification():
        try :
            b=1
            if(entry4.get().endswith("@gmail.com") or entry4.get().endswith("@ves.ac.in") or entry4.get().endswith ("@yahoo.com")):
                b=0
            if (b):
                raise MyException("Mail ID that you have entered is not valid. \nPlease enter valid mail ID")
        except MyException as args:
            tkinter.messagebox.showinfo("Error", args)
        else :
            send_mail()

    def add():

        #print(db)#step to check what goes in
        cursor = db.cursor()#reference to database
        query="insert into user (fname,address,uname,eid,pass) values(%s,%s,%s,%s,%s)"
        values=(entry1.get(),entry2.get(),entry3.get(),entry4.get(),entry5.get())
        cursor.execute(query,values)#query to run
        db.commit()

        regs()



    window = Tk()
    window.geometry("500x500")
    window.title("Online Pharmacy")

    lab1 = Label(window, text="Enter the details to register", relief="solid", width=30).place(x=150, y=100)
    fname=""
    address=""
    username=""
    eID=""
    eP=""
    label1 = Label(window, text="Full Name").place(x=120, y=197)
    label2 = Label(window, text="Address").place(x=120, y=217)
    entry1 = Entry(window, textvar=fname)
    entry1.place(x=187.5, y=200)

    entry2 = Entry(window, textvar=address)
    entry2.place(x=187.5, y=220)

   
    label3 = Label(window, text="Username").place(x=120, y=237)
    entry3 = Entry(window, textvar=username)
    entry3.place(x=187.5, y=240)

    
    label4 = Label(window, text="Email ID").place(x=120, y=257)
    entry4 = Entry(window, textvar=eID)
    entry4.place(x=187.5, y=260)
    
    label5 = Label(window, text="Password").place(x=120, y=277)
    entry5 = Entry(window, textvar=eP)
    entry5.place(x=187.5, y=280)

    

    b1 = Button(window, text='Register', relief='solid', width=10, command=exp).place(x=200, y=350)
    b2 = Button(window, text="Exit", relief="solid", width=10, command=exit1)
    b2.place(x=200, y=375)



def graphs1():

    order_price = np.random.normal(1000, 250, 1000)
    plt.hist(order_price, 50)
    plt.show()

def searchmed():
    def bac():
        tkinter.messagebox.showinfo("Online Pharmacy", "Added to cart sucessfully")
        medwin.destroy()

    def medfound():
        def bac():
            tkinter.messagebox.showinfo("Online Pharmacy", "Added to cart sucessfully")
            fmed.destroy()

        def exit():
            fmed.destroy()

        fmed = Tk()
        fmed.geometry("250x250")
        fmed.title("Online Pharmacy")
        lab3 = Label(fmed, text="Crocin found").place(x=60, y=50)
        bu1 = Button(fmed, text="Add to cart", command=bac).place(x=50, y=200)
        bu2 = Button(fmed, text="Exit", command=exit).place(x=170, y=200)
        medwin.destroy()

    medwin = Tk()
    medwin.geometry("500x500")
    medwin.title("Online Pharmacy")

    lab1 = Label(medwin, text="Search Medicine ", fg="yellow", bg="Black", relief="solid", width=20).place(x=170, y=170)
    var1 = StringVar
    label1 = Label(medwin, text="Medicine Name").place(x=90, y=237)

    entry1 = Entry(medwin, textvar=var1)
    entry1.place(x=187.5, y=240)

    def update(data):
        # Clear the listbox
        my_list.delete(0, END)

        # Add toppings to listbox
        for item in data:
            my_list.insert(END, item)

    def fillout(e):
        # Delete whatever is in the entry box
        entry1.delete(0, END)

        # Add clicked list item to entry box
        entry1.insert(0, my_list.get(ANCHOR))

    def check(e):
        # grab what was typed
        typed = entry1.get()

        if typed == '':
            data = toppings
        else:
            data = []
            for item in toppings:
                if typed.lower() in item.lower():
                    data.append(item)

        # update our listbox with selected items
        update(data)

    toppings = ["Crocin", "Xyzal ", "Mushrooms",
                "Actonel ", "Paracetamol", "Abstral", "Taco"]

    my_list = Listbox(medwin, width=50)
    my_list.pack(pady=40)

    # Add the toppings to our list
    update(toppings)
    # Create a binding on the listbox onclick
    my_list.bind("<<ListboxSelect>>", fillout)

    # Create a binding on the entry box
    entry1.bind("<KeyRelease>", check)

    def exit1():
        medwin.destroy()

    b1 = Button(medwin, text='Purchase', fg="black", bg="cyan", relief='solid', width=10, command=bac).place(x=150,
                                                                                                             y=300)
    b2 = Button(medwin, text="Exit", fg="black", bg="cyan", relief="solid", width=10, command=exit1).place(x=250, y=300)


"""def newwindow1():
    root = Tk()
    root.title("Welcome to second window")
    root.geometry('250x250')
    label2 = Label(root, text="reg s", relief="solid", bg='red', fg='yellow').place(x=30, y=70)
    but_01 = Button(root, text='Demo', relief='solid', width=10, ).place(x=80, y=100)"""


def loginpage():
    def log1():
        tkinter.messagebox.showinfo("Online Pharmacy", "Logged in successfully")
        logpage.destroy()

    def exit1():
        logpage.destroy()

    logpage = Tk()
    logpage.title("Login Page")
    logpage.geometry('300x300')
    lab1 = Label(logpage, text="Enter Username and Password", relief="solid", bg='black', fg='cyan').place(x=60, y=50)
    lab2 = Label(logpage, text="Username").place(x=60, y=110)
    var1 = StringVar
    entry1 = Entry(logpage, textvar=var1).place(x=120, y=110)
    lab3 = Label(logpage, text="Password").place(x=60, y=130)
    var2 = StringVar

    entry2 = Entry(logpage, textvar=var2, show="*").place(x=120, y=130)
    b1 = Button(logpage, text='Login', relief='solid', width=10, command=log1).place(x=100, y=200)
    b2 = Button(logpage, text="Exit", relief="solid", width=10, command=exit1)
    b2.place(x=100, y=225)


but1_win1 = Button(win1, text="Register if new user", relief="solid", bg="crimson", fg="white", command=regpage).place(x=450, y=500)
but2_win1 = Button(win1, text="Login if already an existing user", relief="solid", bg="crimson", fg="white",command=loginpage).place(x=600, y=500)
but3_win1 = Button(win1, text="Search Medicines ", relief="solid", bg="crimson", fg="white", command=searchmed).place(x=300, y=400)
but4_win1 = Button(win1, text="Order Summary", relief="solid", bg="crimson", fg="white", width = 15,command=graphs1).place(x=300,y=450)

win1.mainloop()
