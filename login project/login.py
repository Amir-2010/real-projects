
import hashlib
import sqlite3

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


def login_f(user_name,user_password):
    """
    this function is login function
    this function help you to login into your account and use it
    """
    connection = sqlite3.connect("users.db")
    cursor=connection.cursor()
    try:
        cursor.execute(f"select user_name from user where user_name = '{user_name}'")
        result1 = cursor.fetchone()
        if result1 == None:
            return "user_name not found"
        else:
            cursor.execute(f"select user_password from user where user_name = '{user_name}' and user_password = '{hash_password(user_password)}'")
            result1 = cursor.fetchone()
            if result1 == None:
                return "password error"
            else:
                return "user is in"
    finally:
        cursor.close()
        connection.close()