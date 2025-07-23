
import hashlib
import sqlite3

def check_email(email):
    """
    this function is checking email function
    this is check the email is real or no
    and it check user input when (he/she) want to enter (his/her) email
    """
    valid_domains = ["@gmail.com", "@yahoo.com", "@hotmail.com", "@outlook.com", "@icloud.com", "@protonmail.com","@mail.com", "@aol.com", "@gmx.com", "@zoho.com"]
    for i in valid_domains:
        if i in email:
            return True
        else:
            return False

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

def sign_up_f(user_name,user_password,email):
    """
    this is sign up function
    this function help you to add your name into database and create one new account for your self
    """
    connection=sqlite3.connect("users.db")
    cursor=connection.cursor()
    try:
        cursor.execute(f"select user_name from user where user_name = '{user_name}'")
        sign_up_result=cursor.fetchone()
        if sign_up_result == None:
            if check_email(email)==True:
                cursor.execute(f"insert into user (user_name,user_password,email) values('{user_name}','{hash_password(user_password)}','{email.lower()}')")
                connection.commit()
                return "sign up is successful"
            else:
                return "invalid email"
        else:
            return "user_name is in the list"
    finally:
        cursor.close()
        connection.close()