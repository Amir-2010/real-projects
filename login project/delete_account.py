
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

def delete_account_f(id,name,password):
    """
    this function is delete account function
    this function help you to delete your account in the database
    """
    connection = sqlite3.connect("users.db")
    cursor = connection.cursor()
    cursor.execute(f"select id from user where id = '{id}'")
    result = cursor.fetchone()
    if result != None:
        cursor.execute(f"select user_name from user where id = '{id}' and user_name = '{name}'")
        result = cursor.fetchone()
        if result != None:
            cursor.execute(f"select user_password from user where id = '{id}' and user_name = '{name}' and user_password = '{hash_password(password)}'")
            result = cursor.fetchone()
            if result != None:
                cursor.execute(f"delete from user where id = '{id}' and user_name = '{name}' and user_password = '{hash_password(password)}'")
                connection.commit()
                return "account deleted"
            else:
                return "password is wrong"
        else:
            return "name isn't match with id"
    else:
        return "id not found"