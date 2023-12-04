import customtkinter as ctk
import subprocess
import tkinter
import os
from PIL import ImageTk, Image
import pandas as pd
import csv

main_page = ctk.CTk()
main_page.title('inKOGnito')
main_page.geometry('1366x768')

def login_page():
    pass

def authenticate_User(username, password):
    global userData
    if userData is not None:
        matches = userData.index[(userData.Username == username) & (userData.Password == password)].tolist()
        return matches 
    else: 
        return False

def register_Acc():
    login_Frame.pack_forget()
    register_Frame = ctk.CTkFrame(
        master = main_page,
        height = 500,
        width = 500,
        corner_radius = 50,
        fg_color = ('#FFF6F6', '#191919'),
        border_width = 10,
        border_color = ('#F875AA', '#8758FF'))
    register_Frame.place(
        relx = 0.5,
        rely = 0.5,
        anchor = tkinter.CENTER)

    app_Welcome = ctk.CTkLabel(
        master = register_Frame,
        text = 'Welcome to Arcade Games!',
        font = ('Alpharush - Retro Gaming Typeface', 25, 'bold'))
    app_Welcome.place(
        x = 58,
        y = 45)

    create_Acc = ctk.CTkLabel(
        master = register_Frame,
        text = 'Create your Account',
        font = ('Ubuntu', 20, 'bold'))
    create_Acc.place(
        x = 58,
        y = 100)

    enter_Uniqueuser = ctk.CTkLabel(
        master = register_Frame,
        text = 'Enter Unique Username',
        font = ('Ubuntu', 15))
    enter_Uniqueuser.place(
        x = 58,
        y = 155)

    enter_Newuser = ctk.CTkEntry(
        register_Frame,
        height = 40,
        width = 250,
        placeholder_text = 'Create your Username')
    enter_Newuser.place(
        x = 58,
        y = 185)

    enter_Uniquepass = ctk.CTkLabel(
        master = register_Frame,
        text = 'Enter Password',
        font = ('Ubuntu', 15))
    enter_Uniquepass.place(
        x = 58,
        y = 240)

    enter_Newpass = ctk.CTkEntry(
        register_Frame,
        height = 40,
        width = 250,
        placeholder_text = 'Create your Password',
        show = '*')
    enter_Newpass.place(
        x = 58,
        y = 270)

    def write_NewUser():
        user_input = enter_Newuser.get()
        pass_input = enter_Newpass.get()

        if user_Exist(user_input):
            print('Username already taken. Please choose another one.')
        else:
            data_to_append = [[user_input,  pass_input]]
            file = open('userinfo.csv', 'a', newline = '')
            writer = csv.writer(file)

            writer.writerows(data_to_append)

            file.close()
            userData = pd.read_csv('userinfo.csv')

        login_Interface()
    create_Button = ctk.CTkButton(
        register_Frame,
        fg_color = "#F8C8C8",
        text_color = "#000000",
        height = 35,
        width = 90,
        text = 'Create',
        font = ('Ubuntu', 15, 'bold'),
        command = write_NewUser)
    create_Button.place(
        x = 139,
        y = 340)

    have_Acc = ctk.CTkLabel(
        register_Frame,
        text = 'Already have Account?',
        font = ("Helvetica", 12))
    have_Acc.place(
        x = 90,
        y = 400)

    signin_Button = ctk.CTkButton(
        register_Frame,
        fg_color = "transparent",
        text_color = "#F8C8C8",
        height = 35,
        width = 30,
        text = 'Sign In',
        font = ('Helvetica', 12,'bold'),
        command = login_page)
    signin_Button.place(
        x = 220,
        y = 397.5)

def authentication():
    global userData
    username = user_Entry.get()
    password = pass_Entry.get()
    print(username, password)

    authenticated = authenticate_User(username, password)

    if authenticated:
        start_button_event()
        print('Login successful!')
    else:
        print('Invalid username or password. Please try again.')

login_Frame = ctk.CTkFrame(
    master = main_page,
    height = 500,
    width = 500,
    corner_radius = 50,
    fg_color = ('#FFF6F6', '#191919'),
    border_width = 10,
    border_color = ('#F875AA', '#8758FF'))

login_Frame.place(
    relx = 0.5,
    rely = 0.5,
    anchor = tkinter.CENTER)

log_Acc = ctk.CTkLabel(
    master = login_Frame,
    text = 'Login to your Account',
    font = ('Ubuntu', 20, 'bold'))
log_Acc.place(
    x = 145,
    y = 100)

app_Welcome = ctk.CTkLabel(
    master = login_Frame,
    text = 'Welcome to Arcade Games!',
    font = ('Alpharush - Retro Gaming Typeface', 25, 'bold'))
app_Welcome.place(
    x = 92,
    y = 45)

enter_User = ctk.CTkLabel(
    master = login_Frame,
    text = 'Username',
    font = ('Ubuntu', 15))
enter_User.place(
    x = 133,
    y = 155)

user_Entry = ctk.CTkEntry(
    login_Frame,
    height = 40,
    width = 250,
    placeholder_text = 'Enter your Username')
user_Entry.place(
    x = 120,
    y = 185)

enter_Pass = ctk.CTkLabel(
    master = login_Frame,
    text = 'Password',
    font = ('Ubuntu', 15))
enter_Pass.place(
    x = 133,
    y = 240)

pass_Entry = ctk.CTkEntry(
    login_Frame,
    height = 40,
    width = 250,
    placeholder_text = 'Enter your Password',
    show = '*')
pass_Entry.place(
    x = 120,
    y = 270)

login_Button = ctk.CTkButton(
    login_Frame,
    fg_color = ("#F8C8C8", '#8758FF'),
    text_color = "#000000",
    height = 35,
    width = 90,
    text = 'Login',
    font = ('Ubuntu', 15, 'bold'),
    hover_color = ('#AEDEFC', '#5CB8E4'),
    command = authentication)
login_Button.place(
    x = 195,
    y = 340)

no_Acc = ctk.CTkLabel(
    login_Frame,
    text = 'No Account?',
    font = ("Helvetica", 12))
no_Acc.place(
    x = 150,
    y = 400)

registeracc_button = ctk.CTkButton(
    login_Frame,
    fg_color = "transparent",
    text_color = ("#F875AA", '#8758FF'),
    height = 35,
    width = 30,
    text = 'Create a New One',
    hover_color = ('#AEDEFC', '#5CB8E4'),
    font = ('Helvetica', 12,'bold'),
    command = register_Acc)
registeracc_button.place(
    x = 225,
    y = 395.5)

def mode_event():
    if switch_var.get() == 'on':
        ctk.set_appearance_mode("light")
    else: 
        ctk.set_appearance_mode("dark")
switch_var = ctk.StringVar(value='on')
mode_switch = ctk.CTkSwitch(
    master = main_page,
    text = 'Change Mode',
    button_hover_color = ('#F875AA', "#8758FF"),
    progress_color = ('#AEDEFC', '#191919'),
    button_color = ('#F875AA', "#8758FF"),
    command = mode_event,
    variable = switch_var,
    onvalue = 'on',
    offvalue = 'off')
mode_switch.place(
    x = 25,
    y = 670)

main_page.mainloop()