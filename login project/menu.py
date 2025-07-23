
import sqlite3
import hashlib
from login import login_f
from sign_up import sign_up_f
from change_password import change_password_f
from change_user_name import change_user_name_f
from change_email import change_email_f
from delete_account import delete_account_f

exit=False
def hash_password(password):
    """
    his function help you to has your password for database
    And it's help you for the security of your password too
    if one team of hackers attack the database your password is safe
    """
    encoded=password.encode()
    obj=hashlib.sha3_256(encoded)
    hex=obj.hexdigest()
    return hex

def menu():
    """
    this function is a menu for the program
    this function show all of options my program have
    and it is connect to another functions to have a connection to another files
    """
    global exit
    while True:
        if exit == False:
            print("******************\n1.login\n2.sign up\n3.change user name\n4.change password\n5.change email\n6.delete account\n7.\033[31mexit\033[0m\n******************")
            user_input=input("what do you want to do?: ")
            while True:
                if user_input in ["1","login"]:
                    login()
                elif user_input in ["2","sign up"]:
                    sign_up()
                elif user_input in ["3","change user name"]:
                    change_user_name()
                elif user_input in ["4","change password"]:
                    change_password()
                elif user_input in ["5","change email"]:
                    change_email()
                elif user_input in ["6","delete account"]:
                    delete_account()
                elif user_input in ["7","exit"]:
                    exit=True
                    break
                else:
                    print("you must only enter numbers on the top")
                    menu()
        else:
            print("👋🏻good bye👋🏻")
            break

def login():
    """
    this is login function
    if you have an account you can login in to your account with this function
    """
    global exit
    if exit == False:
        name=input("enter your name: ")
        password=input("enter you account password: ")
        result1 = login_f(name,password)
        if result1 == "user_name not found":
            print("user name is not found\nbefore login you must to sign up")
        elif result1 == "password error":
            print("your password is wrong")
        elif result1 == "user is in":
            print("login is successful")
        menu()

def sign_up():
    """
    this is sign up function
    if you don't have account this function help you to create an account
    """
    global exit
    if exit == False:
        name = input("enter your name: ")
        password = input("select one password for your account: ")
        email = input("enter your email: ")
        result = sign_up_f(name,password,email)
        if result == "user_name is in the list":
            print("user name is in the list\ntry again with another name")
        elif result == "invalid email":
            print("this is not a real email\nenter your real email")
        elif result == "sign up is successful":
            print(f"your name is add to the list\nwelcome {name}")
        connection=sqlite3.connect("users.db")
        cursor=connection.cursor()
        cursor.execute(f"select user_name from user where user_name = '{name}'")
        name2=cursor.fetchone()
        if name2!=None:
            cursor.execute(f"select id from user where user_name = '{name}' and user_password = '{hash_password(password)}'")
            find_id=cursor.fetchone()
            print(f"your id is = \033[36m{find_id[0]}\033[0m\n\033[31myour id is so important write it some where\033[0m")
        cursor.close()
        connection.close()
        menu()

def change_user_name():
    """
    this is change user name function
    this function is connect you to the change user_name file and help you to change your name

    """
    global exit
    if exit == False:
        id = input("enter your id: ")
        password = input("enter your password: ")
        new_name = input("select new name for your account: ")
        result = change_user_name_f(id,password,new_name)
        if result == "id not found":
            print("id not found")
        elif result == "password is wrong":
            print("your password is wrong\ntry again")
        elif result == "same name":
            print("you can't select your old name\nselect another name")
        elif result == "duplicate name":
            print("this name is already in the list\nselect another name")
        elif result == "name changed successful":
            print(f"your name is changed to {new_name}")
        menu()

def change_password():
    """
    this is change password function
    this function is connect you to the change password file in this folder and help you to change your account password
    """
    global exit
    if exit == False:
        id = input("enter your id: ")
        password = input("enter your password: ")
        new_password = input("select your new password: ")
        result = change_password_f(id,password,new_password)
        if result == "id not found":
            print("your id is not found\ntry again with your id")
        elif result == "password is wrong":
            print("your password is wrong\ntry again")
        elif result == "password is change successful":
            print(f"your password is changed to \033[36m{new_password}\033[0m")
        menu()

def change_email():
    """
    this is change email function
    this function connect you to change email file in this folder and it help you to change your email
    """
    global exit
    if exit == False:
        id = input("enter your id: ")
        password = input("enter your password: ")
        email = input("select your new email: ")
        result = change_email_f(id,password,email)
        if result == "id not found":
            print("your id not found\ntry again")
        elif result == "wrong password":
            print("your password is wrong")
        elif result == "duplicate email":
            print("you can't user your last password")
        elif result == "email changed":
            print("your email changed successful")
        menu()

def delete_account():
    """
    this is delete account function
    this function help you to delete your account if you want
    this function connect you to delete account file in this folder and delete your account
    """
    global exit
    if exit == False:
        make_confirm = input("are you sure you want to delete account? ")
        if make_confirm in ["yes","Yes","YES","Y","y"]:
            id = input("enter your id: ")
            name = input("enter your name: ")
            password = input("enter your password: ")
            result = delete_account_f(id,name,password)
            if result == "id not found":
                print("id not found\nenter your id again")
            elif result == "name isn't match with id":
                print("your name isn't matching with id")
            elif result == "password is wrong":
                print("your password is wrong\ntry again")
            elif result == "account deleted":
                print("your account is deleted successful")
        elif make_confirm in ["no","No","NO","N","n"]:
            print("ok")
        else:
            print("you must to enter only yes or no")
    menu()

print("\033[36mif you have problem or you forgot your id send email to \033[31m'\033[36mAmir.hozhabri.h@gmail.com\033[31m'\033[0m")
menu()