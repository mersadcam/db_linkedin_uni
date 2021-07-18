from os import error
import sqlite3
from sqlite3.dbapi2 import Cursor, Error
import constants
import uuid
import secrets

class SQLCore:
    pass



class User:

    def __init__(self, db_connection):
        try:
            self.db_connection = db_connection
            self.db_cursor = self.db_connection.cursor()
            self.initialise_User()
            try:
                self.db_cursor.execute(constants.ENABLE_FOREIGN_KEY)
            except Error as e1:
                print(e1)
            self.db_connection.commit()
        except Error as e:
            print(e)

    #table creation
    def initialise_User(self):
        try:
            self.db_cursor.execute(constants.CREATE_TABLE_USER)
            self.db_cursor.execute(constants.CREATE_TABLE_PROFILE)
            self.db_cursor.execute(constants.CREATE_TABLE_CONNECTIONS)

            self.db_connection.commit()
        except Error as e:
            print(e)


    def user_insert(self, insert_table_values):
        try:
            self.db_cursor.execute(constants.INSERT_RECORD_USER, insert_table_values)
            self.db_connection.commit()
            return True
        except Error as e:
            print(e)
            # return (False, 'had problem adding your account! try again.')
            return False

    # user_id can be email or phoneNumber
    def user_delete(self, user_email, password):
        rv = self.user_select(user_email, password)
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

        rv = self.user_select(user_email, password)
        if rv.__len__() == 0:
            return (True, 'record was deleted successfully')
        else:
            return (False, 'we had a problem deleting your record, Try again!')
    

    def user_select(self, user_email, password): 
        self.db_cursor.execute(constants.SELECT_RECORD_USER, (user_email, password))                                 
        return(self.db_cursor.fetchall())


    def user_update(self, user_email, updated_values_with_fileds):
        # self.cursor_1.execute(constants.UPDATE_RECORD_USER, (updated_values_with_fileds, user_email))
        try:
            self.db_cursor.execute(f'UPDATE user SET {updated_values_with_fileds} WHERE user_email = \'{user_email}\'')
            self.db_connection.commit()
            return (True)
        except Error as e:
            return (False)


    def user_signUp(self, user_email, user_password):
        user_uuid = str(uuid.uuid4())
        user_token = self.tokenGenarator()

        user_values = (user_uuid, user_email, user_password, user_token)
        signup_flag = self.user_insert(user_values)

        if signup_flag:
            return (True, user_token)
        else:
            return (False, None)
        

    def user_login(self, user_email, user_password):
        selectedUser = self.user_select(user_email, user_password)
        if selectedUser.__len__() > 0:
            user_token = self.tokenGenarator()
            self.user_update(user_email, f"user_token = \'{user_token}\'")
            # print(user_email, f"user_token = \'{user_token}\'")
            return (True, user_token)
        else:
            return (False, None)

    def tokenGenarator(self):
        return secrets.token_urlsafe()


    
    #PROFILE METHODS
    def profile_insert(self, insert_table_values):
        try:
            self.db_cursor.execute(constants.INSERT_RECORD_PROFILE, insert_table_values)
            self.db_connection.commit()
            return True
        except Error as e:
            print(e)
            # return (False, 'had problem adding your account! try again.')
            return False
        
    def profile_select(self, user_id): 
        self.db_cursor.execute(constants.SELECT_RECORD_PROFILE, (user_id, user_id))                                 
        return(self.db_cursor.fetchall())

    def profile_update(self, user_uuid, updated_values_with_fileds):
        # self.cursor_1.execute(constants.UPDATE_RECORD_USER, (updated_values_with_fileds, user_email))
        updated_values_with_fileds
        try:
            self.db_cursor.execute(f'UPDATE profile SET {updated_values_with_fileds} WHERE user_uuid = \'{user_uuid}\'')
            self.db_connection.commit()
            return (True)
        except Error as e:
            return (False)



    #CONNECTION METHODS
    def connection_numberOfConnections(self, user_uuid):
        noc = self.db_cursor.execute(constants.SELECT_NOC_CONNECTIONS, (user_uuid, user_uuid))
        return noc.fetchall()


#profile test case
# profile_value = ('moouod', 'shahrizi', 'ce student', 'iran', '2000/00/00', 'shiraz', 'nothing about me', 0, 'moouod@mail', '6c2dad19-134e-483a-ba3b-5b6262cfc9bc')
# print(db.insert_profile(profile_value))

# a = db.numberOfConnections_profile('moouod@mail')





if __name__ == '__main__':
    try:
        db_connection = sqlite3.connect(constants.DB_NAME)
        user = User(db_connection)

        # a = user.user_signUp("mad@mail", "123")
        # a = user.user_login("mad@mail", "123")
        # a = user.user_select("mad@mail", "123")
        # a = user.user_update('mad@mail', "user_password = '123456', user_token = '' ")
        # a = user.user_delete('madd@mail', '123')

        
        #profile test case
        # profile_value = ('moouod', 'shahrizi', 'ce student', 'iran', '2000/00/00', 'shiraz', 'nothing about me', 0, 'moouod@mail', 'be49687e-be68-4f31-8feb-aac66fb2479b')
        # print(profile.insert_profile(profile_value))
        # a = profile.select_profile('be49687e-be68-4f31-8feb-aac66fb2479b')
        # a = profile.update_profile('be49687e-be68-4f31-8feb-aac66fb2479b', 'profile_first_name = "amir"')
        # a = db.select_profile('6c2dad19-134e-483a-ba3b-5b6262cfc9bc')
        
        # print(a)
        
        db_connection.close()
        

    except Error as e:
        print(e)
