#########################  Importing Library #############################################

from flask import Flask, flash, request, redirect, url_for, render_template,Response
import urllib.request
import os
from werkzeug.utils import secure_filename
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from skimage.transform import resize
from skimage.io import imread
from sklearn import svm
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import train_test_split
import glob
from tkinter import *
import tkinter.messagebox as tkMessageBox
from tkinter import messagebox
import sqlite3
import tkinter as tk
import pickle

##################################    Importing library finished         ###################################

##################################    Flask Starter                      ###################################

app = Flask(__name__)
model = pickle.load(open('model3.pkl','rb'))
UPLOAD_FOLDER = 'static/uploads/'
app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/file_upload',methods=['POST','GET'])
def file_upload():
    def allowed_file(filename):
        return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


    def computation():
        
        # predicting image which you have uploaded
        flat1_data_arr=[]
        file_type = '/*png'
        files = glob.glob(UPLOAD_FOLDER + file_type)
        max_file = max(files, key=os.path.getctime)
        print(max_file)

        img1_array=imread(max_file)
        img1_resized=resize(img1_array,(150,150,3))
        flat1_data_arr.append(img1_resized.flatten())

        flat1_data=np.array(flat1_data_arr)
        df1=pd.DataFrame(flat1_data)
        y_pred=model.predict(df1)
        print(y_pred[0])
        if y_pred[0] == 0:
            msg = "After training, I guess this is a fire image"
        else:
            msg = "After training I guess this is a non fire image"

        return y_pred[0]



    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        flash('No image selected for uploading')
        return redirect(request.url)
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        flash('Image successfully uploaded')
        path1 = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        s = computation()
        if s==0:
            msg="After training, I guess this is a fire image"
        else:
            msg="After training I guess this is a non fire image"
        top=Tk()
        messagebox.showinfo("information",msg)
        return render_template('temp.html',user=u1.title(),enter=True)
    else:
        flash('Allowed image types are - png, jpg, jpeg, gif')
        return redirect(request.url)
    




@app.route('/signup',methods=['POST','GET'])
def signup():
    def register():
        register_screen = Toplevel(main_screen) # The Toplevel widget work pretty much like Frame, but it is displayed in a separate, top-level window
        register_screen.title("Register")
        register_screen.geometry("300x250")
        global username
        global password
        global username_entry
        global password_entry
        # Set text variables
        username = StringVar()
        password = StringVar()
        # Set label for user's instruction
        Label(register_screen, text="Please enter details below", bg="blue").pack()
        Label(register_screen, text="").pack()
        # Set username label
        username_lable = Label(register_screen, text="Username * ")
        username_lable.pack()
        # Set username entry
        # The Entry widget is a standard Tkinter widget used to enter or display a single line of text
        username_entry = Entry(register_screen, textvariable=username)
        username_entry.pack()
        #set password label
        password_lable = Label(register_screen, text="Password * ")
        password_lable.pack()
        # Set password entry
        password_entry = Entry(register_screen, textvariable=password, show='*')
        password_entry.pack()
        Label(register_screen, text="").pack()
        Button(register_screen, text="Register", width=10, height=1, bg="blue",command = register_user).pack()

    def login():
        global login_screen
        login_screen = Toplevel(main_screen)
        login_screen.title("Login")
        login_screen.geometry("300x250")
        Label(login_screen, text="Please enter details below to login").pack()
        Label(login_screen, text="").pack()
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
        Button(login_screen, text="Login", width=10, height=1, command = login_verify).pack()

    # Implementing event on register button
    def register_user():
        username_info = username.get()
        password_info = password.get()
        print("hii")
        file = open(username_info, "w")
        file.write(username_info + "\n")
        file.write(password_info)
        file.close()
        print("hello")
        username_entry.delete(0, END)
        password_entry.delete(0, END)
        Label(register_screen, text="Registration Success", fg="green", font=("calibri", 11)).pack()

    # Implementing event on login button
    def login_verify():
        username1 = username_verify.get()
        password1 = password_verify.get()
        username_login_entry.delete(0, END)
        password_login_entry.delete(0, END)
        list_of_files = os.listdir()
        if username1 in list_of_files:
            file1 = open(username1, "r")
            verify = file1.read().splitlines()
            if password1 in verify:
                global u1
                u1 = username1
                print(u1)
                login_sucess()
            else:
                password_not_recognised()
        else:
            user_not_found()
    
    # Designing popup for login success
    def login_sucess():
        global login_success_screen
        login_success_screen = Toplevel(login_screen)
        login_success_screen.title("Success")
        login_success_screen.geometry("150x100")
        Label(login_success_screen, text="Login Success").pack()
        Button(login_success_screen, text="OK", command=delete_login_success).pack()
        

    # Designing popup for login invalid password
    def password_not_recognised():
        global password_not_recog_screen
        password_not_recog_screen = Toplevel(login_screen)
        password_not_recog_screen.title("Success")
        password_not_recog_screen.geometry("150x100")
        Label(password_not_recog_screen, text="Invalid Password ").pack()
        Button(password_not_recog_screen, text="OK", command=delete_password_not_recognised).pack()

    # Designing popup for user not found
    def user_not_found():
        global user_not_found_screen
        user_not_found_screen = Toplevel(login_screen)
        user_not_found_screen.title("Success")
        user_not_found_screen.geometry("150x100")
        Label(user_not_found_screen, text="User Not Found").pack()
        Button(user_not_found_screen, text="OK", command=delete_user_not_found_screen).pack()

    # Deleting popups
    def delete_login_success():
        login_success_screen.destroy()
        print(u1)
        main_screen.destroy()
        return render_template('temp.html',user = u1)
    def delete_password_not_recognised():
        password_not_recog_screen.destroy()
    def delete_user_not_found_screen():
        user_not_found_screen.destroy()
    
    # Designing Main(first) window
    def main_account_screen():
        global main_screen
        main_screen = Tk()
        main_screen.geometry("300x250")
        main_screen.title("Account Login")
        Label(text="Select Your Choice", bg="blue", width="300", height="2", font=("Calibri", 13)).pack()
        Label(text="").pack()
        Button(text="Login", height="2", width="30", command = login).pack()
        Label(text="").pack()
        Button(text="Register", height="2", width="30", command=register).pack()

        main_screen.mainloop()
    
    main_account_screen()
    print(u1)
    return render_template('temp.html',user=u1.title(),enter=True)


# @app.route('/login',methods=['post','get'])
# def login():
#     return render_template("temp.html")

if __name__ == "__main__":
    app.debug = True
    app.run()



