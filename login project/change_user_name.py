
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

def change_user_name_f(id,password,new_name):
    """
    this is change user name function
    this function help you to change your user name in the database
    """
    connection = sqlite3.connect("users.db")
    cursor = connection.cursor()
    try:
        cursor.execute(f"select id from user where id = '{id}'")
        result=cursor.fetchone()
        if result!=None:
            cursor.execute(f"select user_password from user where id = '{id}' and user_password = '{hash_password(password)}'")
            result = cursor.fetchone()
            if result!=None:
                cursor.execute(f"select user_name from user where id = '{id}'")
                result = cursor.fetchone()
                if new_name != result[0]:
                    cursor.execute(f"select user_name from user where user_name = '{new_name}'")
                    result = cursor.fetchone()
                    if result == None:
                        cursor.execute(f"update user set user_name = '{new_name}' where id = '{id}'")
                        connection.commit()
                        return "name changed successful"
                    else:
                        return "duplicate name"
                else:
                    return "same name"
            else:
                return "password is wrong"
        else:
            return "id not found"
    finally:
        cursor.close()
        connection.close()