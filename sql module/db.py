import sqlite3
from sqlite3.dbapi2 import Error
import constants
import uuid
import secrets

class SQLCore:
    pass

class LinkeInDB:

    def __init__(self, ):
        try:
            self.db_connection = sqlite3.connect(constants.DB_NAME)
            self.cursor_1 = self.db_connection.cursor()
            self.initialTableCreation()
        except Error as e:
            print(e)

    def startUp():
        pass    

    def initialTableCreation(self):
        self.cursor_1.execute(constants.CREATE_TABLE_USER)
        self.db_connection.commit()

    def insert_user(self, insert_table_values):
        try:
            self.cursor_1.execute(constants.INSERT_RECORD_USER, insert_table_values)
            self.db_connection.commit()
            return True
        except Error as e:
            print(e)
            # return (False, 'had problem adding your account! try again.')
            return False

    # user_id can be email or phoneNumber
    def delete_user(self, user_email, password):
        rv = self.select_user(user_email, password)
        if rv.__len__() == 0:
            return (False, 'NO SUCH RECORD FOUND!')

        self.cursor_1.execute(constants.DELETE_RECORD_USER, (user_email, password))
        self.db_connection.commit()

        rv = self.select_user(user_email, password)
        if rv.__len__() == 0:
            return (True, 'record was deleted successfully')
        else:
            return (False, 'we had a problem deleting your record, Try again!')
    

    def select_user(self, user_email, password): 
        self.cursor_1.execute(constants.SELECT_RECORD_USER, (user_email, password))                                 
        return(self.cursor_1.fetchall())


    def update_user(self, user_email, updated_values_with_fileds):
        # self.cursor_1.execute(constants.UPDATE_RECORD_USER, (updated_values_with_fileds, user_email))
        self.cursor_1.execute(f'UPDATE user SET {updated_values_with_fileds} WHERE user_email = \'{user_email}\'')
        self.db_connection.commit()


    def signUp(self, user_email, user_password):
        user_uuid = str(uuid.uuid4())
        user_token = self.tokenGenarator()

        user_values = (user_uuid, user_email, user_password, user_token)
        signup_flag = self.insert_user(user_values)

        if signup_flag:
            return (True, user_token)
        else:
            return (False, None)
        

    def login(self, user_email, user_password):
        selectedUser = self.select_user(user_email, user_password)
        if selectedUser.__len__() > 0:
            user_token = self.tokenGenarator()
            self.update_user(user_email, f"user_token = \'{user_token}\'")
            # print(user_email, f"user_token = \'{user_token}\'")
            return (True, user_token)
        else:
            return (False, None)

    def tokenGenarator(self):
        return secrets.token_urlsafe()


db = LinkeInDB()

# db.update_user('"moouod@mail"', "user_password = '456', user_token = '', user_email = 'mersad@email'")
# a = db.signUp("mersad@mail", "1234")
# a = db.select_user('mersad@mail', '1234')
# a = db.delete_user('mersad@mail', '1234')
a = db.login('mersad@email', '456')


print(a)

db.db_connection.close()
