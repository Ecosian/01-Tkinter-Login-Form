from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import os
import sys
# Designing window for registration

def register():
    global register_screen
    register_screen = Toplevel(main_screen)
    register_screen.title("Register")
    register_screen.geometry("200x150")
    windowWidth = register_screen.winfo_reqwidth()
    windowHeight = register_screen.winfo_reqheight()
    positionRight = int(register_screen.winfo_screenwidth()//2.25 - windowWidth//2.25)
    positionDown = int(register_screen.winfo_screenheight()//2.25 - windowHeight//2.25)
    register_screen.geometry("+{}+{}".format(positionRight, positionDown))  
    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()

    username_lable = Label(register_screen, text="Username * ")
    username_lable.pack()
    username_entry = Entry(register_screen, textvariable=username)
    username_entry.pack()
    password_lable = Label(register_screen, text="Password * ")
    password_lable.pack()
    password_entry = Entry(register_screen, textvariable=password, show='*')
    password_entry.pack()
    Label(register_screen, text="").pack()
    but1 = ttk.Button(register_screen, text="Register", width=20, command = register_user)
    but1.pack()
 
# Designing window for login 
 
def login():
    global login_screen
    login_screen = Toplevel(main_screen)
    login_screen.title("Login")
    login_screen.geometry("220x160")
    windowWidth = login_screen.winfo_reqwidth()
    windowHeight = login_screen.winfo_reqheight()
    positionRight = int(login_screen.winfo_screenwidth()//2.25 - windowWidth//2.25)
    positionDown = int(login_screen.winfo_screenheight()//2.25 - windowHeight//2.25)
    login_screen.geometry("+{}+{}".format(positionRight, positionDown))    
 
    global username_verify
    global password_verify
 
    username_verify = StringVar()
    password_verify = StringVar()
 
    global username_login_entry
    global password_login_entry
 
    Label(login_screen, text="Username * ").pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify)
    username_login_entry.pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="Password * ").pack()
    password_login_entry = Entry(login_screen, textvariable=password_verify, show= '*')
    password_login_entry.pack()
    Label(login_screen, text="").pack()
    but2 = ttk.Button(login_screen, text="Login", width=20, command = login_verify)
    but2.pack()
 
# Implementing event on register button
 
def register_user():
 
    username_info = username.get()
    password_info = password.get()

    if username_info == "" or password_info == "":
        messagebox.showerror("Error", "Please Enter Something First")
    else:
        file = open(username_info, "w")
        file.write(username_info + "\n")
        file.write(password_info)
        file.close()
        messagebox.showinfo("Info", "Registration Successful")
        username_entry.delete(0, END)
        password_entry.delete(0, END)
        register_screen.destroy()
        
# Implementing event on login button 
 
def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()

    if username1 == "" or password1 == "":
        messagebox.showerror("Error", "Please Enter Something First")
    else:
        list_of_files = os.listdir()
        if username1 in list_of_files:
            file1 = open(username1, "r")
            verify = file1.read().splitlines()
            if password1 in verify:
                login_sucess() 
            else:
                password_not_recognised()
 
        else:
            user_not_found()
            username_login_entry.delete(0, END)
            password_login_entry.delete(0, END)
            
 
# Designing popup for login success
 
def login_sucess():
    global login_success_screen
    login_success_screen = Toplevel(login_screen)
    login_success_screen.title("Success")
    login_success_screen.geometry("100x50")
    Label(login_success_screen, text="Login Successful").pack()
    windowWidth = login_success_screen.winfo_reqwidth()
    windowHeight = login_success_screen.winfo_reqheight()
    positionRight = int(login_success_screen.winfo_screenwidth()//2 - windowWidth//2)
    positionDown = int(login_success_screen.winfo_screenheight()//2 - windowHeight//2)
    login_success_screen.geometry("+{}+{}".format(positionRight, positionDown)) 
    but3 = ttk.Button(login_success_screen, text="OK", command=delete_login_success)
    but3.pack()
         
# Designing popup for login invalid password
 
def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(login_screen)
    password_not_recog_screen.title("Success")
    password_not_recog_screen.geometry("100x50")
    Label(password_not_recog_screen, text="Invalid Password!").pack()
    password_login_entry.delete(0, END)
    windowWidth = password_not_recog_screen.winfo_reqwidth()
    windowHeight = password_not_recog_screen.winfo_reqheight()
    positionRight = int(password_not_recog_screen.winfo_screenwidth()//2 - windowWidth//2)
    positionDown = int(password_not_recog_screen.winfo_screenheight()//2 - windowHeight//2)
    password_not_recog_screen.geometry("+{}+{}".format(positionRight, positionDown))
    but4 = ttk.Button(password_not_recog_screen, text="OK", command=delete_password_not_recognised)
    but4.pack()
 
# Designing popup for user not found
 
def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Toplevel(login_screen)
    user_not_found_screen.title("Success")
    user_not_found_screen.geometry("100x50")
    Label(user_not_found_screen, text="User Not Found!").pack()
    windowWidth = user_not_found_screen.winfo_reqwidth()
    windowHeight = user_not_found_screen.winfo_reqheight()
    positionRight = int(user_not_found_screen.winfo_screenwidth()//2 - windowWidth//2)
    positionDown = int(user_not_found_screen.winfo_screenheight()//2 - windowHeight//2)
    user_not_found_screen.geometry("+{}+{}".format(positionRight, positionDown))
    but5 = ttk.Button(user_not_found_screen, text="OK", command=delete_user_not_found_screen)
    but5.pack()
 
# Deleting 5popups
 
def delete_login_success():
    login_success_screen.destroy()
    login_screen.destroy()
    import quizprogram.pyw
 
def delete_password_not_recognised():
    password_not_recog_screen.destroy()
        
def delete_user_not_found_screen():
    user_not_found_screen.destroy()
  
# Designing Main(first) window
 
def main_account_screen():
    global main_screen
    main_screen = Tk()
    main_screen.geometry("240x180+0+0")
    main_screen.title("Account Login")
    Label(text="Select Your Choice", bg="black", fg="white", width="300", height="2", font=("Calibri", 13)).pack()
    Label(text="").pack()
    but7 = ttk.Button(text="Login",width="20", command = login)
    but7.pack()
    Label(text="").pack()
    but6 = ttk.Button(text="Register", width="20", command=register)
    but6.pack()
 
    main_screen.mainloop()

main_account_screen()
