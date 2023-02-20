# -*- coding: utf-8 -*-
"""
Created on Sun Nov  6 01:21:31 2022

@author: Shree

file structure:
    {main password}
    {website1} {userid1} {password1}
    {website2} {userid2} {password2}
    ...

"""

from tkinter import *
import os
import security as sec
import quant_random_generator as q


mydir = os.path.abspath(os.getcwd())
myname = os.getlogin()

# Designing window for registration
 
def register():
    global reglog_screen
    reglog_screen = Toplevel(main_screen)
    reglog_screen.title("Register")
    reglog_screen.geometry("300x250")
 
    global password
    global password_entry
    password = StringVar()
 
    Label(reglog_screen, text="Please create a password", bg="blue").pack()
    Label(reglog_screen, text="").pack()
    username_lable = Label(reglog_screen, text=f"Hello {myname}!")
    username_lable.pack()

    password_lable = Label(reglog_screen, text="Create Password:")
    password_lable.pack()
    password_entry = Entry(reglog_screen, textvariable=password) #, show='*')
    password_entry.pack()
    Label(reglog_screen, text="").pack()
    Button(reglog_screen, text="Register", width=10, height=1, bg="blue", command = register_user).pack()
 
def display(entry):
    Label(main_screen, text=f"Website: {entry[0]} || UserID: {entry[1]} || Password: {entry[2]}",
          bg="blue", width="300", height="2", font=("Calibri", 13)).pack()
    Label(main_screen, text="").pack()


def new_entry():
    data.append([web.get(), userid.get(), q.generate(16)])
    sec.encrypt('\n'.join([' '.join(line) for line in data]), mydir + '\\data.crypt')
    display(data[-1])
    add_new_sucess()

def add_new():
    global add_new_screen
    add_new_screen = Toplevel(main_screen)
    add_new_screen.title("New Entry")
    add_new_screen.geometry("300x250")
    Label(add_new_screen, text="Please enter new credentials to save").pack()
    Label(add_new_screen, text="").pack()
 
    global web, userid, passw
    global password_verify
 
    web = StringVar()
    userid = StringVar()
 
    global password_login_entry, web_entry
 
    Label(add_new_screen, text=f"Hello {myname}!").pack()

    Label(add_new_screen, text="").pack()
    Label(add_new_screen, text="Website").pack()
    web_entry = Entry(add_new_screen, textvariable=web)
    web_entry.pack()
    
    Label(add_new_screen, text="").pack()
    Label(add_new_screen, text="User ID").pack()
    userid_entry = Entry(add_new_screen, textvariable=userid)
    userid_entry.pack()
    
    Label(add_new_screen, text="").pack()
    Button(add_new_screen, text="Create", width=10, height=1, command = new_entry).pack()
 
# Implementing event on register button

def register_user():
    global data
    password_info = password.get()
    data = [[password_info]]
    sec.encrypt(password_info, mydir + '\\data.crypt')
    

    password_entry.delete(0, END)

    Label(reglog_screen, text="Registration Success", fg="green", font=("calibri", 11)).pack()
    mainloop()
 
# Implementing event on login button 
 
def login_verify():
    password1 = password_verify.get()
    # password_login_entry.delete(0, END)
    
    file = sec.decrypt(mydir + '\\data.crypt').split('\n')
    # file = ['quantum']
    if file[0]== password1:
        login_sucess()
    else:
        password_not_recognised()
 
# Designing popup for login success
 
def login_sucess():
    global login_success_screen
    login_success_screen = Toplevel(reglog_screen)
    login_success_screen.title("Success")
    login_success_screen.geometry("150x100")
    Label(login_success_screen, text="Login Success").pack()
    Button(login_success_screen, text="OK", command=delete_login_success).pack()
    
def add_new_sucess():
    global add_new_success_screen
    add_new_success_screen = Toplevel(add_new_screen)
    add_new_success_screen.title("Success")
    add_new_success_screen.geometry("150x100")
    Label(add_new_success_screen, text="Data added succesfully").pack()
    Button(add_new_success_screen, text="OK", command=delete_add_new).pack()
 
# Designing popup for login invalid password
 
def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(reglog_screen)
    password_not_recog_screen.title("Success")
    password_not_recog_screen.geometry("150x100")
    Label(password_not_recog_screen, text="Invalid Password ").pack()
    Button(password_not_recog_screen, text="OK", command=delete_password_not_recognised).pack()
 
def mainloop():
    global main_screen, data
    
    main_screen = Toplevel(reglog_screen)
    main_screen.geometry("300x250")
    main_screen.title("Account Login")
        
    Button(main_screen, text="New entry", height="2", width="30", command = add_new).pack()
    Label(main_screen, text="").pack()
    
    for line in data[1:]:
        display(line)
        
    # main_screen.mainloop()


# Deleting popups
 
def delete_login_success():
    login_success_screen.destroy()
    mainloop()

def delete_add_new():
    add_new_screen.destroy()

def delete_password_not_recognised():
    password_not_recog_screen.destroy()

# Designing Main(first) window

reglog_screen = Tk()
reglog_screen.geometry("300x250")

if 'data.crypt' in os.listdir():

    reglog_screen.title("Login")
    Label(reglog_screen, text="Please enter details below to login").pack()
    Label(reglog_screen, text="").pack()

    password_verify = StringVar()
 
    Label(reglog_screen, text=f"Hello {myname}!").pack()

    Label(reglog_screen, text="").pack()
    Label(reglog_screen, text="Password:").pack()
    password_login_entry = Entry(reglog_screen, textvariable=password_verify)
    password_login_entry.pack()
    Label(reglog_screen, text="").pack()
    
    Button(reglog_screen, text="Login", width=10, height=1, command = login_verify).pack()

    data = sec.decrypt(mydir + '\\data.crypt').split('\n')
    for i, line in enumerate(data):
        if i==0:
            data[0] = [line]
            continue

        data[i] = data[i].split(' ')
else:
    reglog_screen.title("Register")
 
    password = StringVar()
 
    Label(reglog_screen, text="Please create a password", bg="blue").pack()
    Label(reglog_screen, text="").pack()

    password_lable = Label(reglog_screen, text="Create Password:")
    password_lable.pack()
    password_entry = Entry(reglog_screen, textvariable=password) #, show='*')
    password_entry.pack()
    Label(reglog_screen, text="").pack()
    Button(reglog_screen, text="Register", width=10, height=1, bg="blue", command = register_user).pack()
    
reglog_screen.mainloop()
