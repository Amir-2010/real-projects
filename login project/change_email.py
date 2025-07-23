
import sqlite3
import hashlib

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

def change_email_f(id,password,new_email):
    """
    this function is change email
    this function help you to change your email in the database
    """
    connection = sqlite3.connect("users.db")
    cursor = connection.cursor()
    cursor.execute(f"select id from user where id = '{id}'")
    result = cursor.fetchone()
    if result != None:
        cursor.execute(f"select user_password from user where id = '{id}' and user_password = '{hash_password(password)}'")
        result = cursor.fetchone()
        if result != None:
            cursor.execute(f"select email from user where id = '{id}'")
            result = cursor.fetchone()
            if result != new_email:
                cursor.execute(f"update user set email = '{new_email}' where id = '{id}' and user_password = '{hash_password(password)}'")
                connection.commit()
                return "email changed"
            else:
                return "duplicate email"
        else:
            return "wrong password"
    else:
        return "id not found"