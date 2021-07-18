from os import error
import sqlite3
from sqlite3.dbapi2 import Cursor, Error
import constants
import uuid
import secrets

class SQLCore:
    pass

# class Profile:
#     def __init__(self):
#         pass
    
    # def insert_profile(self, insert_table_values, db_connection):
    #     try:
    #         self.db_cursor.execute(constants.INSERT_RECORD_PROFILE, insert_table_values)
    #         db_connection.commit()
    #         return True
    #     except Error as e:
    #         print(e)
    #         # return (False, 'had problem adding your account! try again.')
    #         return False 

class Connection:
    def __init__(self, db_connection):
        self.db_connection = db_connection
        self.db_cursor = self.db_connection.cursor()
        self.db_cursor.execute(constants.CREATE_TABLE_CONNECTIONS)
        self.db_connection.commit()

    def numberOfConnections_profile(self, user_id):
        noc = self.db_cursor.execute(constants.SELECT_NOC_CONNECTIONS, (user_id, user_id))
        return noc.fetchall()


class Profile:
    def __init__(self, db_connection):
        self.db_connection = db_connection
        self.db_cursor = self.db_connection.cursor()
        self.db_cursor.execute(constants.CREATE_TABLE_PROFILE)
        self.db_connection.commit()

    def insert_profile(self, insert_table_values):
        try:
            self.db_cursor.execute(constants.INSERT_RECORD_PROFILE, insert_table_values)
            self.db_connection.commit()
            return True
        except Error as e:
            print(e)
            # return (False, 'had problem adding your account! try again.')
            return False
        
    def select_profile(self, user_id): 
        self.db_cursor.execute(constants.SELECT_RECORD_PROFILE, (user_id, user_id))                                 
        return(self.db_cursor.fetchall())


class User:

    def __init__(self, db_connection):
        try:
            self.db_connection = db_connection
            self.db_cursor = self.db_connection.cursor()
            self.db_cursor.execute(constants.CREATE_TABLE_USER)
            self.db_connection.commit()
            try:
                self.db_cursor.execute(constants.ENABLE_FOREIGN_KEY)
            except Error as e1:
                print(e1)
            self.db_connection.commit()
        except Error as e:
            print(e)


    def insert_user(self, insert_table_values):
        try:
            self.db_cursor.execute(constants.INSERT_RECORD_USER, insert_table_values)
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

        try:
            self.db_cursor.execute(constants.DELETE_RECORD_PROFILE, ('moouod@mail', ))
            self.db_connection.commit()
        except Error as e:
            print(e)
        try:
            self.db_cursor.execute(constants.DELETE_RECORD_USER, (user_email, password))
            self.db_connection.commit()
        except Error as e:
            print(e)

        rv = self.select_user(user_email, password)
        if rv.__len__() == 0:
            return (True, 'record was deleted successfully')
        else:
            return (False, 'we had a problem deleting your record, Try again!')
    

    def select_user(self, user_email, password): 
        self.db_cursor.execute(constants.SELECT_RECORD_USER, (user_email, password))                                 
        return(self.db_cursor.fetchall())


    def update_user(self, user_email, updated_values_with_fileds):
        # self.cursor_1.execute(constants.UPDATE_RECORD_USER, (updated_values_with_fileds, user_email))
        try:
            self.db_cursor.execute(f'UPDATE user SET {updated_values_with_fileds} WHERE user_email = \'{user_email}\'')
            self.db_connection.commit()
            return (True)
        except Error as e:
            return (False)


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


    




#profile test case
# profile_value = ('moouod', 'shahrizi', 'ce student', 'iran', '2000/00/00', 'shiraz', 'nothing about me', 0, 'moouod@mail', '6c2dad19-134e-483a-ba3b-5b6262cfc9bc')
# print(db.insert_profile(profile_value))
# a = db.select_profile('6c2dad19-134e-483a-ba3b-5b6262cfc9bc')
# a = db.numberOfConnections_profile('moouod@mail')





if __name__ == '__main__':
    try:
        db_connection = sqlite3.connect(constants.DB_NAME)
        user = User(db_connection)
        # profile = Profile(db_connection)
        # connection = Connection(db_connection)

        # a = user.signUp("moouod@mail", "123")
        # a = user.login('moouod@mail', '456')
        # a = user.select_user('moouod@mail', '123')
        # a = user.update_user('moouodd@mail', "user_password = '456', user_token = '', user_email = 'moouod@mail'")
        a = user.delete_user('moouod@mail', '456')

        print(a)
        
        # curosr = db_connection.cursor()
        # curosr.execute('UPDATE user set user_password = "123" where user_email = "moouod@mail"')
        
        
        db_connection.close()
        

    except Error as e:
        print(e)
