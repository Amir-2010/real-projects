
import sqlite3
import hashlib

name = True
change_password_v = False

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

def change_password_f(id, password, new_password):
    """
    this function is change password fuction
    this function help you to change your password in database
    """
    connection = sqlite3.connect("users.db")
    cursor = connection.cursor()
    cursor.execute(f"select id from user where id = '{id}'")
    result = cursor.fetchone()
    if result != None:
        cursor.execute(f"select user_password from user where id = '{id}' and user_password = '{hash_password(password)}'")
        result = cursor.fetchone()
        if result != None and result[0] == hash_password(password):
            cursor.execute(f"update user set user_password = '{hash_password(new_password)}' where id = '{id}' and user_password = '{hash_password(password)}'")
            connection.commit()
            return "password is change successful"
        else:
            return "password is wrong"
    else:
        return "id not found"