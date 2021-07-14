import sqlite3
from sqlite3.dbapi2 import Error
import constants

class SQLCore:
    pass

class LinkeInDB:

    def __init__(self):
        try:
            self.db_connection = sqlite3.connect(constants.DB_NAME)
            self.cursor_1 = self.db_connection.cursor()
            self.initialTableCreation()
        except Error as e:
            print(e)
        

    def initialTableCreation(self):
        self.cursor_1.execute(constants.CREATE_TABLE_USER)
        self.db_connection.commit()

    def createTable():
        pass
    
    def deleteTable():
        pass

    def insert_user(self, user_email, user_phoneNumber, user_password):
        try:
            insert_table_values = (user_email, user_phoneNumber, user_password)
            self.cursor_1.execute(constants.INSERT_TABLE_USER, insert_table_values)
            self.db_connection.commit()
            return (True, 'account has been successfully added.')
        except Error as e:
            print(e)
            return (False, 'had problem adding your account! try again.')
        

    # user_id can be email or phoneNumber
    def delete_user(self, user_id, password):
        rv = self.select_user(user_id, password)
        if rv.__len__() == 0:
            return (False, 'NO SUCH RECORD FOUND!')

        self.cursor_1.execute(constants.DELETE_RECORD_USER, (user_id, user_id, password))
        self.db_connection.commit()

        rv = self.select_user(user_id, password)
        if rv.__len__() == 0:
            return (True, 'record was deleted successfully')
        else:
            return (False, 'we had a problem deleting your record, Try again!')
    

    def select_user(self, user_id, password): 
        self.cursor_1.execute(f"""SELECT * FROM user WHERE  (user_email = (?) OR user_phoneNumber = (?)) 
                                     AND user_password = (?)""", (user_id, user_id, password))                                 
        return(self.cursor_1.fetchall())


db = LinkeInDB()
a = db.insert_user("moouod@mail", "0936", "1234")
# a = db.select_user('0936', '1234')
# a = db.delete_user('0936', '1234')
print(a)

db.db_connection.close()
